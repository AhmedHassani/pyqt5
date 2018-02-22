from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from tkinter.messagebox import *
import sys

app= QApplication(sys.argv)

window = QWidget()
window.setToolTip("make Button & TollTab")
window.resize(400,500)
window.setWindowTitle("make Button !")
btn=QPushButton("mybuton",window)
btn.setGeometry(50,50,50,50)
btn.clicked.connect(exit)
btn.setToolTip('exit')
window.show()

app.exec_()



