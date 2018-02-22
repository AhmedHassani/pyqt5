from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
app = QApplication(sys.argv)
window = QWidget()
window.resize(500,500)
imge =  QPixmap('b.png').scaled(150,160)
leb=QLabel(window)
leb.setPixmap(imge)

window.show()
app.exec_()