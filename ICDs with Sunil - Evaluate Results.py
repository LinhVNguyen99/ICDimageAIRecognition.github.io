import cv2
import matplotlib.pyplot as plt

results_file = "/Users/linhnguyen/yolov5/runs/train/exp6/results.png"

img = cv2.imread(results_file)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("training metrics")
plt.show()

