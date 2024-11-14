from nuimages import NuImages

import labeled_dataset_extraction

nuim = NuImages(dataroot='./nuimages-v1.0-all-metadata', version='v1.0-test', verbose=True, lazy=False)

idx=0
log = []
file_object = open(f"./test_images.txt", "a")
for i in nuim.sample:
  sample = nuim.sample[idx]
  key_camera_token = sample['key_camera_token']
  #print(idx, key_camera_token)
  sample_data = nuim.get('sample_data', key_camera_token)
  filename = sample_data['filename']
  filename1 = filename.split('/')[2].split('.')[0]
  #log.append(filename1)
  file_object.write(f"{filename}\n")
  if idx == 100000:
    break
  else:
    idx+=1

file_object.close()
print(log)

original_folder = '/home/giang/AL-Yolov8/nuimages-v1.0-all-samples/'
#original_folder = '/home/giang/AL-Yolov8/nuimages-all-samples/train'
new_folder = '/home/giang/AL-Yolov8/nuimages-all-samples/test'

labeled_dataset_extraction.move_and_delete_files('test_images.txt', original_folder, new_folder)