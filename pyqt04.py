from PyQt5.QtWidgets import *
from my_widget_ui_01 import Ui_Form

class MyWindow(Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_add.clicked.connect(self.action_add)

    def action_add(self):
        x = int(self.lineEdit_x.text())
        y = int(self.lineEdit_y.text())
        z = x+y
        self.label_result.setText(str(z))
    
        
def main():
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()

main()
