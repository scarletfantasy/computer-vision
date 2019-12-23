import cv2
import numpy as np
img=cv2.imread("../IMG_20191220_201655.jpg")

drawing=np.zeros(img.shape)
drawing1=np.zeros(img.shape)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray=cv2.blur(gray,(7,7))
edges = cv2.Canny(gray, 0, 25)

kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
cv2.morphologyEx(edges,cv2.MORPH_DILATE,kernel,edges)

cv2.namedWindow("img",0)
cv2.resizeWindow("img",1024,768)
cv2.imshow("img",edges)



cv2.waitKey()
cv2.destroyAllWindows()

