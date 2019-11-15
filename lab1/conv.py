from PIL import Image
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import math
import numpy as np
class qtwindow(QWidget):
    def __init__(self, parent=None):
        self.fname=""
        super(qtwindow, self).__init__(parent)
        self.resize(500,400)
        self.move(500,300)
        self.setWindowTitle("test")
        layout = QVBoxLayout()

        self.btn1 = QPushButton()
        self.btn1.setText("打开照片")
        self.btn1.clicked.connect(self.loadFile)
        layout.addWidget(self.btn1)

        self.label1 = QLabel()
        layout.addWidget(self.label1)

        hbox = QHBoxLayout()
        self.btn2 = QPushButton()
        self.btn2.setText("prewwit")
        self.btn2.clicked.connect(self.prewwit)
        self.btn2.resize(20,50)
        hbox.addWidget(self.btn2)

        self.btn3 = QPushButton()
        self.btn3.setText("robert")
        self.btn3.clicked.connect(self.robert)
        hbox.addWidget(self.btn3)

        self.btn4 = QPushButton()
        self.btn4.setText("sobel")
        self.btn4.clicked.connect(self.sobel)
        hbox.addWidget(self.btn4)
        layout.addLayout(hbox)

        hbox1 = QHBoxLayout()
        self.btn5 = QPushButton()
        self.btn5.setText("mean")
        self.btn5.clicked.connect(self.mean)
        hbox1.addWidget(self.btn5)

        self.btn6 = QPushButton()
        self.btn6.setText("median")
        self.btn6.clicked.connect(self.median)
        hbox1.addWidget(self.btn6)

        self.btn7 = QPushButton()
        self.btn7.setText("gauss")
        self.btn7.clicked.connect(self.gauss)
        hbox1.addWidget(self.btn7)


        layout.addLayout(hbox1)

        self.input=QLineEdit()
        self.input.setText("kernel")
        layout.addWidget(self.input)

        self.input1 = QLineEdit()
        self.input1.setText("sigma1")
        layout.addWidget(self.input1)

        self.input2 = QLineEdit()
        self.input2.setText("sigma2")
        layout.addWidget(self.input2)

        self.label2 = QLabel()
        layout.addWidget(self.label2)

        self.setWindowTitle("test")
        self.setLayout(layout)

    def loadFile(self):
        print("load--file")
        self.fname, _ = QFileDialog.getOpenFileName(self, '选择图片', 'c:\\', 'Image files(*.jpg *.gif *.png)')
        print(self.fname)
        self.label1.setPixmap(QPixmap(self.fname).scaled(400,300,Qt.KeepAspectRatio))
    def prewwit(self):
        conv(self.fname,"prewwit")
        self.label2.setPixmap(QPixmap("tmp.jpg").scaled(400,300,Qt.KeepAspectRatio))
    def robert(self):
        conv(self.fname,"robert")
        self.label2.setPixmap(QPixmap("tmp.jpg").scaled(400,300,Qt.KeepAspectRatio))
    def sobel(self):
        conv(self.fname,"sobel")
        self.label2.setPixmap(QPixmap("tmp.jpg").scaled(400,300,Qt.KeepAspectRatio))
    def mean(self):
        mean(self.fname,int(self.input.text()))
        self.label2.setPixmap(QPixmap("tmp.jpg").scaled(400,300,Qt.KeepAspectRatio))
    def median(self):
        median(self.fname,int(self.input.text()))
        self.label2.setPixmap(QPixmap("tmp.jpg").scaled(400, 300, Qt.KeepAspectRatio))
    def gauss(self):
        gaussian(self.fname,int(self.input.text()),float(self.input1.text()),float(self.input2.text()))
        self.label2.setPixmap(QPixmap("tmp.jpg").scaled(400, 300, Qt.KeepAspectRatio))

