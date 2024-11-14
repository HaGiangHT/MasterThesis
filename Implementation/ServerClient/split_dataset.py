
import random
import os
import shutil

# Assuming your images are in a directory, and each class has its own subdirectory
data_dir = '/home/giang/AL-Yolov8/nuimages-all-samples/train'
output_dirs = [
    '/home/giang/ServerClient/Server_Client_NoneF/client{}_dataset/stored{}'.format(i, i)
    for i in range(10)
]

# List all image files in the data directory
image_files = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith('.jpg')]

# Shuffle the list of image files randomly
random.shuffle(image_files)

# Calculate the size of each part
part_size = len(image_files) // 10

# Split the image files into 10 equal parts
image_parts = [image_files[i * part_size: (i + 1) * part_size] for i in range(10)]

# Create output directories if they don't exist
for output_dir in output_dirs:
    os.makedirs(output_dir, exist_ok=True)

# Copy images to the output directories
for i, images_part in enumerate(image_parts):
    for image in images_part:
        shutil.copy(image, os.path.join(output_dirs[i], os.path.basename(image)))