from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys

# Config tên này để đổi tên trên menu
name = 'Bảng màu'

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

        self.drawColors(painter)

    def drawColors(self, painter):
        x, y, w, h = 60, 40, 15, 40
        painter.setPen(Qt.NoPen)

        # RGB color
        for i in range(1, 4):
            for j in range(0, 52):  # 255/5 + 1
                c = QColor((255-5*j)*(i == 1), (255-5*j)
                           * (i == 2), (255-5*j)*(i == 3))
                painter.setBrush(QBrush(c))
                painter.drawRect(x + j*w, y + 2*i*h, w, h)

        # Random color
        for j in range(0, 52):  # 255/5 + 1
            R = np.random.randint(255)
            G = np.random.randint(255)
            B = np.random.randint(255)
            c = QColor(R, G, B)
            painter.setBrush(QBrush(c))
            painter.drawRect(x + j*w, y + 2*4*h, w, h)


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
