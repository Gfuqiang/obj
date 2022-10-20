import cv2
import numpy as np


img = np.zeros((3, 3), dtype=np.uint8)
img1 = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)


print(img1)