import numpy as np
import cv2 as cv


def draw_circle(event, x, y, flags, param):

    if event == cv.EVENT_LBUTTONDBLCLK:
        print('input draw_circle func')
        cv.circle(img, (x, y), 100, (255, 0, 0), -1)


# Create a black image, a window and bind the function to window
img = np.zeros((512, 512, 3), dtype=np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)
while (1):
    cv.imshow('image', img)
    if cv.waitKey(1) == ord('q'):
        break
cv.destroyAllWindows()
