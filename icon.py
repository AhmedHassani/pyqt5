from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from tkinter.messagebox import *
import sys

app= QApplication(sys.argv)

window = QWidget()
window.resize(400,500)
window.setWindowTitle("make Button !")
window.setWindowIcon(QIcon("b.png"))
window.show()
app.exec_()