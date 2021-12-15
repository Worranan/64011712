import os
from PyQt5 import QtGui
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import random
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class myWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1000,775)
        self.generalLayout = QHBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self.but1 = QPushButton("1")
        self.but1.setFixedSize(100,100)

        self.but2 = QPushButton("2")
        self.but2.setFixedSize(100,100)

        self.but3 = QPushButton("3")
        self.but3.setFixedSize(100,100)

        self.generalLayout.addWidget(self.but1)
        self.generalLayout.addWidget(self.but2)
        self.generalLayout.addWidget(self.but3)

        self.color = ["(102,153,255)", "(255, 51, 153)", "(255, 153, 102)", "(51, 204, 51)"]
        n1 = random.randint(0,3)
        self.but1.setStyleSheet("background-color: rgb" + self.color[n1])
        n2 = random.randint(0,3)
        self.but2.setStyleSheet("background-color: rgb" + self.color[n2])
        n3 = random.randint(0,3)
        self.but3.setStyleSheet("background-color: rgb" + self.color[n3])

        self.but1.clicked.connect(self.ran)
    def ran(self):
        n1 = random.randint(0,3)
        self.but1.setStyleSheet("background-color: rgb" + self.color[n1])
app = QApplication([])
myWindow = myWindow()
myWindow.show()

app.exec()