from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("This is a title")
        self.setGeometry(300, 150, 800, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        self.drawSomething(painter)

    def drawSomething(self, painter):
        # code here
        painter.drawLine(0, 0, 100, 100)
        pass


if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
