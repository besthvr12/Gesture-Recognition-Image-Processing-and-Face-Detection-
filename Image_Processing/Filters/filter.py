import cv2
import numpy as np
color=cv2.imread('new.jpg')
cv2.imwrite('Original.jpg',color)

#Now we are defining our gaussian blur.
#It will blur the image more in x-axis then in y-axis.
blur=cv2.GaussianBlur(color,(55,5),0)
cv2.imwrite('Gaussian_Blur.jpg',blur)

kernel= np.ones((5,5))
#We are defining dilation filter. 
dilate=cv2.dilate(color,kernel,iterations=1)
#We are defining erode filter.
erode=cv2.erode(color,kernel,iterations=1)
cv2.imwrite('Dilate.jpg',dilate)
cv2.imwrite('Erode.jpg',erode) 
cv2.waitKey()
cv2.destroyAllWindows()  