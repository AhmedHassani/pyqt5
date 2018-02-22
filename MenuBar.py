from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

app= QApplication(sys.argv)
window=QMainWindow()
window.resize(700,300)
mainu=window.menuBar()
file_m=mainu.addMenu('الملفات')
edit_m=mainu.addMenu('التعديل')
code_m=mainu.addMenu('الكود')
tools_m=mainu.addMenu('اللغات البرمجية')
#-------------------
Cpp =QAction('C++')
java=QAction('java')
php=QAction('Php')
Html=QAction('Html')

#--------------------
tools_m.addAction(Cpp)
tools_m.addAction(java)
tools_m.addAction(php)
tools_m.addAction(Html)
window.show()
app.exec_()