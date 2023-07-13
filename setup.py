# from torch import hub
import torch
# model = hub.load('ultralytics/yolov5', 'yolov5n', pretrained=True)
model = torch.hub.load("ultralytics/yolov3", custom(detection/yolov3-tiny.pt))