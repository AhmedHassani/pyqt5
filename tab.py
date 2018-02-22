from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
tabs = QTabWidget()

tabs.resize(500,500)
tab1 = QWidget()
tab2 = QWidget()
tab3=QWidget()
def addfun():
    tabs.addTab(tab3,"Hello")
def a():
    p=tabs.tabPosition()
    tabs.removeTab(p)
tabs.addTab(tab1,"Test1")
tabs.addTab(tab2,"Test2")
tabs.setTabsClosable(True)
tabs.tabCloseRequested.connect(a)
but=QPushButton(tab2)
but.setText("add")
but.clicked.connect(addfun)
tabs.show()


app.exec_()