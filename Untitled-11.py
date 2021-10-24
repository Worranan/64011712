from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")

        self.c = ""

        self.labelResult = QLabel()
        self.setGeometry(0,0,125*9,50)

        g = 10
        # for i in range(0,10):
        #     self.button = QPushButton("{}".format(i),self)
        #     self.button.setGeometry(125*i,100,100,100)
        for i in range(0,3):
            for i2 in range(0,3):
                g -= 1
                self.button = QPushButton("{}".format(g),self)
                self.button.setGeometry(125*i2,130+125*i,100,100)

        #     self.button.clicked.connect(self.but)
        # def but(self):
        
            
        
        widget = QWidget()
        self.setCentralWidget(widget)

app = QApplication([])
myWindow = MyWindow()
myWindow.show()

app.exec()
