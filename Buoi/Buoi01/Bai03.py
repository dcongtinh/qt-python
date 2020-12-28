import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

name = 'Ngôi nhà'


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Buoi01 - Bai03")
        self.setGeometry(300, 150, 800, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.translate((self.width()-150) // 2, (self.height()-225) // 2)
        self.drawHouse(painter)

    def drawHouse(self, painter):
        points = QPolygonF([
            QPointF(150/2, 0),
            QPointF(0, 150),
            QPointF(0, 300),
            QPointF(150, 300),
            QPointF(150, 150),
            QPointF(150/2, 0),
        ])

        painter.setBrush(Qt.white)
        painter.drawRect(20, 20, 20, 150)
        painter.drawPolygon(points, 6)
        painter.drawRect(30, 150+150/2, 50, 150/2)
        painter.drawRect(150/2+20, 150+150/4, 30, 150/4)


if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
