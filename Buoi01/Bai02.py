from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Buoi01 - Bai02")
        self.setGeometry(300, 150, 800, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        self.drawThaiCuc(painter)

    def drawThaiCuc(self, painter):
        x = self.width()/2
        y = self.height()/2
        Rx = Ry = 150

        O = QPoint(x, y)
        O1 = QPoint(x-Rx/2, y)
        O2 = QPoint(x+Rx/2, y)

        painter.drawEllipse(O, Rx, Ry)
        painter.drawEllipse(O1, 12, 12)
        painter.drawEllipse(O2, 12, 12)

        rectangle = QRectF(x-Rx/2-Rx/2, y-Ry/2, Rx, Ry)
        startAngle = 180 * 16
        spanAngle = 180 * 16
        painter.drawArc(rectangle, startAngle, spanAngle)

        rectangle2 = QRectF(x+Rx/2-Rx/2, y-Ry/2, Rx, Ry)
        startAngle = 0 * 16
        spanAngle = 180 * 16
        painter.drawArc(rectangle2, startAngle, spanAngle)


if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
