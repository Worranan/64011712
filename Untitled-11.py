from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.resize(1000,1000)
        self.c = ""

        self.labelResult = QLabel(self)
        self.labelResult.setGeometry(25,25,125*9,100)
        self.labelResult.setFont(QFont("Times", 30))

        
        g = 10
        for i in range(0,3):
            for i2 in range(0,3):
                g -= 1
                self.button = QPushButton("{}".format(g),self)
                self.button.setGeometry(25+(125*i2),130+(125*i),100,100)
                self.button.setFont(QFont("Times",30))

                self.button.clicked.connect(lambda checked, g = g: self.but(g))

    def but(self,i):
        self.c += str(i)
        self.labelResult.setText(self.c)
            
            
        
        widget = QWidget()
        self.setCentralWidget(widget)

app = QApplication([])
myWindow = MyWindow()
myWindow.show()

app.exec()
