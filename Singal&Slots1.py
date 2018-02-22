from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
app = QApplication(sys.argv)
window = QWidget()


lcd = QLCDNumber(window)

lcd.move(100,100)
lcd.display(0)

ls =QSlider(window)
ls.move(200,80)

ls.valueChanged.connect(lcd.display)

window.show()

app.exec_()