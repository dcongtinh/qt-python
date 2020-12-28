import sys
from math import cos, sin
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

name = 'Đồng hồ chạy'


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.timer = QTimer()
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start(50)

        # config angles
        self.secondAngle = 90
        # use multiple of 60 to config for minuteAngle and hour angle to avoid differences in precision
        self.minuteAngle = 90*60
        self.hourAngle = 90*3600

    def getPointInCircle(self, center, r, angle):
        return QPoint(
            center.x() + r * cos(- angle / 180 * 3.14),
            center.y() + r * sin(- angle / 180 * 3.14)
        )

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(painter.Antialiasing, True)
        painter.setPen(QPen(Qt.black, 2))
        painter.setBrush(Qt.black)
        center = QPoint(self.width()/2, self.height()/2)
        painter.drawRoundedRect(
            QRect(center.x()-250, center.y()-250, 500, 500), 30, 30)
        painter.setBrush(Qt.white)
        painter.drawEllipse(center, 240, 240)
        painter.setBrush(Qt.black)

        painter.setPen(QPen(Qt.red, 2))
        tmp = self.getPointInCircle(center, 200, self.secondAngle)
        painter.drawLine(center, tmp)

        painter.setPen(QPen(Qt.black, 2))
        tmp = self.getPointInCircle(center, 150, self.minuteAngle / 60)
        painter.drawLine(center, tmp)

        tmp = self.getPointInCircle(center, 90, self.hourAngle / 3600)
        painter.drawLine(center, tmp)

        # Draw numbers on the clock to painterPath
        font = QFont("Georgia", 40)
        path = QPainterPath()
        fi = 90
        for i in range(12):
            p = self.getPointInCircle(center, 200, fi)
            st = '%d' % (12 if i == 0 else i)
            fm = QFontMetrics(font)
            fwidth = fm.width(st)
            fheight = fm.height()
            path.addText(QPoint(p.x()-fwidth/2, p.y() + fheight/4), font, st)
            fi -= 360//12

        # paint the path onto screen
        painter.drawPath(path)

    def handleTimer(self):
        # change the angles:
        angle = 6
        self.secondAngle -= angle
        if (self.secondAngle < -360):
            self.secondAngle += 360
        self.minuteAngle -= angle
        if (self.minuteAngle < -360*60):
            self.minuteAngle += 360*60
        self.hourAngle -= angle * 30.0 / 6
        if (self.hourAngle < -360*3600):
            self.hourAngle += 360*3600

        # then repaint frame
        self.repaint()


if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
