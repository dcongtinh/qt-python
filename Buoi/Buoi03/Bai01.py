from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys

name = 'Polyspirals'


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Buoi03 - Bai01")
        self.setGeometry(300, 150, 900, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        self.drawPolyspirals(painter)

    def drawPolyspiral(self, painter, P, angle, incr):
        BD = P
        kc = 1
        huong = 0
        for i in range(100):
            BD = P
            P = self.dichuyen(P, kc, huong)
            painter.drawLine(BD, P)
            kc += incr
            huong += angle

    def drawPolyspirals(self, painter):
        P = QPointF(200, 150)
        self.drawPolyspiral(painter, P, 89.5, 2)

        P = self.dichuyen(P, 450, 0)
        self.drawPolyspiral(painter, P, -89.5, 2)

        Q = QPointF(100, 400)
        self.drawPolyspiral(painter, Q, -60, 1)

        Q = self.dichuyen(Q, 320, 0)
        self.drawPolyspiral(painter, Q, 144, 2.5)

        Q = self.dichuyen(Q, 320, 0)
        self.drawPolyspiral(painter, Q, -170, 2.5)

    def dichuyen(self, p, kc, huong):
        pnew = QPointF()
        pnew.setX(p.x() + kc*np.cos(np.pi*huong/180))
        pnew.setY(p.y() + kc*np.sin(np.pi*huong/180))
        return pnew


if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
