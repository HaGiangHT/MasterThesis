import os
import shutil
from lightly.api import ApiWorkflowClient
import sys

if len(sys.argv) < 2:
    print("Usage: python labeled_dataset_extraction_client.py <client_id>")

client_id = sys.argv[1]
print(client_id)

dataset_id = ApiWorkflowClient(token="976331148fad69677c163a1d8eb788c4f42141356697e9be").get_datasets_by_name(f"client{client_id}_datasetNoneF")[0].id

# Create the Lightly client to connect to the API.
#client = ApiWorkflowClient(token="976331148fad69677c163a1d8eb788c4f42141356697e9be", dataset_id="65ac518afc3bfd1925690ebe")
client = ApiWorkflowClient(token="976331148fad69677c163a1d8eb788c4f42141356697e9be", dataset_id=dataset_id)

def move_and_delete_files(file_list_path, original_folder, new_folder):
    # Create the new folder if it doesn't exist
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    # Read the list of files from the text file
    with open(file_list_path, 'r') as file:
        file_names = [line.strip() for line in file]

    # Move each file to the new folder
    for file_name in file_names:
        source_path = os.path.join(original_folder, file_name)
        destination_path = os.path.join(new_folder, file_name)

        # Copy the file to the new folder
        shutil.copy2(source_path, destination_path)

        # Delete the file from the original folder
        os.remove(source_path)

    print("Files moved and deleted successfully.")

# exporting selected0 labels
tags = client.get_all_tags()
filename = client.export_filenames_by_tag_name(tags[0].name)
print(tags[0].name)
with open(f"Server_Client_NoneF/filenames/filenames-of-{tags[0].name}.txt", "w") as f:
         f.write(filename)

filenames_images = "Server_Client_NoneF/filenames/filenames-of-" + tags[0].name + ".txt"
filenames_labels = "Server_Client_NoneF/filenames/filenames-of-" + tags[0].name + "_txt.txt"

# get file with corresponding labels
with open(filenames_images, "rt") as fin:
    with open(filenames_labels, "wt") as fout:
        for line in fin:
            fout.write(line.replace('.jpg', '.txt'))


# extracting selected0 images + labels
file_list_path_images = filenames_images
original_folder_images = f'./Server_Client_NoneF/client{client_id}_dataset/stored{client_id}'
new_folder_images = f'./Server_Client_NoneF/client{client_id}_dataset/selected{client_id}'

move_and_delete_files(file_list_path_images, original_folder_images, new_folder_images)

# file_list_path_labels = filenames_labels
# original_folder_labels = '/home/giang/AL-Yolov8/labels/train'
# new_folder_labels = './traindata/labels/train'
#
# move_and_delete_files(file_list_path_labels, original_folder_labels, new_folder_labels)
