import pandas as pd
import os

# Define the column name to search for the highest value
column_name = '       metrics/mAP50(B)'

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
output_file = '../csv/mAP50xIterationxUsedData2.csv'

# Save the DataFrame to a CSV file
highest_values_df.to_csv(output_file, index=False)

# Print a success message
print(f"The highest values have been saved to {output_file}.")
