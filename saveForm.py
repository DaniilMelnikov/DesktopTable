# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './saveForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(529, 355)
        Dialog.setMaximumSize(QtCore.QSize(529, 355))
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.comboWidget = QtWidgets.QWidget(Dialog)
        self.comboWidget.setMinimumSize(QtCore.QSize(250, 50))
        self.comboWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.comboWidget.setObjectName("comboWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.comboWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.comboWidget)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(250, 50))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "?????????????????? ????????????"))
        self.label.setText(_translate("Dialog", "???????? ?????????? ?????????????? ???????????????????? -------->"))
        self.label_2.setText(_translate("Dialog", "?????????? ???? ?????????????? 1 ?????????????? ??????????????????"))
        self.label_3.setText(_translate("Dialog", "?? ???????? 2 ?????????????? ????????????????"))
        self.label_4.setText(_translate("Dialog", "???????? ?????????????????? ??????????????????\n"
"?????? ???????????? ????????????????"))
