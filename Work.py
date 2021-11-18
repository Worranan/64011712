from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

class myWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Break Game")
        self.resize(525, 775)

        self.button = QPushButton("Hello",self,)
        self.button.setGeometry(100,100,100,100)
        self.button.clicked.connect(self.but)
    def but(self):
        self.button.setStyleSheet("background-color: red")
app = QApplication([])
myWindow = myWindow()
myWindow.show()

app.exec()