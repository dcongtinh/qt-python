from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys
from functools import partial
from math import cos, sin

name = 'Hệ mặt trời'

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.timer = QTimer()
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start(50)
        self.position = 0
        self.angle = 0
        
        # load bitmaps and config angles
        self.sunBmp     = QPixmap("./Assets/sun.png")
        self.sunAngle = 0

        self.earthBmp   = QPixmap("./Assets/earth.png")
        self.earthAngle = 0

        self.moonBmp    = QPixmap("./Assets/moon.png")
        self.moonAngle = 0
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(Qt.black)
        painter.drawRect(0, 0, self.width(), self.height())
        self.paintSolar(painter, 240, 60)

    def paintSolar(self, painter, earthTrajectoryRadius, moonTrajectoryRadius):
        '''
        sun radius = 696340 km
        moon radius 1737 km
        earth radius 6371
        moon distance from earth 384400 km
        earth distance from sun: 150000000 km
        Period moon around earth: 29 days
        Period earth aroud sun: 365 days

        double sunRadius = 100.0;
        double earthRadius = 6371 / 696340.0 * sunRadius + 5, moonRadius = 1737.0 / 696340 * sunRadius + 5;
        earthTrajectoryRadius = sunRadius * 150000000.0 / 696340 ;
        moonTrajectoryRadius = sunRadius * 384400.0 / 1737;
        painter.fillRect(0, 0, width(), height(), Qt::black);
        '''

        # update earch angle
        self.earthAngle += 2
        if self.earthAngle > 360: 
            self.earthAngle -= 360
        
        # update moon angle
        self.moonAngle += 4
        if self.moonAngle > 360:
            self.moonAngle -= 360

        # draw sun
        center = QPoint(self.width()/2, self.height()/2)
        painter.drawPixmap(center.x()-50, center.y()-50, 100, 100, self.sunBmp)

        # draw earth
        earthCenter = QPoint(
            earthTrajectoryRadius * cos(self.earthAngle/180.0*3.14) + center.x(), 
            earthTrajectoryRadius * sin(self.earthAngle/180.0*3.14) + center.y()
        )
        painter.drawPixmap(earthCenter.x()-40, earthCenter.y()-40, 80, 80, self.earthBmp)

        # draw moon
        moonCenter = QPoint(
            moonTrajectoryRadius * cos(self.moonAngle/180.0*3.14) + earthCenter.x(), 
            moonTrajectoryRadius * sin(self.moonAngle/180.0*3.14) + earthCenter.y()
        )
        painter.drawPixmap(moonCenter.x()-10, moonCenter.y()-10, 20, 20, self.moonBmp)

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
