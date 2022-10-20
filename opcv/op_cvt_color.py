import cv2 as cv
import numpy as np


def get_hsv():
    cap = cv.VideoCapture(0)
    while True:
        _, frame = cap.read()
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        # 获取蓝色范围
        lower_blue = np.array([50, 100, 100])
        upper_blue = np.array([70, 255, 255])
        # Threshold the HSV image to get only blue colors
        mask = cv.inRange(hsv, lower_blue, upper_blue)
        # Bitwise-AND mask and original image
        res = cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow('frame', frame)
        cv.imshow('mask', mask)
        cv.imshow('res', res)
        if cv.waitKey(100) == ord('q'):
            break

    cv.destroyAllWindows()


if __name__ == '__main__':
    # 查找hsv值
    green = np.uint8([[[255, 0, 0]]])
    hsv = cv.cvtColor(green, cv.COLOR_BGR2HSV)
    print(hsv)
    # [[[120 255 255]]]
    # 色调范围是[0, 179]，饱和度范围是[0, 255]，值范围是[0, 255]
    # get_hsv()、

