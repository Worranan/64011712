from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *


import Work
import withbot
import Howto

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setWindowTitle("BreakMePlease")
        self.setGeometry(50,50,950,600)

        self.FirstWindow()

    def FirstWindow(self):
        label = QLabel("Break me Please",  self)
        label.setGeometry(180, 100, 800,100)
        label.setFont(QFont("Times", 50))

        btn = QPushButton("With bot", self)
        btn.clicked.connect(self.secondPage)    # - (SecondPage())
        btn.move(150,300)
        btn.setFixedSize(200, 100)
        btn.setFont(QFont("Times", 20))

        btn = QPushButton("Only me", self)
        btn.clicked.connect(self.thirdPage)    # - (Thrid Page())
        btn.setFixedSize(200, 100)
        btn.move(600,300)
        btn.setFont(QFont("Times", 20))

        btn = QPushButton("How to", self)
        btn.clicked.connect(self.forthPage)    # - (Thrid Page())
        btn.setFixedSize(200, 100)
        btn.move(375,450)
        btn.setFont(QFont("Times", 20))

        self.show()

    def secondPage(self):                       # +++
        self.MewithbotWindow = withbot.myWindow()
        self.MewithbotWindow.show()
    def thirdPage(self):
        self.MeWindow = Work.myWindow()
        self.MeWindow.show()
    def forthPage(self):
        self.Howto = Howto.Window()
        self.Howto.show()

def run():
    app = QApplication([])
    GUI = Window()
    app.exec()

run()