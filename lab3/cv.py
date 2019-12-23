import cv2
import numpy as np
im=cv2.imread("../IMG_20191220_201655.jpg")
'''
x=cv2.Sobel(im,cv2.CV_8U,0,1)
y=cv2.Sobel(im,cv2.CV_8U,1,0)
cv2.convertScaleAbs(x,x)
cv2.convertScaleAbs(y,y)
im=cv2.addWeighted(x,0.5,y,0.5,0)
'''
cv2.blur(im,(3,3),im)
cv2.Laplacian(im,cv2.CV_8U,im,ksize=3)
'''
kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
cv2.morphologyEx(im,cv2.MORPH_OPEN,kernel,im)
'''
ret,im=cv2.threshold(im,50,255,cv2.THRESH_BINARY)
cv2.namedWindow("img",0)
cv2.resizeWindow("img",1024,768)
cv2.imshow("img",im)
cv2.waitKey()
cv2.destroyAllWindows()