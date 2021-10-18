from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Your code here

        self.layout1 = QVBoxLayout()
        self.setLayout(self.layout1)

        self.layout2 = QHBoxLayout()
        self.label1 = QLabel('Enter x')
        self.lineEditX = QLineEdit()
        self.layout2.addWidget(self.label1)
        self.layout2.addWidget(self.lineEditX)
        self.layout1.addLayout(self.layout2)

        self.layout3 = QHBoxLayout()
        self.label2 = QLabel('Enter y')
        self.lineEditY = QLineEdit()
        self.layout3.addWidget(self.label2)
        self.layout3.addWidget(self.lineEditY)
        self.layout1.addLayout(self.layout3)

        self.buttonAdd = QPushButton('Add')
        self.buttonAdd.clicked.connect(self.actionAdd)
        self.layout1.addWidget(self.buttonAdd)

        self.layout4 = QHBoxLayout()
        self.label3 = QLabel('x+y = ')
        self.labelResult = QLabel()
        self.layout4.addWidget(self.label3)
        self.layout4.addWidget(self.labelResult)
        self.layout1.addLayout(self.layout4)


    def actionAdd(self):
        x = int(self.lineEditX.text())
        y = int(self.lineEditY.text())
        z = x+y
        self.labelResult.setText(str(z))
    
app = QApplication([])
myWindow = MyWindow()
myWindow.show()
app.exec()
