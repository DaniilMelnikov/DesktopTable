# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './allTable.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1117, 711)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ageTable = QtWidgets.QTableWidget(Dialog)
        self.ageTable.setObjectName("ageTable")
        self.ageTable.setColumnCount(0)
        self.ageTable.setRowCount(0)
        self.horizontalLayout.addWidget(self.ageTable)
        self.nameTable = QtWidgets.QTableWidget(Dialog)
        self.nameTable.setObjectName("nameTable")
        self.nameTable.setColumnCount(0)
        self.nameTable.setRowCount(0)
        self.horizontalLayout.addWidget(self.nameTable)
        self.nationTable = QtWidgets.QTableWidget(Dialog)
        self.nationTable.setObjectName("nationTable")
        self.nationTable.setColumnCount(0)
        self.nationTable.setRowCount(0)
        self.horizontalLayout.addWidget(self.nationTable)
        self.univerTable = QtWidgets.QTableWidget(Dialog)
        self.univerTable.setObjectName("univerTable")
        self.univerTable.setColumnCount(0)
        self.univerTable.setRowCount(0)
        self.horizontalLayout.addWidget(self.univerTable)
        self.schoolTable = QtWidgets.QTableWidget(Dialog)
        self.schoolTable.setObjectName("schoolTable")
        self.schoolTable.setColumnCount(0)
        self.schoolTable.setRowCount(0)
        self.horizontalLayout.addWidget(self.schoolTable)
        self.operandTable = QtWidgets.QTableWidget(Dialog)
        self.operandTable.setObjectName("operandTable")
        self.operandTable.setColumnCount(0)
        self.operandTable.setRowCount(0)
        self.horizontalLayout.addWidget(self.operandTable)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
