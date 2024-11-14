import pandas as pd
import os

# Define the classes
classes = ['person', 'bicycle', 'car', 'motorcycle', 'bus', 'truck']

# Define the folders where the CSV files are located
folders = ['../runs_new/detect/train',
           '../runs_new/detect/train2',
           '../runs_new/detect/train3',
           '../runs_new/detect/train4',
           '../runs_new/detect/train5',
           '../runs_new/detect/train6',
           '../runs_new/detect/train7',
           '../runs_new/detect/train8',
           '../runs_new/detect/train9',
           '../runs_new/detect/train10']

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
output_file = 'class_mAP50_values.csv'

# Save the DataFrame to a CSV file
class_mAP50_df.to_csv(output_file, index=False)

# Print a success message
print(f"The mAP50 values for each class have been saved to {output_file}.")
