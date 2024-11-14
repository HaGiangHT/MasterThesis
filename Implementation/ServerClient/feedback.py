import copy
import json
import shutil

from ultralytics import YOLO
import os
import re
import csv
import pandas as pd

def all_subdirs_of(b='.'):
  result = []
  for d in os.listdir(b):
    bd = os.path.join(b, d)
    if os.path.isdir(bd) and 'train' in d.lower(): result.append(bd)
  return result

def latest_training_class_metrics():
    first_row = ['Class','Precision','Recall','mAP50', 'mAP50-95']
    if len(all_subdirs_of('./runs/detect')) == 0:
        print('No runs detected')
    elif os.path.exists(max(all_subdirs_of('./runs/detect'), key=os.path.getmtime) + '/class_metrics.csv')\
            and os.path.exists(max(all_subdirs_of('./runs/detect'), key=os.path.getmtime) + '/new_balancing.json'):
        latest_subdir = max(all_subdirs_of('./runs/detect'), key=os.path.getmtime)
        match = re.search(r'train(\d+)', latest_subdir)
        if match:
            current_training_number = match.group(1)
            return current_training_number
    else:
        latest_subdir = max(all_subdirs_of('./runs/detect'), key=os.path.getmtime)
        current_best_model_path = latest_subdir + '/weights/best.pt'
        model = YOLO(current_best_model_path)
        metrics = model.val()
        all_class_metric = [first_row]
        for i in range(6):
            if i == 0:
                class_name = 'person'
            elif i == 1:
                class_name = 'bicycle'
            elif i == 2:
                class_name = 'car'
            elif i == 3:
                class_name = 'motorcycle'
            elif i == 4:
                class_name = 'bus'
            else:
                class_name = 'truck'
            metric_i = [class_name] + list(metrics.class_result(i))
            all_class_metric.append(metric_i)
        csv_file_path = latest_subdir + '/class_metrics.csv'
        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in all_class_metric:
                csv_writer.writerow(row)
        match = re.search(r'train(\d+)', latest_subdir)
        if match:
            current_training_number = match.group(1)
            return current_training_number
        else:
            training_number = ''
            # return training_number
        print("new csv file saved")

# generate feedback here
def read_from_csv(current_training_number):
    print(current_training_number)
    if current_training_number is not None and int(current_training_number) >= 5:#5
        csv_file_path_current = f'Server_Client_NoneF/runs/detect/train{current_training_number}/class_metrics.csv'
        df_current = pd.read_csv(csv_file_path_current)
        training_number_minus_1 = int(current_training_number) - 1
        # print(training_number_minus_1)
        training_number_minus_2 = int(current_training_number) - 2
        # print(training_number_minus_2)

        df_minus_1 = pd.read_csv(f'Server_Client_NoneF/runs/detect/train{training_number_minus_1}/class_metrics.csv')
        df_minus_2 = pd.read_csv(f'Server_Client_NoneF/runs/detect/train{training_number_minus_2}/class_metrics.csv')
        df_current['Dataset'] = 'df_current'
        df_minus_1['Dataset'] = 'df_minus_1'
        df_minus_2['Dataset'] = 'df_minus_2'
        all_df = pd.concat([df_minus_2, df_minus_1, df_current])
        grouped_data = all_df.groupby(['Class', 'Dataset'])['mAP50'].mean().unstack()
        grouped_data = grouped_data[['df_minus_2', 'df_minus_1', 'df_current']]
        increase = grouped_data.diff(axis=1)
        total_increase = increase.sum(axis=1)

        class_lowest_increase = total_increase.idxmin()
        increase_value_lowest_class = increase.loc[class_lowest_increase].sum()
        print('Class lowest')
        print(class_lowest_increase, increase_value_lowest_class)

        class_second_lowest_increase = total_increase.nsmallest(2).index[1]
        increase_value_second_lowest_class = increase.loc[class_second_lowest_increase].sum()
        print('Class second lowest')
        print(class_second_lowest_increase, increase_value_second_lowest_class)

        class_highest_increase = total_increase.idxmax()
        increase_value_highest_class = increase.loc[class_highest_increase].sum()
        print('Class highest')
        print(class_highest_increase, increase_value_highest_class)

        class_second_highest_increase = total_increase.nlargest(2).index[1]
        increase_value_second_highest_class = increase.loc[class_second_highest_increase].sum()
        print('Class second highest')
        print(class_second_highest_increase, increase_value_second_highest_class)

        # make comparison here
        if current_training_number == 5:
            with open("./initial_balancing.json", "r") as file:
                data = json.load(file)
        else:
            with open(f"Server_Client_NoneF/runs/detect/train{training_number_minus_1}/new_balancing.json", "r") as file:
                data = json.load(file)

        updates =  {}
        if increase_value_lowest_class < 0.01 or increase_value_highest_class >= 0.05:
            if data[class_highest_increase] >= 0.1:
                #print("check 3")
                class_lowest_increase_value = data[class_lowest_increase] + 0.05
                class_lowest_increase_value = round(class_lowest_increase_value, 3)
                class_highest_increase_value = data[class_highest_increase] - 0.05
                class_highest_increase_value = round(class_highest_increase_value, 3)

                updates[class_highest_increase] = class_highest_increase_value
                updates[class_lowest_increase] = class_lowest_increase_value
                #print(class_lowest_increase_value, class_highest_increase_value)

        if increase_value_second_lowest_class < 0.01 or increase_value_second_highest_class >= 0.03:
            if data[class_second_highest_increase] >= 0.1:
                class_second_lowest_increase_value = data[class_second_lowest_increase] + 0.025
                class_second_lowest_increase_value = round(class_second_lowest_increase_value, 3)
                class_second_highest_increase_value = data[class_second_highest_increase] - 0.025
                class_second_highest_increase_value = round(class_second_highest_increase_value, 3)
                updates[class_second_highest_increase] = class_second_highest_increase_value
                updates[class_second_lowest_increase] = class_second_lowest_increase_value

        update_value(updates, current_training_number)
    elif current_training_number is None:
        src_path = os.path.join('./initial_balancing.json')
        dest_path = os.path.join(f'Server_Client_NoneF/runs/detect/train/new_balancing.json')
        # Copy the file
        shutil.copyfile(src_path, dest_path)
    else:
        src_path = os.path.join('./initial_balancing.json')
        dest_path = os.path.join(f'Server_Client_NoneF/runs/detect/train{current_training_number}/new_balancing.json')
        # Copy the file
        shutil.copyfile(src_path, dest_path)

def update_value(updates, current_training_number):
    training_number_minus_1 = int(current_training_number) - 1
    if current_training_number == 5:
        #print("AAAA")
        with open("./initial_balancing.json", "r") as file:
            json_data  = json.load(file)
    else:
        #print("BBBB")
        with open(f"Server_Client_NoneF/runs/detect/train{training_number_minus_1}/new_balancing.json", "r") as file:
            json_data  = json.load(file)

    for key, value in updates.items():
        json_data[key] = value

    with open(f"Server_Client_NoneF/runs/detect/train{current_training_number}/new_balancing.json", "w") as file:
        json.dump(json_data, file, indent=4)
    print("New Balancing saved")



read_from_csv(latest_training_class_metrics())
#read_from_csv(None)



