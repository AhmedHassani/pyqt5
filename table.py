from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

app= QApplication(sys.argv)

table=QTableWidget()

table.setWindowTitle("Teble")
table.resize(500,500)
table.setRowCount(3)
table.setColumnCount(4)
table.setItem(0,0,QTableWidgetItem("ahmed"))
table.setItem(0,1,QTableWidgetItem("ahmed"))
table.setItem(0,2,QTableWidgetItem("ahmed"))
table.setItem(0,3,QTableWidgetItem("ahmed"))
table.setHorizontalHeaderLabels(("name,id,cost,data").split(","))
table.setVerticalHeaderLabels(("V1-V2-V3-V4").split("-"))


table.show()
app.exec_()