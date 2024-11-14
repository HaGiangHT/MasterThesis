import pandas as pd
import os

# Define the column name to search for the highest value
column_name = '       metrics/mAP50(B)'

# Define the folders where the CSV files are located
root = '../Server_Client_NoneF'
output_file = '../csv/all_mAP50_values_with_index_NoneF.csv'

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

# Initialize a list to store all mAP50 values
mAP50_values = []

# Iterate over each folder
for folder in folders:
    # Construct the file path
    file_path = os.path.join(folder, 'results.csv')
    # Check if the file exists
    if os.path.isfile(file_path):
        # Read the CSV file
        data = pd.read_csv(file_path)
        # Extract the 'mAP50' values
        mAP50_values.extend(data[column_name])

# Create a DataFrame from the list of mAP50 values with an additional index column
mAP50_df = pd.DataFrame({'Index': range(1, len(mAP50_values) + 1), 'mAP50': mAP50_values})

# Define the output file name

# Save the DataFrame to a CSV file
mAP50_df.to_csv(output_file, index=False)

# Print a success message
print(f"All mAP50 values with an index column have been saved to {output_file}.")
