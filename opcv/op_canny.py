import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images/hmbb.jpeg')


def nothing(x):
    pass


cv.namedWindow('canny_img')
minVal = cv.createTrackbar('min', 'canny_img', 0, 400, nothing)
maxVal = cv.createTrackbar('max', 'canny_img', 100, 500, nothing)
edges = cv.Canny(img, 100, 200)
while True:
    cv.imshow('canny_img', edges)
    if cv.waitKey(1) == ord('q'):
        break
    min_val = cv.getTrackbarPos('min', 'canny_img')
    max_val = cv.getTrackbarPos('max', 'canny_img')
    edges = cv.Canny(img, min_val, max_val)


# plt.subplot(121), plt.imshow(img), plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(edges), plt.title('edges'), plt.xticks([]), plt.yticks([])
# plt.show()