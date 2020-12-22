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
    syllabus = getModule(module)
    for key in syllabus:
        if key == 'name':
            continue
        syllabus[key] = getModule(syllabus[key])
    return syllabus


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Mô phỏng đồ hoạ máy tính'
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

        # load modules from folder /Buoi 
        self.modules = modules = moduleToDict(__import__('Buoi'))
        
        # add data to menus
        syllabus = []
        for alias in modules:
            if alias != 'name':
                syllabus.append(alias)

        syllabusIndex = 0
        for syl in syllabus:
            subMenu = mainMenu.addMenu(modules[syl].get('name', syl))
            exerciseIndex = 0
            exercises = []
            for alias in modules[syl]:
                if alias != 'name':
                    exercises.append(alias)
            # traverse through exercises in each syllabus
            for sub in exercises:
                exerciseSelectAction = QAction(
                    getattr(modules[syl][sub], 'name', sub), self)
                # connect to actions
                exerciseSelectAction.triggered.connect(
                    partial(
                        self.exerciseSelectHandler,
                        {'syllabus': syl, 'exercise': sub}
                    )
                )
                subMenu.addAction(exerciseSelectAction)
                exerciseIndex += 1
            syllabusIndex += 1

        self.vLayout = QBoxLayout(QBoxLayout.TopToBottom, self)
        self.show()

    def exerciseSelectHandler(self, config):
        # load exercise first

        exercise = self.modules[config['syllabus']][config['exercise']]
        if self.currentExerciseWindow:
            self.currentExerciseWindow.deleteLater()

        self.currentExerciseWindow = window = exercise.Window()
        self.vLayout.addWidget(window)
        self.setCentralWidget(window)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())
