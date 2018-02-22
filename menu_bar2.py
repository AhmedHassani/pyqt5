from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

App=QApplication(sys.argv)
window=QMainWindow()
window.resize(500,500)
menuBar=window.menuBar()
file=menuBar.addMenu("File")
edit=menuBar.addMenu("Edit")
run=menuBar.addMenu('Run')
view=menuBar.addMenu('View')
#add action for fille :
save = QAction('Save')
exit_ = QAction(QIcon('b.png'),'Exit')
exit_.setShortcut('Ctrl+s')
exit_.triggered.connect(window.close)
save_grop=QMenu("Save as")
save_grop.addAction("jpg")
save_grop.addAction("png")
save_grop.addAction('psd')
file.addAction(save)
file.addMenu(save_grop)
file.addAction(exit_)
#add action for edit
undo_one=QAction("undo one ")
undo_all=QAction("undo all")
edit.addAction(undo_all)
edit.addAction(undo_one)
window.show()
App.exec_()