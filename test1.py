from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

app=QApplication(sys.argv)

window=QMainWindow()
window.resize(500,500)
muine=window.menuBar()
file=muine.addMenu('File')
edit=muine.addMenu('Edit')
xcode=muine.addMenu('Xcode')
show=muine.addMenu('Show')
seting=muine.addMenu('Seting')

#Make action for Eidt !
save=QAction("Save")
exit=QAction("Exit")
save_as=QAction("Save AS")
file.addAction(save)
file.addAction(save_as)
file.addAction(exit)
#make action for edit !
undo_one=QAction("undo one ")
undo_all=QAction("undo all")
edit.addAction(undo_all)
edit.addAction(undo_one)

window.show()


app.exec_()