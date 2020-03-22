# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 400)
        Form.setMinimumSize(QtCore.QSize(800, 400))
        Form.setMaximumSize(QtCore.QSize(1200, 400))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.change_mode = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.change_mode.sizePolicy().hasHeightForWidth())
        self.change_mode.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.change_mode.setFont(font)
        self.change_mode.setObjectName("change_mode")
        self.gridLayout.addWidget(self.change_mode, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.action_button = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.action_button.sizePolicy().hasHeightForWidth())
        self.action_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.action_button.setFont(font)
        self.action_button.setObjectName("action_button")
        self.gridLayout.addWidget(self.action_button, 1, 0, 1, 1)
        self.add_button = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 2, 0, 1, 1)
        self.table = QtWidgets.QTableWidget(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.table.setFont(font)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.gridLayout.addWidget(self.table, 0, 1, 5, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "a.beauty / brows"))
        self.change_mode.setText(_translate("Form", "Перейти"))
        self.label.setText(_translate("Form", "Информация о клиенте"))
        self.label_2.setText(_translate("Form", "Информация о краске"))
        self.action_button.setText(_translate("Form", "Удалить"))
        self.add_button.setText(_translate("Form", "Добавить"))
