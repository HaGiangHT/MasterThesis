import pandas as pd
import os

# Define the column name to search for the highest value
column_name = '       metrics/mAP50(B)'

# Define the folders where the CSV files are located
root = '../Server_Client_NoneF'
folders = [f'{root}/runs/detect/train',
           f'{root}/runs/detect/train2',
           f'{root}/runs/detect/train3',
           f'{root}/runs/detect/train4',
           f'{root}/runs/detect/train5',
           f'{root}/runs/detect/train6',
           f'{root}/runs/detect/train7',
           f'{root}/runs/detect/train8',
           f'{root}/runs/detect/train9',
           f'{root}/runs/detect/train10',
           f'{root}/runs/detect/train32'
           ]

# Initialize a dictionary to store the highest values
highest_values = {}
iteration = 1
# Iterate over each folder
for folder in folders:
    # Construct the file path
    file_path = os.path.join(folder, 'results.csv')
    # Check if the file exists
    if os.path.isfile(file_path):
        # Read the CSV file
        data = pd.read_csv(file_path)
        # Get the highest value in the specified column
        highest_value = data[column_name].max()
        # Store the highest value with the folder name as the key
        highest_values[iteration] = highest_value
        iteration = iteration + 1

# Convert the dictionary to a DataFrame
highest_values_df = pd.DataFrame(list(highest_values.items()), columns=['Training Cycle', 'mAP50'])

highest_values_df['Used Data'] = 1000 + 1000 * highest_values_df.index

# Define the output file name
output_file = '../csv/mAP50xIterationxUsedData_NoneF.csv'

# Save the DataFrame to a CSV file
highest_values_df.to_csv(output_file, index=False)

# Print a success message
print(f"The highest values have been saved to {output_file}.")
