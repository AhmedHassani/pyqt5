from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
app=QApplication(sys.argv)
window=QWidget()

ok_but=QPushButton(window,text="ok")
cansel_but=QPushButton(window,text="cansal")
#her=QHBoxLayout(window)
#her=QVBoxLayout(window)
her=QGridLayout(window)
her.setSpacing(30)
her.addWidget(ok_but,0,0)
her.addWidget(cansel_but,0,1)
window.show()


app.exec_()