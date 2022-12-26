# -*- coding:utf-8 -*-
# AUTHOR: SUN
from Wapi.single_window import Ui_Form
from PyQt5 import QtWidgets, QtCore
from filelist import FileListItem


class main(Ui_Form, QtWidgets.QMainWindow):
    name = QtCore.pyqtSignal(object)

    def __init__(self, item: FileListItem, wightitem: QtWidgets.QListWidgetItem):
        super(main, self).__init__()
        self.setupUi(self)
        self.item = item
        self.wightitem = wightitem
        self.textEdit.setText(item.name)
        self.lineEdit.setText(item.suffix)
        self.pushButton.clicked.connect(self.confirm)

    def confirm(self):
        self.wightitem.setText(self.textEdit.toPlainText()+self.lineEdit.text())
        self.item.name = self.textEdit.toPlainText()
        self.item.suffix = self.lineEdit.text()
        self.close()


if __name__ == '__main__':
    pass
