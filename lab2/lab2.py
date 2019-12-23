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
        self.resize(500,800)
        self.move(500,300)
        self.setWindowTitle("test")
        self.layout = QVBoxLayout()

        self.btn1 = QPushButton()
        self.btn1.setText("打开照片")
        self.btn1.clicked.connect(self.loadFile)
        self.layout.addWidget(self.btn1)

        self.btn1 = QPushButton()
        self.btn1.setText("打开mask")
        self.btn1.clicked.connect(self.loadFile1)
        self.layout.addWidget(self.btn1)

        self.hbox=QHBoxLayout()

        self.label1 = QLabel()
        self.hbox.addWidget(self.label1)

        self.label6 = QLabel()
        self.hbox.addWidget(self.label6)

        self.layout.addLayout(self.hbox)

        self.hbox3 = QHBoxLayout()

        self.label3=QLabel();
        self.label3.setText("kernelx")
        self.hbox3.addWidget(self.label3)

        self.input=QLineEdit()
        self.input.setText("3")
        self.hbox3.addWidget(self.input)

        self.label7 = QLabel();
        self.label3.setText("kernely")
        self.hbox3.addWidget(self.label7)

        self.input3=QLineEdit()
        self.input3.setText("3")
        self.hbox3.addWidget(self.input3)

        self.label4 = QLabel();
        self.label4.setText("x")
        self.hbox3.addWidget(self.label4)

        self.input1 = QLineEdit()
        self.input1.setText("1")
        self.hbox3.addWidget(self.input1)

        self.label5 = QLabel();
        self.label5.setText("y")
        self.hbox3.addWidget(self.label5)

        self.input2 = QLineEdit()
        self.input2.setText("1")
        self.hbox3.addWidget(self.input2)

        self.layout.addLayout(self.hbox3)

        self.btn2=QPushButton()
        self.btn2.setText("create filter")
        self.btn2.clicked.connect(self.createtable)
        self.layout.addWidget(self.btn2)

        self.label8 = QLabel();
        self.label8.setText("note:x,y is the core of se which starts from 0,the standard binary se should be like np.ones(3,3),the standard grayscale se should be like np.zeros(3,3)")
        self.layout.addWidget(self.label8)

        self.hbox1=QHBoxLayout()

        self.btn3 = QPushButton()
        self.btn3.setText("Conditional dilation ")
        self.btn3.clicked.connect(self.Conditionaldilation )

        self.hbox1.addWidget(self.btn3)
        '''
        self.btn4 = QPushButton()
        self.btn4.setText("conditional erosion")
        self.btn4.clicked.connect(self.Conditionalerosion)
        self.hbox1.addWidget(self.btn4)
        '''


        self.btn7 = QPushButton()
        self.btn7.setText("obr")
        self.btn7.clicked.connect(self.obr)
        self.hbox1.addWidget(self.btn7)

        self.btn8 = QPushButton()
        self.btn8.setText("cbr")
        self.btn8.clicked.connect(self.cbr)
        self.hbox1.addWidget(self.btn8)

        self.layout.addLayout(self.hbox1)

        self.hbox4 = QHBoxLayout()

        self.btn6 = QPushButton()
        self.btn6.setText("externaledgedetection")
        self.btn6.clicked.connect(self.edgedetection0)
        self.hbox4.addWidget(self.btn6)

        self.btn9 = QPushButton()
        self.btn9.setText("standardedgedetection")
        self.btn9.clicked.connect(self.edgedetection1)
        self.hbox4.addWidget(self.btn9)

        self.btn10 = QPushButton()
        self.btn10.setText("internaledgedetection")
        self.btn10.clicked.connect(self.edgedetection2)
        self.hbox4.addWidget(self.btn10)

        self.layout.addLayout(self.hbox4)

        self.hbox5 = QHBoxLayout()

        self.btn11 = QPushButton()
        self.btn11.setText("externalmorphgredient")
        self.btn11.clicked.connect(self.morphgredient0)
        self.hbox5.addWidget(self.btn11)

        self.btn12 = QPushButton()
        self.btn12.setText("standardmorphgredient")
        self.btn12.clicked.connect(self.morphgredient1)
        self.hbox5.addWidget(self.btn12)

        self.btn13 = QPushButton()
        self.btn13.setText("internalmorphgredient")
        self.btn13.clicked.connect(self.morphgredient2)
        self.hbox5.addWidget(self.btn13)

        self.layout.addLayout(self.hbox5)

        self.label2 = QLabel()
        self.layout.addWidget(self.label2)

        self.setWindowTitle("test")
        self.setLayout(self.layout)
    def Conditionaldilation (self):
        conditiondilation(self.fname,self.fname1,self.sfilter,self.kernelx,self.kernely)
        self.label2.setPixmap(QPixmap("tmp.png").scaled(400, 300, Qt.KeepAspectRatio))
    def Conditionalerosion (self):
        conditionerosion(self.fname,self.fname1,self.sfilter,self.kernelx,self.kernely)
        self.label2.setPixmap(QPixmap("tmp.png").scaled(400, 300, Qt.KeepAspectRatio))
    def grayscalereconstruction(self):
        grayscalereconstruction(self.fname,self.fname1,self.sfilter,self.kernelx,self.kernely)
        self.label2.setPixmap(QPixmap("tmp.png").scaled(400, 300, Qt.KeepAspectRatio))
    def morphgredient0(self):
        externalmorphgredient(self.fname,self.sfilter,self.kernelx,self.kernely)
        self.label2.setPixmap(QPixmap("tmp.png").scaled(400, 300, Qt.KeepAspectRatio))
    def morphgredient1(self):
        standardmorphgredient(self.fname,self.sfilter,self.kernelx,self.kernely)
        self.label2.setPixmap(QPixmap("tmp.png").scaled(400, 300, Qt.KeepAspectRatio))
    def morphgredient2(self):
        internalmorphgredient(self.fname,self.sfilter,self.kernelx,self.kernely)
        self.label2.setPixmap(QPixmap("tmp.png").scaled(400, 300, Qt.KeepAspectRatio))
    def edgedetection0(self):
        externaledgedetection(self.fname,self.sfilter,self.kernelx,self.kernely)
        self.label2.setPixmap(QPixmap("tmp.png").scaled(400, 300, Qt.KeepAspectRatio))
    def edgedetection1(self):
        standardedgedetection(self.fname,self.sfilter,self.kernelx,self.kernely)
        self.label2.setPixmap(QPixmap("tmp.png").scaled(400, 300, Qt.KeepAspectRatio))
    def edgedetection2(self):
        internaledgedetection(self.fname,self.sfilter,self.kernelx,self.kernely)
        self.label2.setPixmap(QPixmap("tmp.png").scaled(400, 300, Qt.KeepAspectRatio))
    def cbr(self):
        cbr(self.fname,self.sfilter,self.kernelx,self.kernely)
        self.label2.setPixmap(QPixmap("tmp.png").scaled(400, 300, Qt.KeepAspectRatio))

    def obr(self):
        obr(self.fname, self.sfilter, self.kernelx, self.kernely)
        self.label2.setPixmap(QPixmap("tmp.png").scaled(400, 300, Qt.KeepAspectRatio))
    def loadFile(self):
        print("load--file")
        self.fname, _ = QFileDialog.getOpenFileName(self, '选择图片', 'c:\\', 'Image files(*.png *.gif *.png)')
        print(self.fname)
        self.label1.setPixmap(QPixmap(self.fname).scaled(400,300,Qt.KeepAspectRatio))

    def loadFile1(self):
        print("load--file")
        self.fname1, _ = QFileDialog.getOpenFileName(self, '选择图片', 'c:\\', 'Image files(*.png *.gif *.png)')
        print(self.fname)
        self.label6.setPixmap(QPixmap(self.fname1).scaled(400, 300, Qt.KeepAspectRatio))
    def createtable(self):
        self.table = QTableWidget()
        self.table.setRowCount(int(self.input.text()))
        self.table.setColumnCount(int(self.input3.text()))

        self.layout.addWidget(self.table)
        self.btn2 = QPushButton()
        self.btn2.setText("save")
        self.btn2.clicked.connect(self.savefilter)
        self.layout.addWidget(self.btn2)
    def savefilter(self):
        self.kernelsizex=(int(self.input.text()))
        self.kernelsizey = (int(self.input3.text()))
        self.sfilter=np.zeros((self.kernelsizex,self.kernelsizey))
        for i in range(self.kernelsizex):
            for j in range(self.kernelsizey):
                self.sfilter[i][j]=int(self.table.item(i,j).text())
        self.kernelx=int(self.input1.text())
        self.kernely=int(self.input2.text())
        print("success")


