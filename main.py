#Paredes Márquez Carlos
#Algoritmo 12
#05 10 2021

import cv2
import numpy as np

im = cv2.imread('im.png')
im = np.zeros((400, 500), np.uint8)
im[200,:] = 100

cv2.floodFill(im, None, (80, 300), 255) #im, mask, (x,y), color
cv2.imshow('imagen', im)
cv2.waitKey(0)