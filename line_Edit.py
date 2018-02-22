from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

app= QApplication(sys.argv)

window = QWidget()
window.resize(400,500)
window.setWindowTitle("EidtText !")
editText = QLineEdit(window) # انشاء حقل جديد
editText.resize(120,25)
editText.move(130,120)
editText.setPlaceholderText(" Enter You Email") #نص توضيحي
editText.setEchoMode(editText.Password) #اختيار نوعيه الحقل
editText.setText("H") #اعطاء قيمه النص
val = editText.text()   #جلب قيمه النص
print(val)
window.show()

app.exec_()