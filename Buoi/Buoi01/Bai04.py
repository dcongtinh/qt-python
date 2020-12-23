from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys

name = 'Bàn cờ'


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Buoi01 - Bai04")
        self.setGeometry(300, 150, 800, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        self.drawBoard(painter)

    def drawBoard(self, painter):
        x = self.width()/2 - 200
        y = self.height()/2 - 200
        pen = QPen()
        pen.setWidth(1)
        painter.setPen((pen))
        for i in range(8):
            for j in range(8):
                if ((i % 2) ^ (j % 2)):
                    painter.setBrush(Qt.black)
                else:
                    painter.setBrush(Qt.white)
                painter.drawRect(x + j*50, y + i*50, 50, 50)


if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
