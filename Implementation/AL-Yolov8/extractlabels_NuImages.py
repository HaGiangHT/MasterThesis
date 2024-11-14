
import os
from nuimages import NuImages

nuim = NuImages(dataroot='./nuimages-v1.0-all-metadata', version='v1.0-val', verbose=True, lazy=False)

person = ['human.pedestrian.adult','human.pedestrian.child', 'human.pedestrian.construction_worker',
          'human.pedestrian.personal_mobility', 'human.pedestrian.police_officer', 'human.pedestrian.stroller', 'human.pedestrian.wheelchair']
bicycle = ['vehicle.bicycle', 'static_object.bicycle_rack']
car =['vehicle.car', 'vehicle.emergency.police', 'vehicle.emergency.ambulance']
motorcycle = ['vehicle.motorcycle']
bus = ['vehicle.bus.bendy', 'vehicle.bus.rigid']
truck =['vehicle.truck', 'vehicle.construction', 'vehicle.trailer']

def class_number(category_name: str):
  if category_name in person:
    return 0
  elif category_name in bicycle:
    return 1
  elif category_name in car:
    return 2
  elif category_name in motorcycle:
    return 3
  elif category_name in bus:
    return 4
  elif category_name in truck:
    return 5


def extract_label(sd_token: str):
    x1: int
    y1: int
    x2: int
    y2: int
    c: int
    log = []
    # Validate inputs.
    sample_data = nuim.get('sample_data', sd_token)
    # print(sd_token)
    filename = sample_data['filename']
    filename1 = filename.split('/')[2].split('.')[0]
    filename2 = filename.split('.')[0]
    log.append(filename1)

    # file_object = open(f"/data/sets/nuimages/{filename2}.txt","a")
    file_object = open(f"nuimages-all-samples/labels/val/{filename1}.txt", "a")

    # Load object instances.
    object_anns = [o for o in nuim.object_ann if o['sample_data_token'] == sd_token]

    for ann in object_anns:
        category_token = ann['category_token']
        category_name = nuim.get('category', category_token)['name']
        c = class_number(category_name)
        bbox = ann['bbox']
        if ann['mask'] is not None:
            size = ann['mask']['size']
            # print(size)
            img_h = size[0]
            img_w = size[1]
            x1 = bbox[0]
            y1 = bbox[1]
            x2 = bbox[2]
            y2 = bbox[3]

            x_centre = ((x2 - x1) / 2) + x1
            y_centre = ((y2 - y1) / 2) + y1
            width = x2 - x1
            height = y2 - y1

            # Normalize
            x_centre = x_centre / img_w
            y_centre = y_centre / img_h
            width = width / img_w
            height = height / img_h

            # Limiting upto fix decimal
            x_centre = format(x_centre, '.6f')
            y_centre = format(y_centre, '.6f')
            width = format(width, '.6f')
            height = format(height, '.6f')
            if c is not None:
                # print(c,x1,y1,x2,y2)
                # log.append([c, x_centre, y_centre, width, height])
                file_object.write(f"{c} {x_centre} {y_centre} {width} {height}\n")

    file_object.close()
    #if os.stat(f"./labels/{filename1}.txt").st_size == 0:
    #    os.remove(f"/labels/{filename1}.txt")


idx=0
for i in nuim.sample:
  sample = nuim.sample[idx]
  key_camera_token = sample['key_camera_token']
  #print(idx, key_camera_token)
  extract_label(key_camera_token)
  if idx == 100000:
    break
  else:
    idx+=1