import cv2
import numpy as np
img=cv2.imread("../IMG_20191220_193628.jpg")
img1=cv2.imread("../IMG_20191219_171731.jpg")
img2=cv2.imread("../IMG_20191220_195436.jpg")
drawing=np.zeros(img.shape)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
sift=cv2.xfeatures2d.SIFT_create()
kp, des = sift.detectAndCompute(gray,None)
kp1, des1 = sift.detectAndCompute(gray1,None)
kp2, des2 = sift.detectAndCompute(gray2,None)
bf=cv2.BFMatcher()
matches=bf.knnMatch(des1,des,k=2)
matches1=bf.knnMatch(des1,des2,k=2)
good=[]
good1=[]
for m,n in matches:
    if m.distance<0.6*n.distance:
        good.append([m])
for m,n in matches1:
    if m.distance<0.6*n.distance:
        good1.append([m])
print(good.__len__())
print(good1.__len__())
im=cv2.drawMatchesKnn(img1,kp1,img,kp,good,None,flags=2)
im1=cv2.drawMatchesKnn(img1,kp1,img2,kp2,good1,None,flags=2)
cv2.namedWindow("img1",0)
cv2.resizeWindow("img1",1024,768)
cv2.imshow("img1",im)
cv2.namedWindow("img2",0)
cv2.resizeWindow("img2",1024,768)
cv2.imshow("img2",im1)
cv2.waitKey()
cv2.destroyAllWindows()