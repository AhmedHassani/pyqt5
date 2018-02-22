from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

app= QApplication(sys.argv)

window = QWidget()
window.resize(400,500)
window.setWindowTitle("porgressbar !")

porg=QProgressBar(window)
#استعدعاء كلاس البروسجير واخذ نسخه منه
porg.resize(300,20)
#اعطاء حجم طول و العرض
porg.move(100,100)
# الاحدائي
porg.setValue(78)
#قيمه البروسيجر
porg.setAlignment(Qt.AlignCenter)
#جعل قيمه البروسيجر داخله
window.show()
app.exec_()