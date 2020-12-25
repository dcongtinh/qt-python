from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
import numpy as np
import sys
from functools import partial
from math import cos, sin, tan, sqrt
from random import randint

name = 'Hello, World!!!'


class Snowflake:
    def __init__(self, position, size, angle):
        self.position = position
        self.size = size
        self.angle = angle


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.timer = QTimer()
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start(10)
        self.maxSnowflake = 50
        self.flakes = []

        self.currentPosition = None
        self.angle = 0

        # additional setup
        self.player = QMediaPlayer()
        # play sound
        # find desired path
        theme_song_path = QDir.current().absoluteFilePath('Assets/theme_song.mp3')

        # load file and play
        sound = QMediaContent(QUrl.fromLocalFile(theme_song_path))
        self.player.setMedia(sound)
        self.player.setVolume(100)
        self.player.play()

    def dichuyen(self, painter, kc, drawLine=True):
        p = self.currentPosition
        pnew = QPointF(
            p.x() + kc*np.cos(3.14*self.angle/180),
            p.y() + kc*np.sin(3.14*self.angle/180)
        )
        if drawLine:
            painter.drawLine(p, pnew)
        self.currentPosition = pnew

    def xoay(self, alpha):
        self.angle += alpha

    def drawSnowflake(self, painter, P, l, k, startAngle):
        x3 = l*np.sqrt(2)/80.
        x1 = x3/np.sin(np.pi*30/180)
        # move to P
        self.currentPosition = P
        self.angle = startAngle

        # k parts
        for _ in range(0, k):
            self.xoay(-30)
            self.dichuyen(painter, x1, drawLine=False)
            self.xoay(30)
            self.dichuyen(painter, l*4/10)
            self.xoay(-60)
            self.dichuyen(painter, l*3/10)
            self.xoay(90)
            self.dichuyen(painter, l/40)
            self.xoay(90)
            self.dichuyen(painter, l*3/10-l/(40*tan(60*np.pi/180)))
            self.xoay(-120)
            self.dichuyen(painter, l/5)
            self.xoay(-60)
            self.dichuyen(painter, l/5)
            self.xoay(90)
            self.dichuyen(painter, l/40)

            self.xoay(90)
            self.dichuyen(painter, l/5-l/(40*sqrt(3)))
            self.xoay(-120)
            self.dichuyen(painter, l/5)

            # draw top
            self.xoay(45)
            self.dichuyen(painter, l/40)
            self.xoay(90)
            self.dichuyen(painter, l/40)

            # # draw symmetry shape
            self.xoay(45)
            self.dichuyen(painter, l/5)
            self.xoay(-120)
            self.dichuyen(painter, l/5-l/(40*sqrt(3)))
            self.xoay(90)
            self.dichuyen(painter, l/40)
            self.xoay(90)
            self.dichuyen(painter, l/5)
            self.xoay(-60)
            self.dichuyen(painter, l/5)
            self.xoay(-120)
            self.dichuyen(painter, l*3/10-l/(40*tan(60*np.pi/180)))
            self.xoay(90)
            self.dichuyen(painter, l/40)
            self.xoay(90)
            self.dichuyen(painter, l*3/10)
            self.xoay(-60)
            self.dichuyen(painter, l*2/5)
            self.xoay(30)
            self.dichuyen(painter, x1, drawLine=False)

            self.xoay(150)
            self.xoay(360/k)

    def drawText(self, painter):
        fontFamily = "CMU Serif, Arial"
        font = QFont(fontFamily, 60)
        path = QPainterPath()
        st = 'Thực hành'
        fm = QFontMetrics(font)
        fwidth = fm.width(st)
        fheight = fm.height()
        path.addText(QPoint(self.width()/2-fwidth/2,
                            self.height()/2 + fheight/4 - 120), font, st)

        st = 'Đồ Hoạ Máy Tính'
        fm = QFontMetrics(font)
        fwidth = fm.width(st)
        fheight = fm.height()
        path.addText(QPoint(self.width()/2-fwidth/2,
                            self.height()/2 + fheight/4 - 50), font, st)

        font = QFont(fontFamily, 36)
        st = 'ThS. Phạm Xuân Hiền'
        fm = QFontMetrics(font)
        fwidth = fm.width(st)
        fheight = fm.height()
        path.addText(QPoint(self.width()/2-fwidth/2,
                            self.height()/2 + fheight/4 + 50), font, st)

        font = QFont(fontFamily, 16)
        st = '© 2020 Cong Tinh Dao, Vinh Phuc Ta Dang'
        fm = QFontMetrics(font)
        fwidth = fm.width(st)
        fheight = fm.height()
        path.addText(QPoint(self.width()/2-fwidth/2,
                            self.height()/2 + fheight/4 + 260), font, st)
        painter.setBrush(Qt.black)
        painter.drawPath(path)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(Qt.white)
        painter.setPen(Qt.white)
        painter.drawRect(0, 0, self.width(), self.height())

        painter.setPen(QColor('#00a8ff'))
        painter.setOpacity(0.08)
        for flake in self.flakes:
            self.drawSnowflake(painter, flake.position,
                               flake.size, 6, self.angle)

        painter.setPen(Qt.black)
        painter.setOpacity(1)
        self.drawText(painter)

    def newFlake(self, pos=None):
        size = randint(2, 6)*10
        if not pos:
            pos = QPointF(randint(0, self.width()), -size*2)
        flake = Snowflake(
            position=pos,
            size=size,
            angle=randint(0, 180)
        )
        return flake

    def handleTimer(self):
        # start generating in handle timer may make coordination more exactly
        flakes = self.flakes
        if not len(self.flakes):
            # generate stars
            for i in range(self.maxSnowflake):
                self.flakes.append(self.newFlake(pos=QPointF(
                    randint(0, self.width()), randint(0, self.width()))))
        # calculate target color of stars for next frame
        for i in range(len(flakes)):
            flakes[i].angle += 3
            if flakes[i].angle > 360:
                flakes[i].angle -= 360

            curPos = flakes[i].position
            if curPos.y() > self.height() + flakes[i].size:
                flakes[i] = self.newFlake()
                continue
            curPos = QPointF(curPos.x(), curPos.y() + 4)
            flakes[i].position = curPos

        self.repaint()


if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)
    # create the instance of our Window
    window = Window()
    window.show()
    # start the app
    sys.exit(App.exec())
