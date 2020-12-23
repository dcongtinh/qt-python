from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys

name = 'Thái cực'


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Buoi02 - Bai05")
        self.setGeometry(300, 150, 800, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        self.drawThaiCuc(painter)

    def drawThaiCuc(self, painter):
        painter.setPen(Qt.red)
        x = self.width()/2
        y = self.height()/2
        r = 200
        r1 = r/2
        x1 = x - r
        y1 = y - r1
        xr = x
        yr = y - r1
        p = QPoint(x, y)

        painter.drawEllipse(p, r, r)
        painter.drawArc(x1, y1, r, r, 0, -180*16)

        xr = self.doixungX(QPoint(x1, y1), 0).x()
        yr = self.doixungY(QPoint(x1, y1), 0).y()
        xr = self.tinhtien(QPoint(xr, yr), r, 0).x()

        painter.drawArc(xr, yr, r, r, 0, 180*16)
        p1 = QPoint(x - r/2, y)
        p2 = QPoint(x + r/2, y)
        painter.drawEllipse(p1, r/10, r/10)
        painter.drawEllipse(p2, r/10, r/10)

    def quay(self, p, c, delta):
        goc = delta*np.pi/180
        dx = p.x() - c.x()
        dy = p.y() - c.y()
        pnew = QPoint(int(c.x() + dx * np.cos(goc) - dy * np.sin(goc)),
                      int(c.y() + dx * np.sin(goc) + dy * np.cos(goc)))
        return pnew

    def tinhtien(self, p, tx, ty):
        pnew = QPoint(p.x() + tx, p.y() + ty)
        return pnew

    def doixungX(self, p, y):
        pnew = QPoint(p.x(), 2*y - p.y())
        return pnew

    def doixungY(self, p, x):
        pnew = QPoint(2*x - p.x(), p.y())
        return pnew


if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
