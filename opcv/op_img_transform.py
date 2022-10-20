import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images/hmbb.jpeg')
res = cv.resize(img, None, fx=0.25, fy=0.25, interpolation=cv.INTER_CUBIC)
cv.imwrite('images/small.jpeg', res)


