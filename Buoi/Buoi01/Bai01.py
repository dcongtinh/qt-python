import sys
import numpy as np
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Config tên này để đổi tên trên menu
name = 'Hình vuông nội tiếp hình tròn'

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

        self.drawCircle(painter)
        self.drawSquare(painter)
        self.drawLines(painter)

    def drawCircle(self, painter):
        pen = QPen()
        pen.setWidth(3)
        painter.setPen(pen)
        center = QPoint(self.width()/2, self.height()/2)
        Rx = Ry = 150
        painter.drawEllipse(center, Rx, Ry)

    def drawSquare(self, painter):
        pen = QPen()
        pen.setWidth(3)
        painter.setPen(pen)
        d = np.sqrt((150*150)/2)
        painter.drawRect(self.width()/2-d, self.height()/2-d, 2*d, 2*d)

    def drawLines(self, painter):
        pen = QPen()
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawLine(self.width()/2 - 200, self.height()/2,
                         self.width()/2 + 200, self.height()/2)
        painter.drawLine(self.width()/2, self.height()/2 - 200,
                         self.width()/2, self.height()/2 + 200)


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
