from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


app = QApplication(sys.argv)
window = QWidget()
window.resize(500,500)


def A():
   ls.setValue(10)



but = QPushButton("MyButton",window)
but.move(100,100)
but.clicked.connect(A)

ls=QSlider(window)

window.show()

app.exec_()