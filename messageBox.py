from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

app= QApplication(sys.argv)

window = QWidget()
window.resize(400,500)
window.setWindowTitle("messgebox !")
rsulit = QMessageBox.question(window,"qisetion","are fmale ",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
#داله (question )تاخذ عده متغيؤلت منها وجت التى يشتغل بها و العنوان و النص
if rsulit == QMessageBox.Yes:
    print("Yes")
if rsulit == QMessageBox.No:
    app.exec_()
    print("No")

#rsulit = QMessageBox.about(window,"qisetion","are fmale ")
#rsulit = QMessageBox.warning(window, "qisetion", "are fmale ")



window.show()
app.exec_()