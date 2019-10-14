import cv2
import numpy as np
color=cv2.imread('photo.jpg')
cv2.imshow('Original',color)
cv2.waitKey()
gray=cv2.cvtColor(color,cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray.jpg",gray)
cv2.imshow('Grayscale',gray)
cv2.moveWindow('Grayscale',0,0)
print(color.shape)
height,width,channels=color.shape


#Now to split the image we are using:
b,g,r=cv2.split(color)
#We are creating a matrix:
rgb_split=np.empty([height,width*3,3],'uint8')
#It will now placed blue channel on the left side of the image.
rgb_split[:,0:width]=cv2.merge([b,b,b])
rgb_split[:,width:width*2]=cv2.merge([g,g,g])
rgb_split[:,width*2:width*3]=cv2.merge([r,r,r]) 
cv2.imwrite("rgb_split.jpg",rgb_split)
cv2.imshow("Channels",rgb_split)
cv2.moveWindow("Channels",0,height)
 
#Now we are adding hue transformation:
hsv=cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)
#We are use np here to make hsv come before rgb_split.
hsv_split=np.concatenate((h,s,v),axis=1)
cv2.imwrite("hsv_split.jpg",hsv_split)
cv2.imshow("Split HSV",hsv_split)
cv2.waitKey()
cv2.destroyAllWindows()
#Here 3 are the numbers of channels we are spliting in.
#uint8 is used for making our data in range between 0-255
  