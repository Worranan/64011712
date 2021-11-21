from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import random

class myWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Break Game")
        # self.resize(1000, 775)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)


        self.color = ["(102,153,255)", "(255, 51, 153)", "(255, 153, 102)", "(51, 204, 51)"]
        self._createButtons()


    def _createButtons(self):
        buttonsLayout = QGridLayout()

        self.numcolor = []
        self.buttons = {}
        buttons = {}
        for i in range(0, 9):

            self.numcolor.append([])

            for j in range(0, 9):
                buttons[str(i)+ " " + str(j)] = (i,j)
                n = random.randint(0,3)
                self.numcolor[i].append(n)
                print(self.numcolor)

        for btnText,pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(100,100)
            
            

            self.buttons[btnText].setStyleSheet("background-color: rgb" + self.color[self.numcolor[pos[0]][pos[1]]])
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
            
            
        self.generalLayout.addLayout(buttonsLayout)
        
        
        # self.button = QPushButton("Hello",self)
        # self.button.setGeometry(100,100,100,100)
        # self.button.clicked.connect(self.but)
        # self.create


        # self.button = {}
        # row = range(0, 5)
        # column = range(0,5)
        # for each in row:
        #     self.button[each] = QPushButton("row %d" %row, self)
        #     n = random.randint(0,3)
        #     self.button[each].setGeometry(100,100*each,100,100)
        #     self.button[each].setStyleSheet("background-color: rgb" + self.color[n])


    # def but(self):
    #     n = random.randint(0,3)
    #     self.button.setStyleSheet("background-color: rgb" + self.color[n])
app = QApplication([])
myWindow = myWindow()
myWindow.show()

app.exec()