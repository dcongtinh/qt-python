from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys
from functools import partial
from math import cos, sin
from random import randint

name = 'Bầu trời sao lấp lánh'
class Star:
    def __init__(self, position, size, currentColor):
        self.position = position
        self.size = size 
        self.currentColor = currentColor
        self.targetColor = currentColor

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.timer = QTimer()
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start(10)
        self.maxStars = 50
        self.stars = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(Qt.black)
        painter.drawRect(QRect(0, 0, self.width(), self.height()))
        for i in range(len(self.stars)):
            pos = self.stars[i].position
            c = self.stars[i].currentColor
            size = self.stars[i].size
            self.drawStar(painter, pos, size, QColor(c, c, c))

    def drawStar(self, painter, center, h, color):
            real_h = h * 0.8
            edge = h - real_h
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(color))
            a = QPolygonF()
            a += QPointF(center.x() - edge, center.y() - edge)
            a += QPointF(center.x(), center.y() - h)
            a += QPointF(center.x() + edge, center.y() - edge)
            a += QPointF(center.x() + h, center.y())
            a += QPointF(center.x() + edge, center.y() + edge)
            a += QPointF(center.x(), center.y() + h)
            a += QPointF(center.x() - edge, center.y() + edge)
            a += QPointF(center.x() - h, center.y())
            painter.drawPolygon(a, 8)

    def handleTimer(self):
        stars = self.stars
        if not len(stars):
            # generate stars
            for i in range(self.maxStars):
                currentColor = randint(0, 255)
                size = randint(6, 20)
                pos = QPointF(randint(0, self.width()), randint(0, self.height()))
                self.stars.append(
                    Star(
                        position=pos,
                        size=size, 
                        currentColor=currentColor
                    )
                )
        # calculate target color of stars for next frame
        for i in range(len(stars)):
            if (stars[i].currentColor < stars[i].targetColor):
                stars[i].currentColor += 1
                if (stars[i].currentColor == stars[i].targetColor):
                    stars[i].targetColor = (0 if stars[i].targetColor == 255 else 255)
            else:
                stars[i].currentColor -= 1
                if (stars[i].currentColor == stars[i].targetColor):
                    stars[i].targetColor = (0 if stars[i].targetColor == 255 else 255)
        self.repaint()

if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)
    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
