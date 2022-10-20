import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('images/j.png')
kernel = np.ones((5, 5), dtype=np.uint8)
erosion = cv.erode(img, kernel, iterations=1)
dilation = cv.dilate(img, kernel, iterations=1)
# 形态学梯度，
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
plt.subplot(221), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(222), plt.imshow(erosion), plt.title('erosion')
plt.xticks([]), plt.yticks([])

plt.subplot(223), plt.imshow(dilation), plt.title('dilation')
plt.xticks([]), plt.yticks([])

plt.subplot(224), plt.imshow(opening), plt.title('opening')
plt.xticks([]), plt.yticks([])
plt.show()