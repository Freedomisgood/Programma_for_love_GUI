# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_time.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(293, 169)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(50, 40, 194, 22))
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 4, 19), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit.setTime(QtCore.QTime(0, 0, 0))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 100, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 100, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.dateTimeEdit.setDisplayFormat(_translate("Dialog", "yyyy/M/d HH:mm:ss"))
        self.pushButton.setText(_translate("Dialog", "设置"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))

