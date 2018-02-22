from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

app= QApplication(sys.argv)

window = QWidget()
window.resize(400,500)
window.setWindowTitle("Radio Button")
rd1 = QRadioButton(window,text="Android")
rd1.move(80,100)
rd2 = QRadioButton(window,text="Ios")
rd2.move(80,80)
rd2.setChecked(True)
t=rd2.isChecked()
print(t)

window.show()
app.exec_()