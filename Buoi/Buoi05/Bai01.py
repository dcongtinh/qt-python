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
        self.img = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        self.drawMegaman(painter)

    def drawMegaman(self, painter):
        spritesheet = QPixmap("./Assets/Megaman.png")
        w_img = spritesheet.width()/10
        h_img = spritesheet.height()

        r = 10
        # Tạo một cửa sổ có tọa độ và kích thước phù hơp vói ảnh nhỏ
        displayWindow = QRect(w_img*self.img, 0, w_img, h_img)

        position = QRect(self.position * r, self.height() /
                         2 - 100, w_img*3, h_img*3)
        painter.drawPixmap(position, spritesheet, displayWindow)

    def handleTimer(self):
        if self.position < self.width()/2:
            self.position += 1
        # 10 frames
        self.img = (self.img + 1) % 10
        self.repaint()


if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
