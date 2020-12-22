from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Buoi02 - Bai03")
        self.setGeometry(300, 200, 800, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        self.drawBongHoa(painter)

    def random(self, n):
        return np.random.randint(n)

    def quay(self, p, c, delta):
        pnew = QPoint()
        goc = delta*np.pi/180
        dx = p.x() - c.x()
        dy = p.y() - c.y()
        pnew.setX(int(c.x() + dx * np.cos(goc) - dy * np.sin(goc)))
        pnew.setY(int(c.y() + dx * np.sin(goc) + dy * np.cos(goc)))
        return pnew

    def drawBongHoa(self, painter):
        painter.setBrush(
            QColor(self.random(255), self.random(255), self.random(255)))
        x = self.random(self.width())
        y = self.random(self.height())
        rx = ry = 50
        c = QPoint(x, y)
        p = QPoint(x, y - rx)
        for i in range(1, 6):
            pnew = self.quay(p, c, i*72)
            painter.drawEllipse(pnew, rx, ry)


if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
