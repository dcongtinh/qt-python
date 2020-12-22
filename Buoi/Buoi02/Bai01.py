from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Buoi02 - Bai01")
        self.setGeometry(300, 200, 800, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        self.drawKhaoSat(painter)

    def drawKhaoSat(self, painter):
        painter.setPen(Qt.red)

        painter.drawLine(0, 0, 200, 0)
        painter.drawLine(0, 0, 0, 200)

        painter.drawRect(0, 0, 100, 50)

        painter.translate(200, 100)

        painter.rotate(30)
        painter.setPen(Qt.blue)
        painter.drawLine(0, 0, 200, 0)
        painter.drawLine(0, 0, 0, 200)
        painter.drawRect(0, 0, 100, 50)


if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
