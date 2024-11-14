from ultralytics import YOLO
from pathlib import Path
import json
import os
import cv2

#model = YOLO("yolov8x.pt")  # load a pretrained model (recommended for training)
def all_subdirs_of(b='.'):
  result = []
  for d in os.listdir(b):
    bd = os.path.join(b, d)
    if os.path.isdir(bd) and 'train' in d.lower(): result.append(bd)
  return result

if max(all_subdirs_of('./runs/detect'), key=os.path.getmtime, default=None) is not None:
    latest_subdir = max(all_subdirs_of('./runs/detect'), key=os.path.getmtime)
    current_best_model_path = latest_subdir + '/weights/best.pt'
    model = YOLO(current_best_model_path)
else:
    model = YOLO('yolov8m.pt')

predictions_root_path = Path("lightly/pred/.lightly/predictions")
task_name = "yolov8_detection"
predictions_path = Path(predictions_root_path / task_name)

# following coco class numeration
important_classes = {
    "person": 0,
    "bicycle": 1,
    "car": 2,
    "motorcycle": 3,
    "airplane": 4,
    "bus": 5,
    "train":  6,
    "truck": 7}

classes = list(important_classes.values())


# create tasks.json
tasks_json_path = predictions_root_path / "tasks.json"
tasks_json_path.parent.mkdir(parents=True, exist_ok=True)

with open(tasks_json_path, "w") as f:
    json.dump([task_name], f)


# create schema.json
schema = {"task_type": "object-detection", "categories": []}
for key, val in important_classes.items():
    cat = {"id": val, "name": key}
    schema["categories"].append(cat)

schema_path = predictions_path / "schema.json"
schema_path.parent.mkdir(parents=True, exist_ok=True)

with open(schema_path, "w") as f:
    json.dump(schema, f, indent=4)


#videos = Path("data/").glob("*.avi")
images = Path("./nuimages-all-samples/train/").glob("*.jpg")
#print("Hello")
#print(Path("./nuimages-v1.0-all-samples/samples/CAM_BACK/n003-2018-01-02-11-48-43+0800__CAM_BACK__1514864956159109.jpg").is_file())


i = 0
for image in images:
    # if i == 2:
    #     break
    # else:
    #     i += 1
    #print("Hello 1 image")
    results = model.predict(image, conf=0.3, device=0, classes=classes )
    #print("here are the results:", results)
    predictions = [result.boxes for result in results]
    #print("YOOOOOOOOO:", predictions)

    # convert filename to lightly format
    # 'data/passageway1-c0.avi' --> 'data/passageway1-c0-0001-avi.json'
    #number_of_frames = len(predictions)
    #padding = len(str(number_of_frames))  # '1234' --> 4 digits
    fname =image.name
    #print(fname)


    for idx, prediction in enumerate(predictions):
        # NOTE: prediction file_name must be a .png file as the Lightly Worker
        # treats extracted frames from videos as PNGs
        lightly_prediction = {
            #"file_name": str(Path(fname_prediction).with_suffix(".png")),
            "file_name": fname,
            "predictions": [],
        }
        #print("PREDICTION", prediction)

        for pred in prediction:
            #print("PRED:", pred.data)
            x0, y0, x1, y1, conf, class_id = pred.data[0]
            #print(important_classes)
            #print(pred.data[0])
            #print(class_id)

            # skip predictions thare are not part of the important_classes
            if class_id in important_classes.values():
                # note that we need to conver form x0, y0, x1, y1 to x, y, w, h format
                pred = {
                    "category_id": int(class_id),
                    "bbox": [int(x0), int(y0), int(x1 - x0), int(y1 - y0)],
                    "score": float(conf),
                }
                lightly_prediction["predictions"].append(pred)

                # create the prediction file for the image
                path_to_prediction = predictions_path / Path(
                    fname
                ).with_suffix(".json")

                path_to_prediction.parents[0].mkdir(parents=True, exist_ok=True)
                with open(path_to_prediction, "w") as f:
                    json.dump(lightly_prediction, f, indent=4)
