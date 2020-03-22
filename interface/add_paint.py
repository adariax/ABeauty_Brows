# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface/add_paint.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_P(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 75)
        Dialog.setMinimumSize(QtCore.QSize(400, 75))
        Dialog.setMaximumSize(QtCore.QSize(400, 75))
        self.text = QtWidgets.QLineEdit(Dialog)
        self.text.setGeometry(QtCore.QRect(10, 10, 301, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.text.setFont(font)
        self.text.setObjectName("text")
        self.acccept = QtWidgets.QPushButton(Dialog)
        self.acccept.setGeometry(QtCore.QRect(320, 10, 71, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.acccept.setFont(font)
        self.acccept.setObjectName("acccept")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Добавить"))
        self.text.setPlaceholderText(_translate("Dialog", "Название"))
        self.acccept.setText(_translate("Dialog", "ОК"))
