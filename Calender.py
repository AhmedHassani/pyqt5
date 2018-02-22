from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

app= QApplication(sys.argv)

window = QWidget()
window.resize(400,500)
window.setWindowTitle("font_dialog !")
time=QCalendarWidget(window)
time.resize(200,200)
lib=QLabel(window)
data=time.selectedDate()
lib.setText(data.toString())
lib.move(100,500)
window.show()
app.exec_()