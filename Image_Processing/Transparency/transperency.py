import cv2
import numpy as np
color=cv2.imread('photo.jpg')
cv2.imshow('Original',color)
cv2.waitKey()
gray=cv2.cvtColor(color,cv2.COLOR_BGR2GRAY)
#It is better to split like that then split method:
b=color[:,:,0]
g=color[:,:,1]
r=color[:,:,2]
#Here we are adding an extra green channel to add transperency in our image,we are making non-green part of the image transperent.
rgba=cv2.merge((b,g,r,g))
#Now we will use .png to save becaue .jpeg does not support image transperency if we add .jpeg it will make our image again of 3-dimensional.
cv2.imwrite('rgba.png',rgba)