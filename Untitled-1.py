from abc import abstractclassmethod
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.c = ""

        self.layout1 = QVBoxLayout()
        self.setLayout(self.layout1)

        self.layout2 = QVBoxLayout()
        self.labelResult = QLabel()
        self.layout2.addWidget(self.labelResult)
        self.layout1.addLayout(self.layout2)

        self.layout3 = QVBoxLayout()

        self.buttonAdd1 = QPushButton("1")
        self.buttonAdd1.clicked.connect(self.showing1)
        self.layout3.addWidget(self.buttonAdd1)

        self.buttonAdd2 = QPushButton("2")
        self.buttonAdd2.clicked.connect(self.showing2)
        self.layout3.addWidget(self.buttonAdd2)

        self.layout1.addLayout(self.layout3)


    def showing1(self):
        self.a = 1
        self.c += str(self.a)
        self.labelResult.setText(self.c)

    def showing2(self):
        self.a = 2
        self.c += str(self.a)
        self.labelResult.setText(self.c)
        

app = QApplication([])
myWindow = MyWindow()
myWindow.show()
app.exec()
