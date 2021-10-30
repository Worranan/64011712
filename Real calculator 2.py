from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setStyleSheet("background-color: rgb(51, 255, 255)")

        self.resize(525 ,775)
        self.c = ""         #use for down line result
        self.s = ""         #use for up line result

        self.labelupResult = QLabel(self)
        self.labelupResult.setGeometry(25,25,(125*4)-25,30)
        self.labelupResult.setFont(QFont("Times", 10))
        self.labelupResult.setStyleSheet("background-color: white")

        self.labelResult = QLabel(self)
        self.labelResult.setGeometry(25,55,(125*4)-25,70)
        self.labelResult.setFont(QFont("Times", 30))
        self.labelResult.setStyleSheet("background-color: white")



        
        g = 10

        for i in range(0,3):
            for i2 in range(0,3):
                g -= 1
                self.button = QPushButton("{}".format(g),self)
                self.button.setGeometry(25+(125*i2),155+(125*i),100,100)
                self.button.setFont(QFont("Times",30))
                self.button.setStyleSheet("background-color: white")

                self.button.clicked.connect(lambda checked, g = g: self.but(g))
        
        #before last line
        self.button = QPushButton("0",self)
        self.button.setGeometry(25+(125*1),155+(125*3),100,100)
        self.button.setFont(QFont("Times",30))
        self.button.setStyleSheet("background-color: white")
        self.button.clicked.connect(lambda checked, g = 0:self.but(g))

        self.button = QPushButton("=",self)
        self.button.setGeometry(25+(125*0),155+(125*3),100,100)
        self.button.setFont(QFont("Times",30))
        self.button.setStyleSheet("background-color: white")
        self.button.clicked.connect(self.equal)

        self.button = QPushButton(".",self)
        self.button.setGeometry(25+(125*2),155+(125*3),100,100)
        self.button.setFont(QFont("Times",30))
        self.button.setStyleSheet("background-color: white")
        self.button.clicked.connect(lambda checked, g = ".":self.but(g))

        #last column
        self.button = QPushButton("/",self)
        self.button.setGeometry(25+(125*3),155+(125*0),100,100)
        self.button.setFont(QFont("Times",30))
        self.button.setStyleSheet("background-color: white")
        self.button.clicked.connect(lambda checked, g = "/":self.sign(g))

        self.button = QPushButton("*",self)
        self.button.setGeometry(25+(125*3),155+(125*1),100,100)
        self.button.setFont(QFont("Times",30))
        self.button.setStyleSheet("background-color: white")
        self.button.clicked.connect(lambda checked, g = "*":self.sign(g))

        self.button = QPushButton("-",self)
        self.button.setGeometry(25+(125*3),155+(125*2),100,100)
        self.button.setFont(QFont("Times",30))
        self.button.setStyleSheet("background-color: white")
        self.button.clicked.connect(lambda checked, g = "-":self.sign(g))

        self.button = QPushButton("+",self)
        self.button.setGeometry(25+(125*3),155+(125*3),100,100)
        self.button.setFont(QFont("Times",30))
        self.button.setStyleSheet("background-color: white")
        self.button.clicked.connect(lambda checked, g = "+":self.sign(g))

        #last row
        self.button = QPushButton("CE",self)
        self.button.setGeometry(25+(125*0),155+(125*4),100+125,100)
        self.button.setFont(QFont("Times",30))
        self.button.setStyleSheet("background-color: white")
        self.button.clicked.connect(self.cebut)
        

        self.button = QPushButton("C",self)
        self.button.setGeometry(25+(125*2),155+(125*4),100+125,100)
        self.button.setFont(QFont("Times",30))
        self.button.setStyleSheet("background-color: white")
        self.button.clicked.connect(self.cbut)

        self.eq = "False"   #use for renew after press (=)
        self.num2 = "False" #use for track this is another numer in equation

    def but(self,i): #do not forgot in when type num after = (re)
        if len(self.c) < 17:
            if self.eq == "True":
                self.s = ""
                self.c = ""
                self.labelupResult.setText(self.s)
                self.labelResult.setText(self.c)
                self.eq = "False"
            if i == ".":
                if "." not in self.c:
                    self.c += str(i)
                    self.labelResult.setText(self.c)
            elif "+" not in self.s and "-" not in self.s and "*" not in self.s and "/" not in self.s:
                self.c += str(i)
                self.labelResult.setText(self.c)
            else:
                if self.s[-1] == "+" or self.s[-1] == "-" or self.s[-1] == "*" or self.s[-1] == "/":
                    if self.num2 == "False":
                        self.c = str(i)
                        self.labelResult.setText(self.c)
                        self.num2 = "True"
                    else:
                        self.c += str(i)
                        self.labelResult.setText(self.c)
                else:
                    self.c += str(i)
                    self.labelResult.setText(self.c)
        else:
            self.labelResult.setText("Can not type more")
            self.c = self.c[:16]
        
    def sign(self,i): #check change sign
        if self.c != "" or self.s != "":
            if self.num2 == "True":
                self.equal()
                self.s = self.c + str(i)
                self.labelupResult.setText(self.s)
                self.eq = "False"
                self.num2 = "False"
            elif self.eq == "True":
                self.s = self.c + str(i)
                self.labelupResult.setText(self.s)
                self.eq = "False"
            
            elif self.num2 == "False":
                self.s = self.c + str(i)
                self.labelupResult.setText(self.s)
            else:
                self.equal
                self.s = self.c + str(i)
                self.labelupResult.setText(self.s)
                self.num2 = "False"
        self.labelResult.setText(self.c)

    def equal(self):
        if "+" in self.s:
            a = self.s
            b = self.c
            self.s = self.s[:-1]
            c = (float(self.s) + float(self.c))
            if c % 1 == 0:
                self.c = str(int(float(self.s) + float(self.c)))
            else:
                self.c = str(float(self.s) + float(self.c))

            self.s = a + b
            self.labelupResult.setText(self.s)
            self.labelResult.setText(self.c)
        elif "-" in self.s:
            a = self.s
            b = self.c
            self.s = self.s[:-1]
            c = (float(self.s) - float(self.c))
            if c % 1 == 0:
                self.c = str(int(float(self.s) - float(self.c)))
            else:
                self.c = str(float(self.s) - float(self.c))
            self.s = a + b
            self.labelupResult.setText(self.s)
            self.labelResult.setText(self.c)
        elif "*" in self.s:
            a = self.s
            b = self.c
            self.s = self.s[:-1]
            c = (float(self.s) * float(self.c))
            if c % 1 == 0:
                self.c = str(int(float(self.s) * float(self.c)))
            else:
                self.c = str(float(self.s) * float(self.c))
            self.s = a + b
            self.labelupResult.setText(self.s)
            self.labelResult.setText(self.c)
        elif "/" in self.s:
            a = self.s
            b = self.c
            self.s = self.s[:-1]
            c = (float(self.s) / float(self.c))
            if c % 1 == 0:
                self.c = str(int(float(self.s) / float(self.c)))
            else:
                self.c = str(float(self.s) / float(self.c))
            self.s = a + b
            self.labelupResult.setText(self.s)
            self.labelResult.setText(self.c)
        self.eq = "True"
        self.num2 = "False"

    def cbut(self):
        self.s = ""
        self.c = ""
        self.labelResult.setText(self.c)
        self.labelupResult.setText(self.s)
    def cebut(self):
        if self.eq == "True":
            self.cbut
        else:
            self.c =""
            self.labelResult.setText(self.c)



                
            


#have to do more about function of (C) and (CE)
#Check function on window again


            
            
        
    

app = QApplication([])
myWindow = MyWindow()
myWindow.show()

app.exec()
