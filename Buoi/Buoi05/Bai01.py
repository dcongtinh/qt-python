from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys
from functools import partial

name = 'Megan di chuyển'

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.timer = QTimer()
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start(100)
        self.position = 0

        self.megaman = QPixmap("./Assets/megaman.png")
        self.megamanIndex = 0
        self.megamanWidth = 33
        self.scale = 8

    def paintEvent(self, event):
        painter = QPainter(self)
        scale = self.scale
        src = QRect(self.megamanIndex * self.megamanWidth, 0, self.megamanWidth, self.megaman.height())
        dst = QRect(
            (self.width()-self.megamanWidth*scale)//2, (self.height()-self.megaman.height()*scale)//2,
            self.megamanWidth*scale, self.megaman.height()*scale
        )
        painter.drawPixmap(dst, self.megaman, src)
        
    def handleTimer(self):
        self.megamanIndex = (self.megamanIndex + 1) % (self.megaman.width()//self.megamanWidth)
        self.repaint()

if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
