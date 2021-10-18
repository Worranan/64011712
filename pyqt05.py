from PyQt5 import uic
from PyQt5.QtWidgets import *

myWidget = uic.loadUi('my_widget_ui_01.ui',QWidget)
print(myWidget)
app = QApplication([])
myWidget.show()
app.exec()
