# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface/add_event.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_E(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.date = QtWidgets.QDateEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.date.setFont(font)
        self.date.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.date.setObjectName("date")
        self.gridLayout.addWidget(self.date, 0, 0, 1, 1)
        self.paints = QtWidgets.QComboBox(Dialog)
        self.paints.setObjectName("paints")
        self.gridLayout.addWidget(self.paints, 0, 1, 1, 1)
        self.text = QtWidgets.QTextEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text.setFont(font)
        self.text.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text.setObjectName("text")
        self.gridLayout.addWidget(self.text, 2, 0, 1, 2)
        self.add_btn = QtWidgets.QPushButton(Dialog)
        self.add_btn.setObjectName("add_btn")
        self.gridLayout.addWidget(self.add_btn, 3, 0, 1, 2)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Посещение"))
        self.add_btn.setText(_translate("Dialog", "Добавить"))
        self.label.setText(_translate("Dialog", "Примечания"))
