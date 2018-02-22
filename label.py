from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

app= QApplication(sys.argv)

window = QWidget()
window.resize(400,500)
window.setWindowTitle("label")
title=QLabel(window,text="<H1>------Login------</H1>")
title.move(150,0)
le=QLabel(window,text="<H5>Password</H5>")
l=QLabel(window,text="<h5>Username</h5>")
username=QLineEdit(window)
username.setPlaceholderText("enter you username")
password=QLineEdit(window)
password.setPlaceholderText("Enter You Password")
password.setEchoMode(password.Password)
l.move(80,100)
username.move(140,97)
le.move(80,130)
password.move(140,127)
window.show()
app.exec_()