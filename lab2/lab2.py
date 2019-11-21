from PIL import Image
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import math
import numpy as np
'''
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

        self.label3=QLabel();
        self.label3.setText("kernel")
        layout.addWidget(self.label3)

        self.input=QLineEdit()
        self.input.setText("3")
        layout.addWidget(self.input)

        self.label4 = QLabel();
        self.label4.setText("sigma1")
        layout.addWidget(self.label4)

        self.input1 = QLineEdit()
        self.input1.setText("1.0")
        layout.addWidget(self.input1)

        self.label5 = QLabel();
        self.label5.setText("sigma2")
        layout.addWidget(self.label5)

        self.input2 = QLineEdit()
        self.input2.setText("1.0")
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


'''
def eroisin(data,filter):
    kernel = filter.shape[0]
    width = data.shape[0]
    height = data.shape[1]
    newdata = np.zeros((width + kernel - 1, height + kernel - 1))
    newim = np.zeros(data.shape)
    if kernel > 2:
        newdata[int(kernel / 2):-1 * (int(kernel / 2) + kernel % 2 - 1),
        int(kernel / 2):-1 * (int(kernel / 2) + kernel % 2 - 1)] = data
    else:
        newdata[1:, 1:] = data
    filter1 = filter
    for i in range(width):
        for j in range(height):
            flag = True
            for m in range(3):
                for k in range(3):
                    if filter1[m][k] != 0 and newdata[i + m][j + k] == 0:
                        flag = False
            print(flag)
            if flag:
                newim[i][j] = 255
            else:
                newim[i][j] = 0
    return newim
def dilation(data,filter):
    kernel = filter.shape[0]
    width = data.shape[0]
    height = data.shape[1]
    newdata = np.zeros((width + kernel - 1, height + kernel - 1))
    newim = np.zeros(data.shape)
    if kernel > 2:
        newdata[int(kernel / 2):-1 * (int(kernel / 2) + kernel % 2 - 1),
        int(kernel / 2):-1 * (int(kernel / 2) + kernel % 2 - 1)] = data
    else:
        newdata[1:, 1:] = data
    filter1 = filter.T
    for i in range(width):
        for j in range(height):
            flag = False
            for m in range(3):
                for k in range(3):
                    if filter1[m][k] != 0 and newdata[i + m][j + k] ==255:
                        flag = True
            print(flag)
            if flag:
                newim[i][j] = 255
            else:
                newim[i][j] = 0
    return newim
def openopt(data,filter):
    erosion1=eroisin(data,filter)
    dialation1=dilation(erosion1,filter)
    return dialation1

def morphreconstruction(filepath):
    im = Image.open(filepath)
    filter=np.array([[1,1,1],[1,1,1],[1,1,1]])

    v = np.array(im)
    m=openopt(v,filter)
    mask = v.copy()
    for i in range(v.shape[0]):
        for j in range(v.shape[1]):
            if mask[i][j] != 0:
                mask[i][j] = 1
    while True:
        t = m.copy()
        m = dilation(t, filter)
        m = m * mask
        if np.equal(t, m).all():
            break


    Image.fromarray(m.astype('uint8')).save("tmp.jpg")

def grayscalereconstruction(filepath,filepath1):
    im = Image.open(filepath)
    filter = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

    f = np.array(im)
    im = Image.open(filepath1)
    g = np.array(im)
    while True:
        m=g.copy()
        g=dilation(g,filter)
        g=(g>f)*f+(g<=f)*g
        if np.equal(g,m).all():
            break


    Image.fromarray(m.astype('uint8')).save("tmp.jpg")
def morphgredient(filepath):
    im = Image.open(filepath)
    data = np.array(im)
    filter = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    outimage = dilation(data, filter)
    inimage = eroisin(data, filter)
    m =( outimage - inimage)*0.5
    Image.fromarray(m.astype('uint8')).save("tmp.jpg")
def edgedetection(filepath):
    im = Image.open(filepath)
    data=np.array(im)
    filter = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    outimage=dilation(data,filter)
    inimage=eroisin(data,filter)
    m=outimage-inimage
    Image.fromarray(m.astype('uint8')).save("tmp.jpg")

if __name__ == '__main__':
    '''
    app = QApplication(sys.argv)
    w=qtwindow()
    w.show()
    sys.exit(app.exec_())
    '''
    morphreconstruction("C:\\Users\\97023\\Pictures\\timg.jpg")


