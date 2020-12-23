from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys

# Config tên này để đổi tên trên menu
name = 'Hàng rào'

# Class Window cần phải có


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Buoi01 - Bai01")
        self.setGeometry(300, 150, 800, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        self.drawFence(painter)

    def drawElement(self, painter, P, dx):
        P = self.dichuyen(P, dx, 0)
        Q = self.dichuyen(P, 25, 45)
        painter.drawLine(P, Q)
        P = Q
        Q = self.dichuyen(P, 200, 90)
        painter.drawLine(P, Q)

        P = Q
        Q = self.dichuyen(P, 35, -180)
        painter.drawLine(P, Q)

        P = Q
        Q = self.dichuyen(P, 200, -90)
        painter.drawLine(P, Q)

        P = Q
        Q = self.dichuyen(P, 25, -45)
        painter.drawLine(P, Q)

    def drawFence(self, painter):
        P = QPointF(200, 200)
        self.drawElement(painter, P, 0)
        d = 50
        for i in range(1, 11):
            self.drawElement(painter, P, i*d)

        painter.setBrush(QColor(236, 236, 236))
        painter.drawRect(150, 250, 12*d, 25)
        painter.drawRect(150, 350, 12*d, 25)

    def dichuyen(self, p, kc, huong):
        pnew = QPointF()
        pnew.setX(p.x() + kc*np.cos(np.pi*huong/180))
        pnew.setY(p.y() + kc*np.sin(np.pi*huong/180))
        return pnew


# Phần bên dưới nên dùng để chạy khi test
# Không được thực thi trong app.py
if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
