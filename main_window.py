# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 600)
        font = QtGui.QFont()
        font.setPointSize(11)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/Renamer.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 601, 601))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.listWidget = QtWidgets.QListWidget(self.page)
        self.listWidget.setGeometry(QtCore.QRect(10, 100, 401, 461))
        self.listWidget.setObjectName("listWidget")
        self.groupBox = QtWidgets.QGroupBox(self.page)
        self.groupBox.setGeometry(QtCore.QRect(420, 10, 171, 171))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 20, 71, 25))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/folder-plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 50, 71, 23))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/file-addition-one.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(90, 20, 81, 21))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 80, 71, 23))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/arrow-up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(90, 80, 75, 23))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/arrow-down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 110, 151, 23))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icon/delete-key.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon5)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 140, 151, 23))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/icon/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon6)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_9.setGeometry(QtCore.QRect(90, 50, 75, 23))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/icon/return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon7)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(514, 570, 81, 23))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/icon/check-correct.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon8)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 570, 81, 23))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icon/icon/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon9)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setGeometry(QtCore.QRect(12, 570, 401, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(self.page)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 401, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 20, 81, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 50, 331, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_10.setGeometry(QtCore.QRect(350, 48, 41, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_11.setGeometry(QtCore.QRect(350, 20, 41, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(100, 23, 81, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3.setGeometry(QtCore.QRect(190, 23, 131, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.page)
        self.groupBox_3.setGeometry(QtCore.QRect(420, 200, 171, 361))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.groupBox_3)
        self.stackedWidget_2.setGeometry(QtCore.QRect(10, 20, 151, 331))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.comboBox = QtWidgets.QComboBox(self.page)
        self.comboBox.setGeometry(QtCore.QRect(430, 190, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.tableWidget = QtWidgets.QTableWidget(self.page_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 581, 541))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(13, 570, 411, 20))
        self.label.setObjectName("label")
        self.pushButton_12 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_12.setGeometry(QtCore.QRect(510, 570, 75, 23))
        self.pushButton_12.setIcon(icon8)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_13.setGeometry(QtCore.QRect(430, 570, 75, 23))
        self.pushButton_13.setIcon(icon7)
        self.pushButton_13.setObjectName("pushButton_13")
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Renamer"))
        self.groupBox.setTitle(_translate("Form", "基本"))
        self.pushButton_3.setText(_translate("Form", "文件夹"))
        self.pushButton_4.setText(_translate("Form", "文件"))
        self.checkBox.setText(_translate("Form", "子文件夹"))
        self.pushButton_5.setText(_translate("Form", "上移"))
        self.pushButton_6.setText(_translate("Form", "下移"))
        self.pushButton_7.setText(_translate("Form", "从列表中删除"))
        self.pushButton_8.setText(_translate("Form", "清空列表"))
        self.pushButton_9.setText(_translate("Form", "原名称"))
        self.pushButton.setText(_translate("Form", "确认"))
        self.pushButton_2.setText(_translate("Form", "撤销"))
        self.groupBox_2.setTitle(_translate("Form", "筛选"))
        self.comboBox_2.setItemText(0, _translate("Form", "仅名称"))
        self.comboBox_2.setItemText(1, _translate("Form", "仅后缀"))
        self.comboBox_2.setItemText(2, _translate("Form", "名称后缀"))
        self.pushButton_10.setText(_translate("Form", "筛选"))
        self.pushButton_11.setText(_translate("Form", "复原"))
        self.checkBox_2.setText(_translate("Form", "启用正则"))
        self.checkBox_3.setText(_translate("Form", "保留已选择的项"))
        self.label.setText(_translate("Form", "确认重命名？"))
        self.pushButton_12.setText(_translate("Form", "确认"))
        self.pushButton_13.setText(_translate("Form", "取消"))
import icons_rc
