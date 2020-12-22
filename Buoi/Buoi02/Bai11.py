from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys
import random 
import time 

name = 'Sierpinski Gasket'

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the geo for testing
        self.setGeometry(300, 150, 800, 600)
        random.seed(int(time.time()*1000))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        self.drawSierpinski(painter)

    def drawSierpinski(self, painter):
        painter.setBrush(QColor(Qt.blue))
        p1 = QPoint(self.width()/2, self.height()/4 - 100)
        p2 = QPoint(self.width()/4, 3*self.height()/4 + 100)
        p3 = QPoint(3*self.width()/4, 3*self.height()/4 + 100)
        p = [p1, p2, p3]
        idx = random.randrange(0, 3) 
        g = p[idx]
        painter.drawEllipse(g, 1, 1)

        for i in range(10000):
            idx = random.randrange(0, 3) 
            p_rand = p[idx]
            g = QPointF((g.x() + p_rand.x())/2, (g.y() + p_rand.y())/2)
            painter.drawEllipse(g, 1, 1)


if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)
    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
