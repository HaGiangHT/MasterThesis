from ultralytics import YOLO
from PIL import Image

# Load a pretrained YOLOv8n model
model = YOLO('runs/detect/train10/weights/best.pt')

# Define path to the image file
source = ['nuimages-all-samples/val/n003-2018-01-02-14-02-53+0800__CAM_BACK__1514873043448203.jpg',
          'nuimages-all-samples/val/n003-2018-01-02-14-02-53+0800__CAM_BACK__1514873227039030.jpg',
          'nuimages-all-samples/val/n003-2018-01-02-14-02-53+0800__CAM_BACK__1514873406879625.jpg',
          'nuimages-all-samples/val/n003-2018-01-02-14-02-53+0800__CAM_BACK__1514873788228367.jpg']



# Predict with the model
#results = model(source)  # predict on an image

model.predict(source, save=True, save_txt=True, save_conf=True, conf=0.5)