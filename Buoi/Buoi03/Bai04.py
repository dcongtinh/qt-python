import sys
import numpy as np
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from math import sqrt, tan

name = 'Bông Tuyết'


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Buoi03 - Bai04")
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
        # move to P
        self.currentPosition = P

        # k parts
        for _ in range(0, k):
            self.xoay(-30)
            self.dichuyen(painter, x1, drawLine=False)
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
            self.xoay(90)
            self.dichuyen(painter, l/5-l/(40*sqrt(3)))
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
            self.dichuyen(painter, x1, drawLine=False)

            self.xoay(150)
            self.xoay(360/k)

    def drawChumBongTuyet(self, painter):
        x = self.width()/2
        y = self.height()/2
        p = QPoint(x, y)

        # recompute for responsiveness
        L = 0.5 * min(self.width(), self.height())
        self.drawBongTuyet(painter, p, L, 6)

    def dichuyen(self, painter, kc, drawLine=True):
        p = self.currentPosition
        pnew = QPointF(
            p.x() + kc*np.cos(3.14*self.angle/180),
            p.y() + kc*np.sin(3.14*self.angle/180)
        )
        if drawLine:
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
