from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys

 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.acceptDrops()
        self.setWindowTitle("Image")
 
        self.setGeometry(50, 50, 1300, 700)
 
        self.label = QLabel(self)
         
        
        self.pixmap = QPixmap('HowToPlay.jpg')
 
        self.label.setPixmap(self.pixmap)

        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())
#         self.show()
 
# # create pyqt5 app
# App = QApplication(sys.argv)
 
# # create the instance of our Window
# window = Window()
 
# # start the app
# sys.exit(App.exec())