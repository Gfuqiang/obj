import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./images/hmbb.jpeg', 0)
ret, th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

th6 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4)
th7 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 6)

titles = ['BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV', 'MEAN_C', 'GAUSSIAN_C']
imgs = [th, th2, th3, th4, th5, th6, th7]

for i, img in enumerate(imgs):
    # plt.subplot(4, 2, i + 1)
    plt.imshow(th, cmap='gray')
    plt.title(titles[i])
    plt.show()