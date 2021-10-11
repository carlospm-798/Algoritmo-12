#Paredes Márquez Carlos
#Ejercicio dos
#06 10 2021

import cv2

im = cv2.imread('im2.jpg')
hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

mask0 = cv2.inRange(hsv, (104,0,0), (124,255,255))
mask = mask0.copy()

cv2.floodFill(mask0, None, (80, 300), 255)

im2 = cv2.bitwise_not(mask0)
im3 = cv2.bitwise_or(im2, mask)

cv2.imshow('Primera imagen', im)
cv2.imshow('Mask', mask)
cv2.imshow('Flood', mask0)
cv2.imshow('Negacion mask', im2)
cv2.imshow('Imagen final', im3)
cv2.waitKey(0)