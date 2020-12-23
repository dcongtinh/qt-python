from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys

name = 'Ngôi làng'


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Bai02 - Buoi08")
        self.setGeometry(300, 150, 800, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        self.drawNgoiLang(painter)

    def drawNgoiNha(self, painter, d, w, h, transform):
        painter.setPen(Qt.black)
        painter.setBrush(QColor(Qt.white))
        poly = QPolygon()
        if transform == "":
            poly << d
            poly << QPoint(d.x() + w/2, d.y() + h/3)
            poly << QPoint(d.x() + w/2, d.y() + h)
            poly << QPoint(d.x() - w/2, d.y() + h)
            poly << QPoint(d.x() - w/2, d.y() + h/3)
            poly << d
            painter.drawRect(d.x() - w/3, d.y(), w/6, h/3)  # Ve ong khoi
            painter.drawPolygon(poly)
            painter.drawRect(d.x() - w/4, d.y() + 2*h /
                             3, w/4, h/3)  # Ve cua chinh
            painter.drawRect(d.x() + w/6, d.y() + h/2, w/6, h/6)  # Ve cua so
        elif transform == "flipX":
            poly << self.doixungX(d, d.y())
            poly << self.doixungX(QPoint(d.x() + w/2, d.y() + h/3), d.y())
            poly << self.doixungX(QPoint(d.x() + w/2, d.y() + h), d.y())
            poly << self.doixungX(QPoint(d.x() - w/2, d.y() + h), d.y())
            poly << self.doixungX(QPoint(d.x() - w/2, d.y() + h/3), d.y())
            poly << self.doixungX(d, d.y())
            # p ong khoi
            p_khoi = self.doixungX(QPoint(d.x() - w/3, d.y()), d.y())
            painter.drawRect(p_khoi.x(), p_khoi.y() - h /
                             3, w/6, h/3)  # Ve ong khoi
            painter.drawPolygon(poly)
            # p cua chinh
            p_cuachinh = self.doixungX(
                QPoint(d.x() - w/4, d.y() + 2*h/3), d.y())
            painter.drawRect(p_cuachinh.x(), p_cuachinh.y() -
                             h/3, w/4, h/3)  # Ve cua chinh
            # p cua so
            p_cuaso = self.doixungX(QPoint(d.x() + w/6, d.y() + h/2), d.y())
            painter.drawRect(p_cuaso.x(), p_cuaso.y() -
                             h/6, w/6, h/6)  # Ve cua so
        elif transform == "flipY":
            poly << self.doixungY(d, d.x())
            poly << self.doixungY(QPoint(d.x() + w/2, d.y() + h/3), d.x())
            poly << self.doixungY(QPoint(d.x() + w/2, d.y() + h), d.x())
            poly << self.doixungY(QPoint(d.x() - w/2, d.y() + h), d.x())
            poly << self.doixungY(QPoint(d.x() - w/2, d.y() + h/3), d.x())
            poly << self.doixungY(d, d.x())
            # p ong khoi
            p_khoi = self.doixungY(QPoint(d.x() - w/3, d.y()), d.x())
            painter.drawRect(p_khoi.x()-w/6, p_khoi.y(),
                             w/6, h/3)  # Ve ong khoi
            painter.drawPolygon(poly)
            # p cua chinh
            p_cuachinh = self.doixungY(
                QPoint(d.x() - w/4, d.y() + 2*h/3), d.x())
            painter.drawRect(p_cuachinh.x() - w/4,
                             p_cuachinh.y(), w/4, h/3)  # Ve cua chinh
            # p cua so
            p_cuaso = self.doixungY(QPoint(d.x() + w/6, d.y() + h/2), d.x())
            painter.drawRect(p_cuaso.x() - w/6, p_cuaso.y(),
                             w/6, h/6)  # Ve cua so

    def drawNgoiLang(self, painter):
        x = self.width()/2
        y = self.height()/2
        w = h = 150
        self.drawNgoiNha(painter, QPoint(x, y), w, h, "flipY")
        self.drawNgoiNha(painter, QPoint(150, 150), w, h, "")
        self.drawNgoiNha(painter, QPoint(100, 3), 60, 90, "")
        self.drawNgoiNha(painter, QPoint(250, 30), 120, 90, "")
        self.drawNgoiNha(painter, QPoint(400, 20), 60, 150, "")
        self.drawNgoiNha(painter, QPoint(600, 300), w, h, "flipX")

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