def grayscaleeroisin(data,filter,kernelx,kernely):
    kernelsizex = filter.shape[0]
    kernelsizey = filter.shape[1]
    width = data.shape[0]
    height = data.shape[1]
    newdata=np.pad(data,((kernelx,kernelsizex-kernelx-1),(kernely,kernelsizey-kernely-1)),'constant',constant_values=(0,0))
    newim = np.zeros(data.shape)
    filter1 = filter
    for i in range(width):
        for j in range(height):
            newim[i][j]=np.min(newdata[i:i+filter1.shape[0],j:j+filter1.shape[1]]-filter1[:,:])
    return newim
def eroisin(data,filter,kernelx,kernely):
    kernelsizex = filter.shape[0]
    kernelsizey = filter.shape[1]
    width = data.shape[0]
    height = data.shape[1]
    newdata = np.pad(data, ((kernelx, kernelsizex - kernelx - 1), (kernely, kernelsizey - kernely - 1)), 'constant',
                     constant_values=(0, 0))
    newim = np.zeros(data.shape)
    filter1 = filter
    for i in range(width):
        for j in range(height):
            flag = True
            for m in range(filter1.shape[0]):
                for k in range(filter1.shape[1]):
                    if filter1[m][k] != 0 and newdata[i + m][j + k] ==0:
                        flag = False
            if flag:
                newim[i][j] = 255
            else:
                newim[i][j] = 0
    return newim
