# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'repl.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(171, 361)
        font = QtGui.QFont()
        font.setPointSize(11)
        Form.setFont(font)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 151, 161))
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 130, 51, 23))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(70, 134, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(30, 20, 111, 51))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 18, 16, 51))
        self.label.setMouseTracking(False)
        self.label.setStyleSheet("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 75, 20, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(False)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 80, 111, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 180, 151, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 140, 51, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(70, 144, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 40, 131, 91))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 131, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "替换"))
        self.pushButton.setText(_translate("Form", "预览"))
        self.checkBox.setText(_translate("Form", "使用正则"))
        self.label.setText(_translate("Form", "关键词"))
        self.label_2.setText(_translate("Form", "替换为"))
        self.groupBox_2.setTitle(_translate("Form", "删除"))
        self.pushButton_2.setText(_translate("Form", "预览"))
        self.checkBox_2.setText(_translate("Form", "使用正则"))
        self.label_3.setText(_translate("Form", "关  键  词"))
