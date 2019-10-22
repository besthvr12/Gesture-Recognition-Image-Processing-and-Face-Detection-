#Convex hull= It is the technique using we try to find the outer edges of any object
import cv2
import numpy as np
hand=cv2.imread('harsh.jpg',0)#Here we are using because we wanted  to convert our image into gray scale
#Now we find pixel value of the image using thresfolding.
#Here threshold function expect input in gray scale format and thresholding range and last input is type of thresholding.
ret, the=cv2.threshold(hand,70,255,cv2.THRESH_BINARY)
#We are using Thresh_binary because  we need background in black and foreground in white.
#Now we are using contour which helps us in finding outer area.
contours,_=cv2.findContours(the.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#Contours function return image,Number of contours,heirarchy.We only need contour
#RETR_TREE helps us in finding contour and CHAIN_APPROX_SIMPLE helps us in chaining them.
#Contour generally helps us in finding connected pixels.
#Now we are going to find Convex hull:
hull=[cv2.convexHull(c) for c in contours]
#here last argument is for colour.
final=cv2.drawContours(hand,hull,-1,(255,0,0))
cv2.imshow('Original Image',hand)
cv2.imshow('Thresh',the)
cv2.imshow('Convex Hull',final)
cv2.waitKey(0)
cv2.destroyAllWindows()
