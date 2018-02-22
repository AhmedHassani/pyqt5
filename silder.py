from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

app= QApplication(sys.argv)

window = QWidget()
window.resize(400,500)
window.setWindowTitle("silder !")
silder = QSlider(Qt.Horizontal,window)
silder.move(100,20)


window.show()
app.exec_()