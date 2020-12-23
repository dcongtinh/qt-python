from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys
from functools import partial
from math import cos, sin

name = 'Chuyển động tròn có ngôi sao'


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
        painter.setRenderHint(QPainter.Antialiasing, True)
        self.paintCircle(painter, 200, 80, 30, True)

    def paintCircle(self, painter, trajectoryRadius, circleRadius, smallCircleRadius, renderCenter):
        self.angle += 5
        if (self.angle > 360):
            self.angle -= 360

        center = QPoint(self.width()/2, self.height()/2)
        r = trajectoryRadius
        p = QPointF(
            r*cos(self.angle/180.0*3.14)+center.x(),
            r*sin(self.angle/180.0*3.14)+center.y()
        )

        self.paintStar(painter, p, circleRadius)
        painter.drawEllipse(p, circleRadius, circleRadius)
        if renderCenter:
            painter.drawEllipse(center, smallCircleRadius, smallCircleRadius)
            self.paintStar(painter, center, smallCircleRadius)
            painter.drawLine(center, p)

    def paintStar(self, painter, center, height):
        a = -90
        v = []
        for i in range(5):
            tmp = QPointF(height * cos(a/180*3.14)+center.x(),
                          height * sin(a/180*3.14) + center.y())
            v.append(tmp)
            a += 360/5
        for i in range(5):
            for j in range(5):
                if ((i+1) % 5 != j and ((i-1+5) % 5 != j)):
                    painter.drawLine(v[i], v[j])

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
