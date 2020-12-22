from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys

name = 'Rosette'


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Buoi03 - Bai02")
        self.setGeometry(300, 150, 900, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        self.drawRosette(painter)

    def drawPoly(self, painter, P, n, d, full=False):
        BD = P
        for i in range(1, n+1):
            BD = P
            P = self.dichuyen(P, d, -i*360/n)
            painter.drawLine(BD, P)
            if full:
                Q = P
                for j in range(i+1, n+1):
                    Q = self.dichuyen(Q, d, -j*360/n)
                    painter.drawLine(BD, Q)

    def drawRosette(self, painter):
        P = QPointF(100, 200)
        self.drawPoly(painter, P, 3, 100)

        P = self.dichuyen(P, 120, 0)
        self.drawPoly(painter, P, 4, 90)

        P = self.dichuyen(P, 120, 0)
        self.drawPoly(painter, P, 5, 80)

        P = self.dichuyen(P, 140, 0)
        self.drawPoly(painter, P, 6, 70)

        P = self.dichuyen(P, 150, 0)
        self.drawPoly(painter, P, 12, 40)

        P = self.dichuyen(P, 170, 0)
        self.drawPoly(painter, P, 16, 35)

        Q = QPointF(200, 400)
        self.drawPoly(painter, Q, 5, 100, True)

        Q = self.dichuyen(Q, 230, 0)
        self.drawPoly(painter, Q, 11, 50, True)

        Q = self.dichuyen(Q, 250, 0)
        self.drawPoly(painter, Q, 20, 30, True)

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
