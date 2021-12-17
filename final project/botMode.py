from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *


import withbot

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setWindowTitle("Bot mode")
        self.setGeometry(50,50,950,950)

        self.FirstWindow()

    def FirstWindow(self):
        label = QLabel("Bot mode",  self)
        label.setGeometry(300, 100, 800,100)
        label.setFont(QFont("Times", 50))

        btn = QPushButton("Easy", self)
        btn.clicked.connect(self.easy)
        btn.move(400,300)
        btn.setFixedSize(200, 100)
        btn.setFont(QFont("Times", 20))

        btn = QPushButton("Normal", self)
        btn.clicked.connect(self.normal)
        btn.setFixedSize(200, 100)
        btn.move(400,500)
        btn.setFont(QFont("Times", 20))

        btn = QPushButton("Hard", self)
        btn.clicked.connect(self.hard)    
        btn.setFixedSize(200, 100)
        btn.move(400,700)
        btn.setFont(QFont("Times", 20))
        self.show()

    def easy(self):
        self.MewithbotWindow = withbot.myWindow("Easy")
        self.MewithbotWindow.show()
    def normal(self):
        self.MeWindow = withbot.myWindow("Normal")
        self.MeWindow.show()
    def hard(self):
        self.Howto = withbot.myWindow("Hard")
        self.Howto.show()
    

# def run():
#     app = QApplication([])
#     GUI = Window()
#     app.exec()

# run()