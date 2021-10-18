from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Your code here

        self.layout1 = QVBoxLayout()
        self.setLayout(self.layout1)

        # self.buttonAdd = QPushButton("1")
        # self.buttonAdd.clicked.connect(self.show)
        # self.layout1.addWidget(self.buttonAdd)

        self.layout2 = QVBoxLayout()
        self.label1 = QLabel("1")
        self.layout2.addWidget(self.label1)
        self.layout1.addLayout(self.layout2)

    #     self.layout3 = QVBoxLayout()
    #     self.labelResult = QLabel()
    #     self.layout3.addWidget(self.labelResult)
    #     self.layout1.addLayout(self.layout3)

    # def show(self):
    #     self.labelResult.setText("1")

    
app = QApplication([])
myWindow = MyWindow()
myWindow.show()
app.exec()
