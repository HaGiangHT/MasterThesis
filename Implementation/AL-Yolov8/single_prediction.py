import torch
import torchvision
import cv2

from models.experimental import attempt_load
from utils.torch_utils import select_device
from utils.general import check_img_size, non_max_suppression
from utils.datasets import LoadImages

device = select_device()

model = attempt_load("yolov8n.pt", map_location=device)  # load FP32 model
stride = int(model.stride.max())  # model stride
imgsz = check_img_size(640, s=stride)  # check img_size

dataset = LoadImages(
    "traindata/images/train/n008-2018-05-30-15-20-59-0400__CAM_BACK__1527708173137570.jpg",
    img_size=640,
    stride=32,
)

for path, img, im0s, vid_cap in dataset:
    img = torch.from_numpy(img).to(device).float().unsqueeze(0)
    img /= 255.0
    with torch.no_grad():
        output = model(img)[0]

    predictions = non_max_suppression(output, conf_thres=0.25, iou_thres=0.45)[0]

    # each prediction has format [x0, y0, x1, y1, conf, class_index]
    # the bounding box coordinates are in pixels and [0,0] is top left
    print(predictions)
    print(img.shape)

bboxes = predictions[:, :4]
labels = [str(int(label)) for label in predictions[:, 5].data]

img_pred = torchvision.utils.draw_bounding_boxes(
    (img[0] * 255).to(torch.uint8), bboxes, labels
).numpy()

# we need to convert from CxHxW to HxWxC
img_pred = img_pred.transpose((1, 2, 0))

cv2.imwrite("img_with_predictions2.jpg", img_pred)
