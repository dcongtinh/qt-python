from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys

name = '21 Stars'


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Buoi03 - Bai03")
        self.setGeometry(300, 150, 900, 800)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        self.drawChumBongTuyet(painter)

    def drawCombine(self, painter, P, Q, kc, angle):
        P = Q
        Q = self.dichuyen(P, kc, angle)
        painter.drawLine(P, Q)

    def drawBongTuyet(self, painter, P, l, k):
        painter.drawEllipse(P, 1, 1)
        x3 = l*np.sqrt(2)/80.
        x1 = x3/np.sin(np.pi*30/180)
        x2 = x3*np.tan(np.pi*60/180)

        for t in [1]:  # 1: nhánh trên, -1: nhánh dưới
            Q = self.dichuyen(painter, P, x1, -30*t + k)
            y = Q.y()
            Q = self.dichuyen(painter, Q, l*4/10, 0*t + k)
            w = (l - x2 - 8*l/10 - x3)/2
            painter.drawLine(Q, self.dichuyen(painter, Q, w, 0))
            Q = self.dichuyen(painter, Q, l*3/10, -60*t + k)
            Q = self.dichuyen(painter, Q, l/40, 30*t + k)
            Q = self.dichuyen(painter, Q, 3*l/10 -
                              np.sqrt(w*w - (l*l/1600)), 120*t + k)  # Pytago tính cạch góc vuông
            Q = self.dichuyen(painter, Q, l*2/10, 0*t + k)
            Q = self.dichuyen(painter, Q, l*2/10, -60*t + k)
            Q = self.dichuyen(painter, Q, l/40, 30*t + k)
            Q = self.dichuyen(painter, Q, 2*l/10 -
                              np.sqrt(w*w - (l*l)/1600), 120*t + k)  # Pytago tính cạch góc vuông
            Q = self.dichuyen(painter, Q, l*2/10, 0*t + k)
            Q = self.dichuyen(painter, Q, l/40, 45*t + k)

    def drawChumBongTuyet(self, painter):
        x = self.width()/2
        y = self.height()/2
        p = QPoint(x, y)
        self.drawBongTuyet(painter, p, 400, 0)

    def dist(self, p, q):
        return np.sqrt((p.x() - q.x())**2 + (p.y() - q.y())**2)

    def dichuyen(self, painter, p, kc, huong):
        pnew = QPointF()
        pnew.setX(p.x() + kc*np.cos(np.pi*huong/180))
        pnew.setY(p.y() + kc*np.sin(np.pi*huong/180))
        painter.drawLine(p, pnew)
        return pnew

    def doixungX(self, p, y):
        pnew = QPoint()
        pnew.setX(p.x())
        pnew.setY(2*y - p.y())

        return pnew


if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