def grayscaledilation(data,filter,kernelx,kernely):
    kernelsizex = filter.shape[0]
    kernelsizey = filter.shape[1]
    width = data.shape[0]
    height = data.shape[1]
    newdata = np.pad(data, ((kernelx, kernelsizex - kernelx - 1), (kernely, kernelsizey - kernely - 1)), 'constant',
                     constant_values=(0, 0))
    newim = np.zeros(data.shape)

    filter1 = filter

    for i in range(width):
        for j in range(height):
            newim[i][j]=np.max(filter1[:,:]+newdata[i:i+filter1.shape[0],j:j+filter1.shape[1]])
    return newim
def dilation(data,filter,kernelx,kernely):
    kernelsizex = filter.shape[0]
    kernelsizey = filter.shape[1]
    width = data.shape[0]
    height = data.shape[1]
    newdata = np.pad(data, (( kernelsizex - kernelx - 1,kernelx), ( kernelsizey - kernely - 1,kernely)), 'constant',
                     constant_values=(0, 0))
    newim = np.zeros(data.shape)

    filter1 = np.rot90(filter)
    filter1=np.rot90(filter1)

    for i in range(width):
        for j in range(height):
            flag = False
            for m in range(filter1.shape[0]):
                for k in range(filter1.shape[1]):
                    if filter1[m][k] != 0 and newdata[i + m][j + k] ==255:
                        flag = True
            if flag:
                newim[i][j] = 255
            else:
                newim[i][j] = 0
    return newim

def openopt(data,filter,kernelx,kernely):
    erosion1=eroisin(data,filter,kernelx,kernely)
    dialation1=dilation(erosion1,filter,kernelx,kernely)

    return dialation1
def closeopt(data,filter,kernelx,kernely):
    dialation1=dilation(data,filter,kernelx,kernely)
    erosion1=dilation(dialation1,filter,kernelx,kernely)

    return erosion1
def grayscaleopenopt(data,filter,kernelx,kernely):
    erosion1=grayscaleeroisin(data,filter,kernelx,kernely)
    dialation1=grayscaledilation(erosion1,filter,kernelx,kernely)

    return dialation1
def grayscalecloseopt(data,filter,kernelx,kernely):
    dilation1 = grayscaledilation(data, filter, kernelx, kernely)
    eroisin1 = grayscaledilation(dilation1, filter, kernelx, kernely)
    return eroisin1
def conditiondilation(filepath,filepath1,filter,kernelx,kernely):
    im = Image.open(filepath).convert("L")
    im1=Image.open(filepath1).convert("L")

    v = np.array(im)
    m=openopt(v,filter,kernelx,kernely)
    mask = np.array(im1)
    for i in range(v.shape[0]):
        for j in range(v.shape[1]):
            if mask[i][j] != 0:
                mask[i][j] = 1
    filter1=np.ones((3,3))
    while True:
        t = m.copy()
        m = dilation(t, filter1,1,1)
        m = m * mask
        if np.equal(t, m).all():
            break


    Image.fromarray(m.astype('uint8')).save("tmp.png")
