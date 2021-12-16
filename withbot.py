import os
from PyQt5 import QtGui
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import random
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class myWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Break Game")
        self.setGeometry(100, 50 , 800, 800)
        self.generalLayout = QHBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)



        self.element = []

        self.color = ["(102,153,255)", "(255, 51, 153)", "(255, 153, 102)", "(51, 204, 51)"]


        self._createButtons()
        self.score()
        

    def score(self):
        self.score = {}
        self.score["me"] = 0
        self.score["bot"] = 0

        self.resultscore = QLabel("Me : " + str(self.score["me"]))
        self.resultscore.setFont(QFont("Times", 20))
        scorelayout = QVBoxLayout()
        scorelayout.addWidget(self.resultscore)
        # scorelayout.setContentsMargins(0, 0, 0, 0) #check agian
        self.generalLayout.addLayout(scorelayout)
        self.resultscorebot = QLabel("Bot : " + str(self.score["me"]))
        self.resultscorebot.setFont(QFont("Times", 20))
        scorelayout.addWidget(self.resultscorebot)

    def allcheck(self):
        b = 0
        for i in range(0,len(self.numcolor)):
            for each2 in range(0, len(self.numcolor[i])):
                self.check(i, each2,self.numcolor[i][each2])
                # print(len(self.element), i , each2)

                if len(self.element) >=3:
                    b += 1
                    break
                self.element = []
            if b > 0:
                break
        self.element = []
        # print("\n")
    
        if b == 0:
            self.numcolor = []
            buttons = {}
            for i in range(0, 9):

                self.numcolor.append([])

                for j in range(0, 9):
                    buttons[str(i)+ " " + str(j)] = (i,j)
                    n = random.randint(0,3)
                    self.numcolor[i].append(n)
                    # print(self.numcolor)

            for btnText,pos in buttons.items():
                self.buttons[btnText].setStyleSheet("background-color: rgb" + self.color[self.numcolor[pos[0]][pos[1]]])
        b = 0

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
            self.buttons[btnText] = QPushButton()
            self.buttons[btnText].setFixedSize(100,100)



            self.buttons[btnText].setStyleSheet("background-color: rgb" + self.color[self.numcolor[pos[0]][pos[1]]])
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])

        self.generalLayout.addLayout(buttonsLayout)
        for btnText, pos in buttons.items():
            self.buttons[btnText].clicked.connect(lambda checked,g = btnText:self.but(g))

    def bot(self):
        c = 0
        while c < 3:
            n1 = random.randint(0,8)
            n2 = random.randint(0,8)
            self.check(n1, n2,self.numcolor[n1][n2])
            c = len(self.element)
            self.element =[]
        # print(n1,n2)
        self.check(n1,n2,self.numcolor[n1][n2])
        self.score["bot"] += len(self.element)
        self.change("bot")
        # print(self.score["bot"])
        self.resultscorebot.setText("Bot : " + str(self.score["bot"]))



    def but(self, i):
        a = i.split(" ")
        self.check(int(a[0]), int(a[1]),self.numcolor[int(a[0])][int(a[1])] )

        # print(self.element)
        self.change("me")
        self.allcheck()
        # print(self.element)


        # n = random.randint(0,3)
        # self.numcolor[int(a[0])][int(a[1])] = n
        # self.buttons[i].setStyleSheet("background-color: rgb" + self.color[self.numcolor[int(a[0])][int(a[1])]])
        self.bot()
        self.allcheck()
    def check(self, fir, sec, numcolor): # try to change others around color
        self.element.append(str(fir) + " " + str(sec))
        if 1 <= fir <=7 and 1<= sec <= 7:
            if self.numcolor[fir][sec-1] == numcolor and str(fir) + " " + str(sec-1) not in self.element: #left
                self.check(fir, sec-1, numcolor)
            if self.numcolor[fir][sec+1] == numcolor and str(fir) + " " + str(sec+1) not in self.element: #left
                self.check(fir, sec+1, numcolor)
            if self.numcolor[fir-1][sec] == numcolor and str(fir-1) + " " + str(sec) not in self.element: #left
                self.check(fir-1, sec, numcolor)
            if self.numcolor[fir+1][sec] == numcolor and str(fir+1) + " " + str(sec) not in self.element: #left
                self.check(fir+1, sec, numcolor)
        elif fir == 0:
            if sec == 0:
                if self.numcolor[fir][sec+1] == numcolor and str(fir) + " " + str(sec+1) not in self.element: #left
                    self.check(fir, sec+1, numcolor)
                if self.numcolor[fir+1][sec] == numcolor and str(fir+1) + " " + str(sec) not in self.element: #left
                    self.check(fir+1, sec, numcolor)
            elif sec == 8:
                if self.numcolor[fir][sec-1] == numcolor and str(fir) + " " + str(sec-1) not in self.element: #left
                    self.check(fir, sec-1, numcolor)
                if self.numcolor[fir+1][sec] == numcolor and str(fir+1) + " " + str(sec) not in self.element: #left
                    self.check(fir+1, sec, numcolor)
            else:
                if self.numcolor[fir][sec-1] == numcolor and str(fir) + " " + str(sec-1) not in self.element: #left
                    self.check(fir, sec-1, numcolor)
                if self.numcolor[fir][sec+1] == numcolor and str(fir) + " " + str(sec+1) not in self.element: #left
                    self.check(fir, sec+1, numcolor)
                if self.numcolor[fir+1][sec] == numcolor and str(fir+1) + " " + str(sec) not in self.element: #left
                    self.check(fir+1, sec, numcolor)
        elif fir == 8:
            if sec == 0:
                if self.numcolor[fir][sec+1] == numcolor and str(fir) + " " + str(sec+1) not in self.element: #left
                    self.check(fir, sec+1, numcolor)
                if self.numcolor[fir-1][sec] == numcolor and str(fir-1) + " " + str(sec) not in self.element: #left
                    self.check(fir-1, sec, numcolor)
            elif sec == 8:
                if self.numcolor[fir][sec-1] == numcolor and str(fir) + " " + str(sec-1) not in self.element: #left
                    self.check(fir, sec-1, numcolor)
                if self.numcolor[fir-1][sec] == numcolor and str(fir-1) + " " + str(sec) not in self.element: #left
                    self.check(fir-1, sec, numcolor)
            else:
                if self.numcolor[fir][sec-1] == numcolor and str(fir) + " " + str(sec-1) not in self.element: #left
                    self.check(fir, sec-1, numcolor)
                if self.numcolor[fir][sec+1] == numcolor and str(fir) + " " + str(sec+1) not in self.element: #left
                    self.check(fir, sec+1, numcolor)
                if self.numcolor[fir-1][sec] == numcolor and str(fir-1) + " " + str(sec) not in self.element: #left
                    self.check(fir-1, sec, numcolor)
        elif sec == 0:
            if self.numcolor[fir][sec+1] == numcolor and str(fir) + " " + str(sec+1) not in self.element: #left
                self.check(fir, sec+1, numcolor)
            if self.numcolor[fir-1][sec] == numcolor and str(fir-1) + " " + str(sec) not in self.element: #left
                self.check(fir-1, sec, numcolor)
            if self.numcolor[fir+1][sec] == numcolor and str(fir+1) + " " + str(sec) not in self.element: #left
                self.check(fir+1, sec, numcolor)
        elif sec == 8:
            if self.numcolor[fir][sec-1] == numcolor and str(fir) + " " + str(sec-1) not in self.element: #left
                self.check(fir, sec-1, numcolor)
            if self.numcolor[fir-1][sec] == numcolor and str(fir-1) + " " + str(sec) not in self.element: #left
                self.check(fir-1, sec, numcolor)
            if self.numcolor[fir+1][sec] == numcolor and str(fir+1) + " " + str(sec) not in self.element: #left
                self.check(fir+1, sec, numcolor)
    def change(self,user):
        if len(self.element) < 3:
            full_file_path = os.path.join(os.getcwd(),"mixkit-exclamation-of-pain-from-a-zombie-2207.wav" )
            url = QUrl.fromLocalFile(full_file_path)
            content = QMediaContent(url)
            self.player = QMediaPlayer()
            self.player.setMedia(content)
            self.player.play()
            self.element = []
        else:
            # print(self.element)
            if user == "me":
                full_file_path = os.path.join(os.getcwd(),"mixkit-game-balloon-or-bubble-pop-3069.wav" )
                url = QUrl.fromLocalFile(full_file_path)
                content = QMediaContent(url)
                self.player = QMediaPlayer()
                self.player.setMedia(content)
                self.player.play()
            for i in range(0, len(self.element)):
                g = self.element[i].split(" ")
                n = random.randint(0,3)
                self.numcolor[int(g[0])][int(g[1])] = n
                self.buttons[self.element[i]].setStyleSheet("background-color: rgb" + self.color[self.numcolor[int(g[0])][int(g[1])]])
            if user == "me":
                self.score["me"] += len(self.element)*1
                self.resultscore.setText("Me : " + str(self.score["me"]))
            self.element = []
    # def score(self):
    #     self.change()
    # def change(self):
    #     for i in range(0,len(self.element)):
    #         g = self.element[i].split(" ")
    #         self.buttons[self.element(i)].setStyleSheet("background-color: rgb" + self.color[self.numcolor[int(g[0])][int(g[1])]])
    #         self.element = []



        # if self.numcolor[fir][sec-1] == numcolor : #left
        #     b = str(fir)+ " " + str(sec-1)
        #     self.but(b)
        # if self.numcolor[fir][sec+1] == numcolor : #right
        #     b = str(fir)+ " " + str(sec+1)
        #     self.but(b)



        # if self.numcolor[fir][sec-1] == numcolor : #left
        #     b = str(fir)+ " " + str(sec-1)
        #     n = random.randint(0,3)
        #     self.numcolor[fir][sec-1] = n
        #     self.buttons[b].setStyleSheet("background-color: rgb" + self.color[self.numcolor[fir][sec-1]])
        # if self.numcolor[fir][sec+1] == numcolor : #right
        #     b = str(fir)+ " " + str(sec+1)
        #     n = random.randint(0,3)
        #     self.numcolor[fir][sec+1] = n
        #     self.buttons[b].setStyleSheet("background-color: rgb" + self.color[self.numcolor[fir][sec+1]])




# app = QApplication([])
# myWindow = myWindow()
# myWindow.show()

# app.exec()