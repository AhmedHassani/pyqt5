# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(571, 478)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(1500, 1400))
        self.nameadmin = QtWidgets.QLabel(Form)
        self.nameadmin.setGeometry(QtCore.QRect(0, 0, 47, 13))
        self.nameadmin.setObjectName("nameadmin")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.nameadmin.setText(_translate("Form", "TextLabel"))

