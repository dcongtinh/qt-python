'''
Author: Cong-Tinh Dao, Vinh Phuc Ta Dang
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from functools import partial
import sys
import types
from PyQt5.QtMultimedia import *

def moduleToDict(module):
    ''' Convert to dict for easier accesss
    Structure:
    {
        'Buoi01': {
            'Bai01': <Module>
            'Bai02': <Module>
            'name': 'Buổi thực hành 1'
        },
        'Buoi02': {
            'Bai01': <Module>
            'Bai02': <Module>
            'Bai03': <Module>
            'name': 'Buổi thực hành 2'
        }
    }
    where <Module> could be anything, app.py should find a class named Window, instantiate it and insert on top of the screen
    '''
    def getModule(module):
        modules = {}
        for attr in dir(module):
            if attr == 'name':
                modules[attr] = getattr(module, attr)
                continue
            typeAttr = type(getattr(module, attr))
            if typeAttr == types.ModuleType:
                modules[attr] = getattr(module, attr)
        return modules
    units = getModule(module)
    for key in units:
        if key == 'name':
            continue
        units[key] = getModule(units[key])
    return units


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Đồ hoạ máy tính'
        self.left = 300
        self.top = 150
        self.width = 900
        self.height = 600
        # current focus window:
        self.currentExerciseWindow = None

        # coordinate views
        self.initUI()

    def initUI(self):
        # init sizes
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False)
        mainMenu.setStyleSheet(
            "padding: 2px 0;font-size: 16px;")

        import Buoi
        # load modules from folder /Buoi
        self.modules = modules = moduleToDict(Buoi)

        # add data to menus
        for unit in modules:
            subMenu = mainMenu.addMenu(modules[unit].get('name', unit))

            # traverse through exercises in each units
            for sub in modules[unit]:
                if sub == 'name':
                    continue
                exerciseSelectAction = QAction(
                    getattr(modules[unit][sub], 'name', sub), self)
                # connect to actions
                exerciseSelectAction.triggered.connect(
                    partial(
                        self.exerciseSelectHandler,
                        {'units': unit, 'exercise': sub}
                    )
                )
                subMenu.addAction(exerciseSelectAction)

        self.vLayout = QBoxLayout(QBoxLayout.TopToBottom, self)

        self.exerciseSelectHandler(
            {'units': 'Khac', 'exercise': 'Home'})
        self.show()

    def exerciseSelectHandler(self, config):
        # load exercise first
        exercise = self.modules[config['units']][config['exercise']]
        if self.currentExerciseWindow:
            # delete it in current window
            self.currentExerciseWindow.deleteLater()

        # allocate new window
        self.currentExerciseWindow = window = exercise.Window()
        self.vLayout.addWidget(window)
        self.setCentralWidget(window)

        # set current title
        self.setWindowTitle('Đồ hoạ máy tính - %s' %
                            getattr(exercise, 'name', config['exercise']))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())
