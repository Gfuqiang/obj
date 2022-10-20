import numpy as np
import cv2 as cv

cap = cv.VideoCapture('./videos/6799_raw.MP4')
if not cap.isOpened():
    print('not open camera')
    exit(1)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't open frame")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(100) == ord('q'):
        break

# release capture
cap.release()
cv.destroyAllWindows()
