import os
import shutil



def get_all_names_in_folder(folder_path):
    try:
        file_list = os.listdir(folder_path)
        with open('Server_Client_NoneF/train_names_txt.txt', 'w') as txt_file:
            for file_name in file_list:
                txt_file.write(file_name.replace('.jpg', '.txt') + '\n')

        print("File names written to 'train_names_txt.txt'")
    except Exception as e:
        print(f"Error {e}")

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
        #os.remove(source_path)

get_all_names_in_folder("./Server_Client_NoneF/traindata/images/train")

move_and_delete_files("./Server_Client_NoneF/val_images.txt",
                      "./Server_Client_NoneF/nuimages-samples/labels/val",
                      "./Server_Client_NoneF/traindata/labels/val")

move_and_delete_files("./Server_Client_NoneF/train_names_txt.txt",
                      "./Server_Client_NoneF/nuimages-samples/labels/train",
                      "./Server_Client_NoneF/traindata/labels/train")