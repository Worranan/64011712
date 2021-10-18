from PyQt5.QtWidgets import *
from listwidget import Ui_Form

class MyWindow(Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_add.clicked.connect(self.action_add)
        self.pushButton_remove.clicked.connect(self.action_remove)
        self.listWidget.itemClicked.connect(self.action_select)

    def action_add(self):
        self.listWidget.addItem(self.lineEdit.text())
        
    def action_remove(self):
        self.listWidget.takeItem(self.listWidget.currentRow())

    def action_select(self):
        self.label.setText('You are selecting ' + self.listWidget.currentItem().text())
        
    
def main():
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()

main()
