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
        self.spritesheet = QPixmap("./Assets/Megaman.png")
        self.w_img = self.spritesheet.width()/10
        self.h_img = self.spritesheet.height()
        self.delta = 10
        self.frameIndex = 0
        

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        self.drawMegaman(painter)

    def drawMegaman(self, painter):
        # Tạo một cửa sổ có tọa độ và kích thước phù hơp vói ảnh nhỏ
        displayWindow = QRect(self.w_img*self.frameIndex, 0, self.w_img, self.h_img)
        position = QRect(self.position, self.height() / 2 - 100, self.w_img*3, self.h_img*3)
        painter.drawPixmap(position, self.spritesheet, displayWindow)

    def handleTimer(self):
        if self.position > self.width() + self.w_img:
            self.position = - self.w_img - self.delta * 2
        self.position += self.delta
        # 10 frames
        self.frameIndex = (self.frameIndex + 1) % 10
        self.repaint()


if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