def conv(filepath,method):
    threshold=64
    if method=="sobel":
        filter=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
        filter1=np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
        kernel=3
    if method=="robert":
        filter=np.array([[1,0],[0,-1]])
        filter1=np.array([[0,1],[-1,0]])
        kernel=2
    if method=="prewwit":
        filter = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        filter1 = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
        kernel = 3
    im=Image.open(filepath).convert('L')
    data=np.array(im)

    width=data.shape[0]
    height=data.shape[1]
    newdata=np.zeros((width+kernel-1,height+kernel-1))
    newim=np.zeros(data.shape)
    if kernel>2:
        newdata[int(kernel/2):-1*(int(kernel/2)+kernel%2-1),int(kernel/2):-1*(int(kernel/2)+kernel%2-1)]=data
    else:
        newdata[1: , 1:] = data
    for i in range(width):
        for j in range(height):
            tmp=(np.sum(newdata[i:i+kernel,j:j+kernel]*filter)+np.sum(newdata[i:i+kernel,j:j+kernel]*filter1))/2
            print(tmp)
            if(tmp>threshold):
                newim[i,j]=255
            else:
                newim[i, j] = 0
    Image.fromarray(newim.astype('uint8')).save("tmp.jpg")
    print(newdata.shape)

def mean(filepath,kernel):

    im=Image.open(filepath)
    data=np.array(im)

    width=data.shape[0]
    height=data.shape[1]
    newdata=np.zeros((width+kernel-1,height+kernel-1,3))
    newim=np.zeros(data.shape)
    if kernel>2:
        newdata[int(kernel/2):-1*(int(kernel/2)+kernel%2-1),int(kernel/2):-1*(int(kernel/2)+kernel%2-1),:]=data
    else:
        newdata[1: , 1:,:] = data
    for i in range(width):
        for j in range(height):
            newim[i,j,:]=np.mean(newdata[i:i+kernel,j:j+kernel,:],axis=(0,1))
    Image.fromarray(newim.astype('uint8')).save("tmp.jpg")
    print(newdata.shape)
def median(filepath,kernel):
    im = Image.open(filepath)
    data = np.array(im)

    width = data.shape[0]
    height = data.shape[1]
    newdata = np.zeros((width + kernel - 1, height + kernel - 1, 3))
    newim = np.zeros(data.shape)
    if kernel > 2:
        newdata[int(kernel / 2):-1 * (int(kernel / 2) + kernel % 2 - 1),
        int(kernel / 2):-1 * (int(kernel / 2) + kernel % 2 - 1), :] = data
    else:
        newdata[1:, 1:, :] = data
    for i in range(width):
        for j in range(height):
            newim[i, j, :] = np.median(newdata[i:i + kernel, j:j + kernel, :], axis=(0, 1))
    Image.fromarray(newim.astype('uint8')).save("tmp.jpg")
    print(newdata.shape)
def gaus2d(x,y,sigma1,sigma2):
    return math.exp(-1*(x*x/2/sigma1/sigma1+y*y/2/sigma2/sigma2))/2/math.pi/sigma1/sigma2
def gaussian(filepath,kernel,sigma1,sigma2):
    im = Image.open(filepath)
    data = np.array(im)
    filter=np.zeros((kernel,kernel,3))
    mid=(kernel-1)/2
    for i in range(kernel):
        for j in range(kernel):
            filter[i,j,:]=gaus2d(i-mid,j-mid,sigma1,sigma2)
    sum=np.sum(filter)/3

    filter=filter/sum
    print(filter)
    width = data.shape[0]
    height = data.shape[1]
    newdata = np.zeros((width + kernel - 1, height + kernel - 1, 3))
    newim = np.zeros(data.shape)
    if kernel > 2:
        newdata[int(kernel / 2):-1 * (int(kernel / 2) + kernel % 2 - 1),int(kernel / 2):-1 * (int(kernel / 2) + kernel % 2 - 1), :] = data
    else:
        newdata[1:, 1:, :] = data
    for i in range(width):
        for j in range(height):
            newim[i, j, :] =np.sum(newdata[i:i + kernel, j:j + kernel, :]*filter,axis=(0,1))
    Image.fromarray(newim.astype('uint8')).save("tmp.jpg")
    print(newdata.shape)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w=qtwindow()
    w.show()
    sys.exit(app.exec_())



