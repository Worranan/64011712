from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import random

class myWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Break Game")
        self.resize(525, 775)

        self.button = QPushButton("Hello",self,)
        self.button.setGeometry(100,100,100,100)
        self.button.clicked.connect(self.but)

        "(102,153,255)"

        "(255, 51, 153)"

        "(255, 153, 102)"

        "(51, 204, 51)"


    def but(self):
        n = random.randint(0,3)
        a = ["(102,153,255)", "(255, 51, 153)", "(255, 153, 102)", "(51, 204, 51)"]
        self.button.setStyleSheet("background-color: rgb" + a[n])
app = QApplication([])
myWindow = myWindow()
myWindow.show()

app.exec()