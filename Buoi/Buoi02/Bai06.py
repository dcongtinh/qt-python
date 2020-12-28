import sys
import numpy as np
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

name = 'Rosette'


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Buoi02 - Bai06")
        self.setGeometry(300, 150, 840, 600)
        self.a = list([0]*50)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        self.drawRosette(painter)

    def tohop(self, painter, v, i, n, k):
        if i > k:
            painter.drawLine(v[self.a[1]-1], v[self.a[2]-1])
            return
        for j in range(self.a[i-1]+1, n-k+i + 1):
            self.a[i] = j
            self.tohop(painter, v, i+1, n, k)

    def drawRosette(self, painter):
        painter.setPen(Qt.black)
        x = 50
        y = 150
        arr_n = [3, 4, 5, 6, 12, 16, 40]
        for idx in range(len(arr_n)):
            poly = QPolygon()
            p = QPoint(x, y-50)  # dinh 1
            c = QPoint(x, y)  # tam quay
            poly << p
            for i in range(1, arr_n[idx]):
                poly << self.quay(p, c, i*(360/arr_n[idx]))

            painter.drawPolygon(poly)
            x += 120

        # Ve Rosette
        rosette_n = [5, 11, 20]
        x = 150
        y += 200
        v = []
        for idx in range(len(rosette_n)):
            p = QPoint(x, y-100)  # dinh 1
            c = QPoint(x, y)  # tam quay
            v.append(p)
            for i in range(1, rosette_n[idx]):
                v.append(self.quay(p, c, i*(360/rosette_n[idx])))

            painter.setPen(Qt.blue)
            # To hop cac diem noi lai
            self.tohop(painter, v, 1, rosette_n[idx], 2)
            x += 240
            v = []
            self.a = list([0]*50)

    def quay(self, p, c, delta):
        goc = delta*np.pi/180
        dx = p.x() - c.x()
        dy = p.y() - c.y()
        pnew = QPoint(int(c.x() + dx * np.cos(goc) - dy * np.sin(goc)),
                      int(c.y() + dx * np.sin(goc) + dy * np.cos(goc)))
        return pnew


if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
