from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys

name = 'Quốc kỳ'


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Buoi02 - Bai10")
        self.setGeometry(300, 150, 800, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        self.drawQuocKy(painter)

    def drawQuocKy(self, painter):
        painter.setPen(Qt.red)
        painter.setBrush(QColor(Qt.red))
        painter.drawRect(self.width()/4, self.height()/4,
                         self.width()/2, self.height()/2)
        x = self.width()/2
        y = self.height()/2
        p = QPoint(x, y-100)  # dinh 1
        c = QPoint(x, y)  # tam quay
        v, v2 = [], []
        v.append(p)

        for i in range(1, 5):
            v.append(self.quay(p, c, i*72))

        painter.setPen(Qt.yellow)
        painter.setBrush(QColor(Qt.yellow))
        p_mid = QPoint((v[1].x() + v[4].x())/2, (v[1].y() + v[4].y())/2)
        d = np.sqrt(pow(v[0].x() - p_mid.x(), 2) +
                    pow(v[0].y() - p_mid.y(), 2))
        dx = d * np.tan(18*np.pi/180)
        p_new = QPoint(int(p_mid.x()+dx), p_mid.y())
        v2.append(p_new)
        for i in range(1, 5):
            v2.append(self.quay(p_new, c, i*72))

        #    QPolygon star
        star = QPolygon()
        for i in range(5):
            star << v[i] << v2[i]

        painter.drawPolygon(star)

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
