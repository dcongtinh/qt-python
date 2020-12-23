from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys
from math import sqrt, cos, tan

name = 'Bông Tuyết'

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Buoi03 - Bai03")
        self.setGeometry(300, 150, 900, 800)
        self.angle = 0
        self.currentPosition = 0

    def paintEvent(self, event):
        self.angle = 0
        self.currentPosition = 0
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        self.drawChumBongTuyet(painter)

    def drawBongTuyet(self, painter, P, l, k):
        x3 = l*np.sqrt(2)/80.
        x1 = x3/np.sin(np.pi*30/180)
        x2 = x3*np.tan(np.pi*60/180)
        w = (l - x2 - 8*l/10 - x3)/2
        # move to P
        self.currentPosition = P

        # k parts
        for _ in range(0, k):
            self.xoay(-30)
            self.dichuyen(painter, x1)
            self.xoay(30)
            self.dichuyen(painter, l*4/10)
            self.xoay(-60)
            self.dichuyen(painter, l*3/10)
            self.xoay(90)
            self.dichuyen(painter, l/40)
            self.xoay(90)
            self.dichuyen(painter, l*3/10-l/(40*tan(60*np.pi/180)))
            self.xoay(-120)
            self.dichuyen(painter, l/5)
            self.xoay(-60)
            self.dichuyen(painter, l/5)
            self.xoay(90)
            self.dichuyen(painter, l/40)
            # painter.drawLine(self.currentPosition, QPointF(self.currentPosition.x(), self.currentPosition.y()+500)) # debug
            self.xoay(90)
            self.dichuyen(painter, l/5-l/(40*sqrt(3))) # sqrt(3) = tan(60*np.pi/180)
            self.xoay(-120)
            self.dichuyen(painter, l/5)

            # draw top
            self.xoay(45)
            self.dichuyen(painter, l/40)
            self.xoay(90)
            self.dichuyen(painter, l/40)

            # # draw symmetry shape
            self.xoay(45)
            self.dichuyen(painter, l/5)
            self.xoay(-120)
            self.dichuyen(painter, l/5-l/(40*sqrt(3)))
            self.xoay(90)
            self.dichuyen(painter, l/40)
            self.xoay(90)
            self.dichuyen(painter, l/5)
            self.xoay(-60)
            self.dichuyen(painter, l/5)
            self.xoay(-120)
            self.dichuyen(painter, l*3/10-l/(40*tan(60*np.pi/180)))
            self.xoay(90)
            self.dichuyen(painter, l/40)
            self.xoay(90)
            self.dichuyen(painter, l*3/10)
            self.xoay(-60)
            self.dichuyen(painter, l*2/5)
            self.xoay(30)
            self.dichuyen(painter, x1)

            self.xoay(150)
            self.xoay(360/k)

    def drawChumBongTuyet(self, painter):
        x = self.width()/2
        y = self.height()/2
        p = QPoint(x, y)
        
        # recompute for responsiveness
        L = 0.5 * min(self.width(), self.height())
        self.drawBongTuyet(painter, p, L, 6)

    def dist(self, p, q):
        return np.sqrt((p.x() - q.x())**2 + (p.y() - q.y())**2)

    def dichuyen(self, painter, kc):
        p = self.currentPosition
        pnew = QPointF(
            p.x() + kc*np.cos(3.14*self.angle/180),
            p.y() + kc*np.sin(3.14*self.angle/180)
        )
        painter.drawLine(p, pnew)
        self.currentPosition = pnew

    def xoay(self, alpha):
        self.angle += alpha

if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)
    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
