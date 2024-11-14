import os, random, shutil

with open('val_images.txt', 'a') as f:
    i = 0
    original_folder = './nuimages-all-samples/val'
    new_folder = './traindata/images/val'
    while i != 20: # number of val-images if dataset should be 20% and traindata 80% (here train: 500 samples)
        filename = random.choice(os.listdir(original_folder))
        f.write(filename.replace('.jpg', '.txt')+'\n')

        source_path = os.path.join(original_folder, filename)
        destination_path = os.path.join(new_folder, filename)
        # Copy the file to the new folder
        shutil.copy2(source_path, destination_path)

        # Delete the file from the original folder
        os.remove(source_path)
        i += 1

print("finish selecting random val images")
