import pandas as pd
import os

# Define the classes
classes = ['person', 'bicycle', 'car', 'motorcycle', 'bus', 'truck']

# Define the folders where the CSV files are located
root = '../Server_Client_NoneF'
output_file = '../csv/class_mAP50_values_NoneF.csv'
folders = [f'{root}/runs/detect/train',
           f'{root}/runs/detect/train2',
           f'{root}/runs/detect/train3',
           f'{root}/runs/detect/train4',
           f'{root}/runs/detect/train5',
           f'{root}/runs/detect/train6',
           f'{root}/runs/detect/train7',
           f'{root}/runs/detect/train8',
           f'{root}/runs/detect/train9',
           f'{root}/runs/detect/train10']

# Initialize a dictionary to store mAP50 values for each class
class_mAP50_values = {cls: [] for cls in classes}

# Iterate over each folder
for folder in folders:
    # Construct the file path
    file_path = os.path.join(folder, 'class_metrics.csv')
    # Check if the file exists
    if os.path.isfile(file_path):
        # Read the CSV file
        data = pd.read_csv(file_path)
        # Iterate over each class
        for cls in classes:
            # Extract the mAP50 value for the class
            mAP50_value = data[data['Class'] == cls]['mAP50'].values[0]  # Assuming column names are 'class' and 'mAP50'
            # Append the mAP50 value to the respective class list
            class_mAP50_values[cls].append(mAP50_value)

# Create a DataFrame from the dictionary
class_mAP50_df = pd.DataFrame(class_mAP50_values)

# Define the output file name


# Save the DataFrame to a CSV file
class_mAP50_df.to_csv(output_file, index=False)

# Print a success message
print(f"The mAP50 values for each class have been saved to {output_file}.")
