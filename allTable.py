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
        Dialog.resize(1180, 735)
        Dialog.setMinimumSize(QtCore.QSize(1000, 0))
        Dialog.setMaximumSize(QtCore.QSize(1180, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setMaximumSize(QtCore.QSize(140, 16777215))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setMaximumSize(QtCore.QSize(140, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ageTable = QtWidgets.QTableWidget(self.widget)
        self.ageTable.setObjectName("ageTable")
        self.ageTable.setColumnCount(0)
        self.ageTable.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.ageTable)
        self.nameTable = QtWidgets.QTableWidget(self.widget)
        self.nameTable.setObjectName("nameTable")
        self.nameTable.setColumnCount(0)
        self.nameTable.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.nameTable)
        self.nationTable = QtWidgets.QTableWidget(self.widget)
        self.nationTable.setObjectName("nationTable")
        self.nationTable.setColumnCount(0)
        self.nationTable.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.nationTable)
        self.univerTable = QtWidgets.QTableWidget(self.widget)
        self.univerTable.setObjectName("univerTable")
        self.univerTable.setColumnCount(0)
        self.univerTable.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.univerTable)
        self.schoolTable = QtWidgets.QTableWidget(self.widget)
        self.schoolTable.setObjectName("schoolTable")
        self.schoolTable.setColumnCount(0)
        self.schoolTable.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.schoolTable)
        self.operandTable = QtWidgets.QTableWidget(self.widget)
        self.operandTable.setMinimumSize(QtCore.QSize(360, 0))
        self.operandTable.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.operandTable.setObjectName("operandTable")
        self.operandTable.setColumnCount(0)
        self.operandTable.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.operandTable)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "AGE"))
        self.label_6.setText(_translate("Dialog", "NAME"))
        self.label_5.setText(_translate("Dialog", "NATION"))
        self.label_4.setText(_translate("Dialog", "UNIVER"))
        self.label_3.setText(_translate("Dialog", "SCHOOL"))
        self.label.setText(_translate("Dialog", "OPERAND"))
