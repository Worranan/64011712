from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Awesome App")

        self.resize(500,300)
        
        self.clickNum = 0
        
        self.label = QLabel('No. of clicks = '+str(self.clickNum))
        self.setCentralWidget(self.label)

        self.button = QPushButton("Click me", self.label)
        self.button.move(100,150)

        self.button.clicked.connect(self.increment)
        
    def increment(self):
        self.clickNum+=1
        self.label.setText('No. of clicks = '+str(self.clickNum))
    
        

app = QApplication([])
myWindow = MyWindow()
myWindow.show()

app.exec()
