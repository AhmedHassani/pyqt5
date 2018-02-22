from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


app = QApplication(sys.argv)
window = QWidget()
window.resize(500,600)

link_but = QCommandLinkButton(window)
link_but.resize(40,40)
def A():
    window.setEnabled(0)
    return

link_but.clicked.connect(A)
but=QPushButton(window)
but.resize(70,40)
but.move(80,80)
but.setText("button")







window.show()
app.exec_()
