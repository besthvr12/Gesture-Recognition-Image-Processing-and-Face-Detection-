

import cv2

body_cascade = cv2.CascadeClassifier('haarcascade_lowerbody.xml') # load the cascade for the lowerface.


def find(gray, lframe): # We create a function that takes as input the image in black and white (gray) and the original image (frame), and that will return the same image with the detector rectangles. 
    lowerbody = body_cascade.detectMultiScale(gray, 1.08, 3) # the detectMultiScale method from the face cascade to locate one or several faces in the image.Here 1.08 is the size of the image we are reducing.(1.08 and 3 are the good combination for lowerbody)
    for (lx, ly, lw, lh) in lowerbody: # For each detected lowerbody:
        cv2.rectangle(lframe, (lx, ly), (lx+lw, ly+lh), (234, 25, 0), 2)
        
    return lframe # We return the image with the detector rectangles.# We paint a rectangle around the lowerbody.
    # We return the image with the detector rectangles.If the legs are spread then it will show rectangle on both the leg.But when they are closed enough then it will show rectangle on all lower body.

video_capture = cv2.VideoCapture(0) # To turn on the webcam.

while True: # We repeat infinitely (until break)
    _, lframe = video_capture.read() # We get the last frame.
    gray = cv2.cvtColor(lframe, cv2.COLOR_BGR2GRAY) # Some colour transformations.(Converting real image to gray scale)
    canvas = find(gray, lframe) # The output of our detect function.(We are giving gray and lframe as arguments )
    cv2.imshow('Video', canvas) # To display the outputs.(
    if cv2.waitKey(1) & 0xFF == ord('s'): # To stop the loop press s
        break # To stop the loop.

video_capture.release() # To turn the webcam off.
cv2.destroyAllWindows() # To destroy all the windows inside which the images were displayed.
