from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

app= QApplication(sys.argv)

window = QWidget()
window.resize(400,500)
window.setWindowTitle("Combobox !")
cm = QComboBox(window)
cm.move(100,100)
cm.addItem("Ahmed")
cm.addItem("Ali")
cm.addItem("Hussen")
cm.addItem("Hassan")
cm.addItem("Amjed")
cm_text=cm.itemText(1)
print(cm_text)
################################
cn = QComboBox(window)
cn.move(200,200)
cn.addItems(["C++","Java","Python"])
window.show()
app.exec_()