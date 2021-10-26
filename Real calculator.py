from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.resize(1000,1000)
        self.c = ""

        self.labelResult = QLabel(self)
        self.labelResult.setGeometry(25,25,(125*4)-25,100)
        self.labelResult.setFont(QFont("Times", 30))

        
        g = 10

        for i in range(0,3):
            for i2 in range(0,3):
                g -= 1
                self.button = QPushButton("{}".format(g),self)
                self.button.setGeometry(25+(125*i2),130+(125*i),100,100)
                self.button.setFont(QFont("Times",30))

                self.button.clicked.connect(lambda checked, g = g: self.but(g))
        
        #before last line
        self.button = QPushButton("0",self)
        self.button.setGeometry(25+(125*1),130+(125*3),100,100)
        self.button.setFont(QFont("Times",30))
        self.button.clicked.connect(lambda checked, g = 0:self.but(g))

        self.button = QPushButton("=",self)
        self.button.setGeometry(25+(125*0),130+(125*3),100,100)
        self.button.setFont(QFont("Times",30))
        self.button.clicked.connect(self.equal)

        self.button = QPushButton(".",self)
        self.button.setGeometry(25+(125*2),130+(125*3),100,100)
        self.button.setFont(QFont("Times",30))
        self.button.clicked.connect(lambda checked, g = ".":self.but(g))

        #last column
        self.button = QPushButton("/",self)
        self.button.setGeometry(25+(125*3),130+(125*0),100,100)
        self.button.setFont(QFont("Times",30))
        self.button.clicked.connect(lambda checked, g = "/":self.but(g))

        self.button = QPushButton("*",self)
        self.button.setGeometry(25+(125*3),130+(125*1),100,100)
        self.button.setFont(QFont("Times",30))
        self.button.clicked.connect(lambda checked, g = "*":self.but(g))

        self.button = QPushButton("-",self)
        self.button.setGeometry(25+(125*3),130+(125*2),100,100)
        self.button.setFont(QFont("Times",30))
        self.button.clicked.connect(lambda checked, g = "-":self.but(g))

        self.button = QPushButton("+",self)
        self.button.setGeometry(25+(125*3),130+(125*3),100,100)
        self.button.setFont(QFont("Times",30))
        self.button.clicked.connect(lambda checked, g = "+":self.but(g))

        #last row
        self.button = QPushButton("CE",self)
        self.button.setGeometry(25+(125*0),130+(125*4),100+125,100)
        self.button.setFont(QFont("Times",30))

        self.button = QPushButton("C",self)
        self.button.setGeometry(25+(125*2),130+(125*4),100+125,100)
        self.button.setFont(QFont("Times",30))

        self.eq = "Flase"

    def but(self,i):
        if i != "+" and i != "-" and i != "*" and i != "/" and i != ".":
            if self.eq == "True":
                self.c = str(i)
                self.eq = "Flase"
            else:
                self.c += str(i)
            self.labelResult.setText(self.c)
        else:
            if  self.c[-1] == "+" and self.c[-1] == "-" and self.c[-1] == "*" and self.c[-1] == "/":
                self.c = self.c[:len(self.c)-2] + str(i)
            if i == ".":
                if "." not in self.c:
                    self.c += str(i)
                    self.labelResult.setText(self.c)
            elif "+" in self.c or "-" in self.c or "*" or self.c or "/" or self.c:
                self.equal()
                self.c += i
                self.labelResult.setText(self.c)
            elif "+" not in self.c and "-" not in self.c and "*" not in self.c and "/" not in self.c:
                self.c += str(i)
                self.labelResult.setText(self.c)
            self.eq = "Flase"
            
    def equal(self):
        if "+" in self.c:
            f = self.c.split("+")
            self.c = str(float(f[0]) + float(f[1]))
            self.labelResult.setText(self.c)
        elif "-" in self.c:
            f = self.c.split("-")
            self.c = str(float(f[0]) - float(f[1]))
            self.labelResult.setText(self.c)
        elif "*" in self.c:
            f = self.c.split("*")
            self.c = str(float(f[0]) * float(f[1]))
            self.labelResult.setText(self.c)
        elif "/" in self.c:
            f = self.c.split("/")
            self.c = str(float(f[0]) / float(f[1]))
            self.labelResult.setText(self.c)
        self.eq = "True"


                
            


#have to do more about function of (C) and (CE)
#Check function on window again


            
            
        
    

app = QApplication([])
myWindow = MyWindow()
myWindow.show()

app.exec()
