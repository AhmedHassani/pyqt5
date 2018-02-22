from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


app = QApplication(sys.argv)
list = QListView()
list.setWindowTitle('Example List')
list.setMinimumSize(600, 400)
model = QStandardItemModel(list)
foods = [
    'Cookie dough', # Must be store-bought
    'Hummus', # Must be homemade
    'Spaghetti', # Must be saucy
    'Dal makhani', # Must be spicy
    'Chocolate whipped cream' # Must be plentiful
]

for food in foods:
    # create an item with a caption
    item = QStandardItem(food)

    # add a checkbox to it
    item.setCheckable(True)

    # Add the item to the model
    model.appendRow(item)

    list.setModel(model)
list.show()
app.exec_()