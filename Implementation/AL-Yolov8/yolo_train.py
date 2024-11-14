from ultralytics import YOLO
import os

# https://stackoverflow.com/questions/2014554/find-the-newest-folder-in-a-directory-in-python
def all_subdirs_of(b='.'):
  result = []
  for d in os.listdir(b):
    bd = os.path.join(b, d)
    if os.path.isdir(bd): result.append(bd)
  return result

try:
  # Load a model
  if max(all_subdirs_of('./runs/detect'), key=os.path.getmtime, default=None) is not None:
    latest_subdir = max(all_subdirs_of('./runs/detect'), key=os.path.getmtime)
    current_best_model_path = latest_subdir + '/weights/best.pt'
    model = YOLO(current_best_model_path)
  else:
    model = YOLO('yolov8m.pt')

  # Train the model
  results = model.train(data='./nuimages.yaml', epochs=20, imgsz=640, device=0)

except Exception as e:
  print(f"Error sending message to a client: {e}")
