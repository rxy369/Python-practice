import numpy
import cv2
# reads in an image from the local space and displays it
img = cv2.imread('test.jpg')
# show image
cv2.imshow('image', img)
# wait for key to be pressed before closing all windows
cv2.waitKey(0)
cv2.destroyAllWindows()