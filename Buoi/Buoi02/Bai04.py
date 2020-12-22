from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Buoi02 - Bai04")
        self.setGeometry(300, 200, 800, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        self.drawNguGiac(painter)

    def drawNguGiac(self, painter):
        painter.setPen(Qt.red)
        x = self.width()/2
        y = self.height()/2
        p = QPoint(x, y-100)
        c = QPoint(x, y)
        poly = QPolygon()
        poly << p
        for i in range(1, 5):
            pnew = self.quay(p, c, i*72)
            poly << pnew

        painter.drawPolygon(poly)
        painter.setPen(Qt.blue)
        painter.drawLine(poly.value(0), poly.value(2))
        painter.drawLine(poly.value(0), poly.value(3))
        painter.drawLine(poly.value(1), poly.value(3))
        painter.drawLine(poly.value(1), poly.value(4))
        painter.drawLine(poly.value(2), poly.value(4))

    def quay(self, p, c, delta):
        pnew = QPoint()
        goc = delta*np.pi/180
        dx = p.x() - c.x()
        dy = p.y() - c.y()
        pnew.setX(int(c.x() + dx * np.cos(goc) - dy * np.sin(goc)))
        pnew.setY(int(c.y() + dx * np.sin(goc) + dy * np.cos(goc)))
        return pnew


if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
