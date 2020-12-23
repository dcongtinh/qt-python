from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys
from functools import partial
from math import cos, sin

name = 'Chuyển động tròn'

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.timer = QTimer()
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start(50)
        self.position = 0
        self.angle = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        self.paintCircle(painter, 200, 80, 30, True)   

    def paintCircle(self, painter, trajectoryRadius, circleRadius, smallCircleRadius, renderCenter):
        self.angle += 5
        if (self.angle > 360):
            self.angle -=360

        center = QPoint(self.width()/2, self.height()/2)
        r = trajectoryRadius
        p = QPointF(
            r*cos(self.angle/180.0*3.14)+center.x(), 
            r*sin(self.angle/180.0*3.14)+center.y()
        )

        painter.drawEllipse(p, circleRadius, circleRadius)
        if renderCenter:
            painter.drawEllipse(center, smallCircleRadius, smallCircleRadius)
            painter.drawLine(center, p)

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
