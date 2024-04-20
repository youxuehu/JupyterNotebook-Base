# -*- coding:utf-8 -*-
import cv2

image = cv2.imread("./image/1.png", 0)
print(image.shape)

print(type(image))
