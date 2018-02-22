from PyQt5.QtGui import *
from PyQt5.QtWidgets import*
import sys

app = QApplication(sys.argv)
tabs = QTabWidget()
tabs.resize(600,600)
tab1 = QWidget()
tab2 = QWidget()

tabs.addTab(tab1,"tab1")
tabs.addTab(tab2,"tab2")

# use tab one
leb=QLabel(tab1)
leb.setText("Hello Iam Tab One ")

# use tab two
vr=QVBoxLayout(tab2)
but1=QPushButton("login")

Email=QLineEdit(tab2)
Email.setPlaceholderText("Enter You Email !")
Password=QLineEdit(tab2)
Password.setPlaceholderText("Enter You Password !")
Password.setEchoMode(Password.Password)
#get Text from email and pasword onclick on butoon
def print_():
    var_email = Email.text()
    var_pass =Password.text()
    print("Email : "+var_email+"   "+"password :"+var_pass)

but1.clicked.connect(print_)

vr.addWidget(Email)
vr.addWidget(Password)
vr.addWidget(but1)
tabs.show()





app.exec_()