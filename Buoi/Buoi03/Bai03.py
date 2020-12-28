import sys
import numpy as np
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

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

        self.draw21Stars(painter)

    def drawStar(self, painter, P, kc):
        P.setY(P.y() - kc/2)
        Q = self.dichuyen(P, kc, 72)
        painter.drawLine(P, Q)

        P = Q
        Q = self.dichuyen(P, kc, -72-72)
        painter.drawLine(P, Q)

        P = Q
        Q = self.dichuyen(P, kc, 0)
        painter.drawLine(P, Q)

        P = Q
        Q = self.dichuyen(P, kc, 72+72)
        painter.drawLine(P, Q)

        P = Q
        Q = self.dichuyen(P, kc, -72)
        painter.drawLine(P, Q)

    def draw21Stars(self, painter):
        x = self.width()/2
        y = self.height()/2
        P = QPointF(x, y)
        painter.setPen(QPen(Qt.black, 2))
        self.drawStar(painter, P, 200)
        painter.setPen(QPen(Qt.black, 1))

        P = QPointF(x, y)
        for i in range(10):
            Q = self.dichuyen(P, 150, i*36)
            self.drawStar(painter, Q, 20)

        P = QPointF(x, y)
        for i in range(10):
            Q = self.dichuyen(P, 240, i*36)
            self.drawStar(painter, Q, 50)

    def dichuyen(self, p, kc, huong):
        pnew = QPointF(p.x() + kc*np.cos(np.pi*huong/180),
                       p.y() + kc*np.sin(np.pi*huong/180))
        return pnew


if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
