from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys

name = 'MultiEllipse'


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Buoi02 - Bai07")
        self.setGeometry(400, 100, 800, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        self.drawMultiEllipse(painter)

    def xoay(self, p, angle):
        angle = angle * np.pi / 180
        return QPoint(
            int(p.x() * np.cos(angle) - p.y() * np.sin(angle)),
            int(p.x() * np.sin(angle) + p.y() * np.cos(angle))
        )

    def drawMultiEllipse(self, painter):
        x = self.width()/2
        y = self.height()/2
        rx = 50
        ry = 150
        p = QPoint(x, y)
        angle = 6
        painter.rotate(angle)
        for i in range(int(180/angle)):
            painter.rotate(angle * i)
            q = self.xoay(p, -angle * i)
            painter.drawEllipse(q, rx, ry)
            painter.rotate(-angle * i)


if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
