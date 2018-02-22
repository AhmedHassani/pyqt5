from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

app= QApplication(sys.argv)

window = QWidget()
window.resize(400,500)
window.setWindowTitle("check Box")
choose1 = QCheckBox(window,text="Fmael")
choose3 = QCheckBox(window,text="Fmael")
choose1.move(100,100)
choose1.setChecked(True)
window.show()
app.exec_()