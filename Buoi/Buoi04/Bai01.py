from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys
from functools import partial

name = 'Vẽ xe'

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.timer = QTimer()
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start(200)
        self.bmp = QPixmap("./Assets/bike.png")
        self.position = 0

    def paintEvent(self, event):
        self.position += 1
        painter = QPainter(self)
        painter.drawPixmap(self.position, 0, 300, 300, self.bmp)
        
    def handleTimer(self):
        self.repaint()

if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
