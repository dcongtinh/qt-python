from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys

name = 'Ngàn sao'


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Buoi02 - Bai02")
        self.setGeometry(300, 150, 800, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        self.drawNganSao(painter)

    def drawNganSao(self, painter):
        for i in range(1000):
            painter.setPen(Qt.NoPen)
            painter.setBrush(
                QColor(np.random.randint(255), np.random.randint(255), np.random.randint(255)))
            painter.drawEllipse(np.random.randint(
                1000), np.random.randint(1000), 3, 3)


if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
