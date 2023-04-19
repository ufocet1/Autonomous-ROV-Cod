import torch
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Load image
img = 'example.jpg'

# Perform detection
results = model(img)

# Get bounding box coordinates
detections = results.xyxy[0]

# Print bounding box coordinates
for i, box in enumerate(detections):
    LOGGER.info('Bounding box %d: (%.2f, %.2f, %.2f, %.2f)', i, box[0], box[1], box[2], box[3])
