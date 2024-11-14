import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV files and select only the desired class columns
class_to_use = 'bicycle'  # Replace 'desired_class' with the name of the class you want to use

class_mAP50_df_1 = pd.read_csv('../../ServerClient/csv/class_mAP50_values_30.csv', usecols=[class_to_use])
class_mAP50_df_2 = pd.read_csv('../../ServerClient/csv/class_mAP50_values_30N.csv', usecols=[class_to_use])
class_mAP50_df_3 = pd.read_csv('../../ServerClient/csv/class_mAP50_values_30F.csv', usecols=[class_to_use])


class_mAP50_df_1.columns = [class_to_use]
class_mAP50_df_2.columns = [class_to_use]
class_mAP50_df_3.columns = [class_to_use]

# Combine the dataframes
class_mAP50_df = pd.concat([class_mAP50_df_1, class_mAP50_df_2, class_mAP50_df_3], axis=1)

# Plotting the mAP50 values for the desired class
plt.figure(figsize=(10, 6))
plt.plot(class_mAP50_df.index + 1, class_mAP50_df[class_to_use], marker='o')

# Adding title and labels
plt.title(f'Bicycle')
plt.xlabel('Iteration')
plt.ylabel('mAP50')

plt.legend(['CS_30_RF', 'CS_30_A', 'CS_30_AF'])

# Display the plot
plt.xticks(range(1, 11, 1))
plt.grid(True)
plt.tight_layout()
plt.savefig(f'../graphs/{class_to_use}_mAP50_plot30.png')
