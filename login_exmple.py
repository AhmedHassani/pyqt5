from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


app = QApplication(sys.argv)

window = QWidget()
window.resize(400,500)
title = QLabel(window)

title.setText("<h4>اسم المستخدم </h4>")
title.setMargin(14)
title.move(150,0)

lienLayout=QHBoxLayout(window)
lienLayout2=QHBoxLayout(window)

vrlayout=QVBoxLayout(window)

vrlayout.addLayout(lienLayout)
vrlayout.addLayout(lienLayout2)

email = QLineEdit(window)
email.setPlaceholderText("ادخال اسم المستخدم !")
lienLayout.addWidget(email)
lienLayout.addWidget(title)
password = QLineEdit(window)

password.setPlaceholderText(" ادخال كلمة المرور")
password.setEchoMode(password.Password)
lienLayout.addWidget(password)





window.show()
app.exec_()
