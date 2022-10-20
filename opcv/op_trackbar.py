import numpy as np
import cv2 as cv


def nothing(x):
    pass


img = np.zeros((300, 512, 3), dtype=np.uint8)
cv.namedWindow('track_bar')
cv.createTrackbar('R', 'track_bar', 0, 255, nothing)
cv.createTrackbar('G', 'track_bar', 0, 255, nothing)
cv.createTrackbar('B', 'track_bar', 0, 255, nothing)
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'track_bar', 0, 1, nothing)
while (1):
    cv.imshow('track_bar', img)
    if cv.waitKey(1) == ord('q'):
        break
    r = cv.getTrackbarPos('R', 'track_bar')
    g = cv.getTrackbarPos('G', 'track_bar')
    b = cv.getTrackbarPos('B', 'track_bar')
    s = cv.getTrackbarPos(switch, 'track_bar')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]
cv.destroyAllWindows()



