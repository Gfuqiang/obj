import sys
import numpy as np

import cv2

import matplotlib.pyplot as plt
from matplotlib.image import imread


def main():
    img = cv2.imread('images/hmbb.jpeg')
    # print(img[100, 90])
    # print(f"shape: {img.shape}")
    img[0, 0] = [255, 255, 255]
    if img is None:
        sys.exit("Could not read the image.")
    cv2.imshow('show', img)

    cv2.waitKey(5000)


def nu_to_img():
    img = np.zeros((3, 3), dtype=np.unit8)
    cv2.imshow('show', img)
    cv2.waitKey(5000)


def get_pic_property():
    img = cv2.imread('images/hmbb.jpeg')
    print(f"shape: {img.shape}")
    print(f"size: {img.size}")
    print(f"type: {img.dtype}")
    print(f"item: {img.item(100, 100, 1)}")
    red = img[200:500, 330:575]
    # print(f"rds: {red}")
    img[0:300, 115:360] = red
    # cv2.imshow('show', img)
    # cv2.waitKey(5000)
    # img = imread('images/hmbb.jpeg')  # 读入图片，imread函数里是需要显示的图片的地址，相对地址和绝对地址都可以
    plt.imshow(img)  # 把图片传给imshow函数
    #
    plt.show()  # 显示图片


if __name__ == '__main__':
    get_pic_property()