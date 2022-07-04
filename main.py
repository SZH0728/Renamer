# -*- coding:utf-8 -*-
# AUTHOR: SUN

from main_window import Ui_Form
from PyQt5 import QtWidgets, QtCore, QtGui
from filelist import FileList
from fileget import *


class Ui(Ui_Form, QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        self.filelist = FileList()

    def setupUi(self, form):
        super(Ui, self).setupUi(form)
        self.comboBox.addItems(['整个列表', '选中范围'])
        self.comboBox_2.addItems(['正序', '倒序'])
        self.comboBox_3.addItems(['名称+序号', '仅序号', '自定义'])
        self.checkBox.clicked.connect(self.replace_delelate)
        self.pushButton_6.clicked.connect(self.add_files)

    def closeEvent(self, a0: QtGui.QCloseEvent):
        """关闭窗口时执行"""
        self.close()  # 必要代码

    def replace_delelate(self):
        """替换对话框与删除对话框的切换"""
        if self.checkBox.isChecked():
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.stackedWidget.setCurrentIndex(0)

    def add_files(self):
        """向列表中添加文件"""
        path = QtWidgets.QFileDialog.getExistingDirectory(self, '请选择一个目录')
        if self.checkBox_3.isChecked():
            files = get_files_deep(path)
        else:
            files = get_files(path)
        files = self.filelist.add(files)
        for key, value in files.items():
            item = QtWidgets.QListWidgetItem()
            item.setText(value.name)
            item.setWhatsThis(key)
            item.setToolTip(value.origin)
            self.listWidget.addItem(item)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Ui()
    MainWindow.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
    MainWindow.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
