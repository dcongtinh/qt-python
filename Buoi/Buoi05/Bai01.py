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

        # these vars are auto configured
        self.lineWidth = 0
        self.Xs = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        # draw lines
        for X in self.Xs:
            painter.drawLine(X-self.lineWidth//2, self.height()//2-50, X+self.lineWidth//2, self.height()//2-50)
            painter.drawLine(X-self.lineWidth//2-50, self.height()//2+50, X+self.lineWidth//2-50, self.height()//2+50)

        # draw megaman
        self.drawMegaman(painter)

    def drawMegaman(self, painter):
        # Tạo một cửa sổ có tọa độ và kích thước phù hơp vói ảnh nhỏ
        displayWindow = QRect(self.w_img*self.frameIndex, 0, self.w_img, self.h_img)
        position = QRect(self.position, self.height() / 2 - 100, self.w_img*3, self.h_img*3)
        painter.drawPixmap(position, self.spritesheet, displayWindow)

    def handleTimer(self):
        self.lineWidth = self.width() // 4
        if not self.Xs:
            start = self.width()//8
            for _ in range(6):
                self.Xs.append(start)
                start += self.lineWidth + 30
        if self.position >= self.width() // 2:
            for i in range(len(self.Xs)):
                self.Xs[i] -= self.delta
                if self.Xs[i] + self.lineWidth < 0:
                    self.Xs[i] = self.Xs[-1] + self.lineWidth + 20
                    self.Xs[i], self.Xs[-1] = self.Xs[-1], self.Xs[i]
        else:
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
