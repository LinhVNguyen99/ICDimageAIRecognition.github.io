import os
import cv2
import random
import matplotlib.pyplot as plt
import yaml

# Visualize a random image from a trained dataset
image_dir = "/Users/linhnguyen/ICD-Xray-Image-Recognition-5/train/images"
random_image = random.choice(os.listdir(image_dir))
image_path = os.path.join(image_dir, random_image)

image = cv2.imread(image_path)
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("random image from trained dataset")
plt.show()

'''
# Train YOLOv5 model
!python3 train.py --img 640 --batch 16 --epochs 50 --data /Users/linhnguyen/ICD-Xray-Image-Recognition-5/data.yaml --weights yolov5s.pt --device cpu
'''