def conditionerosion(filepath,filepath1,filter,kernelx,kernely):
    im = Image.open(filepath).convert("L")
    im1=Image.open(filepath1).convert("L")

    v = np.array(im)
    m=closeopt(v,filter,kernelx,kernely)
    mask = np.array(im1)
    for i in range(v.shape[0]):
        for j in range(v.shape[1]):
            if mask[i][j] != 0:
                mask[i][j] = 255
    filter1=np.ones((3,3))
    while True:
        t = m.copy()
        m = eroisin(t, filter1,1,1)
        m = (m<mask)*mask+(m>=mask)*m
        if np.equal(t, m).all():
            break


    Image.fromarray(m.astype('uint8')).save("tmp.png")

def grayscalereconstruction(filepath,filepath1,filter,kernelx,kernely):
    im = Image.open(filepath).convert("L")
    im1 = Image.open(filepath1).convert("L")

    f = np.array(im)
    f=grayscaleopenopt(f,filter,kernelx,kernely)
    g = np.array(im1)
    while True:
        m=g.copy()
        g=grayscaledilation(g,filter,kernelx,kernely)
        g=(g>f)*f+(g<=f)*g
        if np.equal(g,m).all():
            break
    Image.fromarray(m.astype('uint8')).save("tmp.png")

def obr(filepath,filter,kernelx,kernely):
    im = Image.open(filepath).convert('L')
    data = np.array(im)
    openimage=grayscaleopenopt(data,filter,kernelx,kernely)
    filter1=np.zeros((3,3))
    g=openimage.copy()
    count=2
    while True:
        m=g.copy()
        g=grayscaledilation(g,filter1,1,1)
        g=(g>data)*data+(g <= data)*g
        if np.equal(g,m).all():
            break
    Image.fromarray(m.astype('uint8')).save("tmp.png")
def cbr(filepath,filter,kernelx,kernely):
    im = Image.open(filepath).convert('L')
    data = np.array(im)
    openimage=grayscalecloseopt(data,filter,kernelx,kernely)
    filter1=np.zeros((3,3))
    g=openimage.copy()
    while True:
        m=g.copy()
        g=grayscaleeroisin(g,filter1,1,1)
        g=(g<data)*data+(g>=data)*g
        if np.equal(g,m).all():
            break
    Image.fromarray(m.astype('uint8')).save("tmp.png")
def externalmorphgredient(filepath,filter,kernelx,kernely):
    im = Image.open(filepath).convert('L')
    data = np.array(im)

    outimage = grayscaledilation(data, filter,kernelx,kernely)

    inimage = grayscaleeroisin(data, filter,kernelx,kernely)
    m =( outimage - data)*0.5
    Image.fromarray(m.astype('uint8')).save("tmp.png")
def standardmorphgredient(filepath,filter,kernelx,kernely):
    im = Image.open(filepath).convert('L')
    data = np.array(im)

    outimage = grayscaledilation(data, filter,kernelx,kernely)

    inimage = grayscaleeroisin(data, filter,kernelx,kernely)
    m =( outimage - inimage)*0.5
    Image.fromarray(m.astype('uint8')).save("tmp.png")
def internalmorphgredient(filepath,filter,kernelx,kernely):
    im = Image.open(filepath).convert('L')
    data = np.array(im)

    outimage = grayscaledilation(data, filter,kernelx,kernely)

    inimage = grayscaleeroisin(data, filter,kernelx,kernely)
    m =( data - inimage)*0.5
    Image.fromarray(m.astype('uint8')).save("tmp.png")

def standardedgedetection(filepath,filter,kernelx,kernely):
    im = Image.open(filepath).convert('L')
    data=np.array(im)

    outimage=dilation(data,filter,kernelx,kernely)
    inimage=eroisin(data,filter,kernelx,kernely)
    m=outimage-inimage
    Image.fromarray(m.astype('uint8')).save("tmp.png")
def externaledgedetection(filepath,filter,kernelx,kernely):
    im = Image.open(filepath).convert('L')
    data=np.array(im)

    outimage=dilation(data,filter,kernelx,kernely)
    m=outimage-data
    Image.fromarray(m.astype('uint8')).save("tmp.png")

def internaledgedetection(filepath, filter, kernelx, kernely):

    im = Image.open(filepath).convert('L')
    data = np.array(im)

    inimage = eroisin(data, filter, kernelx, kernely)
    m = data - inimage
    Image.fromarray(m.astype('uint8')).save("tmp.png")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    w=qtwindow()
    w.show()
    sys.exit(app.exec_())
    '''
    edgedetection("C:\\Users\\97023\\Pictures\\tmp.png")
    '''
