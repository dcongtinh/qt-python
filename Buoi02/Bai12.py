from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Buoi02 - Bai12")
        self.setGeometry(300, 150, 800, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        self.drawBreadman(painter)

    def drawBreadman(self, painter):
        painter.setBrush(QColor(Qt.blue))
        p = QPoint(115, 121)
        for i in range(10000):
            q = QPoint(40*(1 + 2*3) - p.y() + abs(p.x() - 40*3), p.x())
            painter.drawEllipse(q, 1, 1)
            p = q


if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
