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
                # print(self.numcolor)

        for btnText,pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(100,100)
            
            

            self.buttons[btnText].setStyleSheet("background-color: rgb" + self.color[self.numcolor[pos[0]][pos[1]]])
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
            
            
        self.generalLayout.addLayout(buttonsLayout)
        for btnText, pos in buttons.items():
            self.buttons[btnText].clicked.connect(lambda checked,g = btnText:self.but(g))
    


    def but(self, i):
        a = i.split(" ")
        self.check(int(a[0]), int(a[1]),self.numcolor[int(a[0])][int(a[1])] )
        
        n = random.randint(0,3)
        self.numcolor[int(a[0])][int(a[1])] = n
        self.buttons[i].setStyleSheet("background-color: rgb" + self.color[self.numcolor[int(a[0])][int(a[1])]])
        
    def check(self, fir, sec, numcolor): # try to change others around color
        # if self.numcolor[fir][sec-1] == numcolor : #left
        #     b = str(fir)+ " " + str(sec-1)
        #     self.but(b)
        # if self.numcolor[fir][sec+1] == numcolor : #right
        #     b = str(fir)+ " " + str(sec+1)
        #     self.but(b)



        if self.numcolor[fir][sec-1] == numcolor : #left
            b = str(fir)+ " " + str(sec-1)
            n = random.randint(0,3)
            self.numcolor[fir][sec-1] = n
            self.buttons[b].setStyleSheet("background-color: rgb" + self.color[self.numcolor[fir][sec-1]])
        if self.numcolor[fir][sec+1] == numcolor : #right
            b = str(fir)+ " " + str(sec+1)
            n = random.randint(0,3)
            self.numcolor[fir][sec+1] = n
            self.buttons[b].setStyleSheet("background-color: rgb" + self.color[self.numcolor[fir][sec+1]])




app = QApplication([])
myWindow = myWindow()
myWindow.show()

app.exec()