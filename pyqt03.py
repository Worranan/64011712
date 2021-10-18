from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()

layout1 = QVBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()

layout1.addItem(layout2)
layout1.addItem(layout3)

layout2.addWidget(QLabel('Text 1'))
layout2.addWidget(QLabel('Text 2'))
layout2.addWidget(QLabel('Text 3'))

layout3.addWidget(QPushButton('Okay'))
layout3.addWidget(QPushButton('Cancel'))

window.setLayout(layout1)

window.show()
app.exec()
