import cv2 as cv
import numpy as np

img = np.zeros((512, 512, 3), dtype=np.uint8)
# 画线, 参数：起点，终点坐标，bgr值，线条厚度
cv.line(img, (0, 0), (512, 512), (255, 0, 0), 5)
# 长方形 左上角，右下角坐标
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 1)
while True:
    cv.imshow('line', img)
    if cv.waitKey(1) == ord('q'):
        break