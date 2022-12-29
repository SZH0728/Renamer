# -*- coding:utf-8 -*-
# AUTHOR: SUN

from os import listdir, walk
from os.path import isdir, join, split
from re import match

from PyQt5 import QtCore, QtGui, QtWidgets

from Wapi import single
from filelist import FileList, ini
from function import config
from main_window import Ui_Form

__verson__ = '1.1.1'

# pyinstaller -D -w -i Renamer.ico main.py


class main(Ui_Form, QtWidgets.QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.filelist = FileList()
        self.window = ''
        self.functions = []
        self.config = ini()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.config.config.write()
        self.close()

    def setupUi(self, form):
        super(main, self).setupUi(form)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget.currentItemChanged.connect(self.item_click)
        self.listWidget.doubleClicked.connect(self.change_single_name)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['路径', '原名称', '目标名称'])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.lineEdit.setPlaceholderText('文件位置会出现在这里')
        self.lineEdit.textChanged.connect(self.item_click)
        self.lineEdit_2.textChanged.connect(self.context_change)
        self.pushButton.clicked.connect(self.confirm)
        self.pushButton_2.clicked.connect(self.roll_back)
        self.pushButton_3.clicked.connect(self.adddir)
        self.pushButton_4.clicked.connect(self.addfile)
        self.pushButton_5.clicked.connect(self.move_up)
        self.pushButton_6.clicked.connect(self.move_down)
        self.pushButton_7.clicked.connect(self.delete)
        self.pushButton_8.clicked.connect(self.clear)
        self.pushButton_9.clicked.connect(self.present_origin)
        self.pushButton_10.clicked.connect(self.filtrate)
        self.pushButton_11.clicked.connect(self.rebound)
        self.pushButton_12.clicked.connect(self.rename)
        self.pushButton_13.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.comboBox.currentIndexChanged.connect(self.function_change)
        self.comboBox_2.currentIndexChanged.connect(self.way_change)
        self.checkBox_2.clicked.connect(self.re_change)
        self.checkBox_3.clicked.connect(self.save_change)

        self.comboBox_2.setCurrentIndex(int(self.config.config['general']['filtrate']['way']))
        self.checkBox_2.setChecked(bool(self.config.config['general']['filtrate']['re']))
        self.checkBox_3.setChecked(bool(self.config.config['general']['filtrate']['save']))
        self.lineEdit_2.setText(self.config.config['general']['filtrate']['context'])

        for key, value in config.functions.items():
            self.comboBox.addItem(key)
            wight = QtWidgets.QWidget(self.stackedWidget_2)
            wight.setObjectName(key)
            value = value(self)
            value.setupUi(wight)
            self.functions.append(value)
            self.stackedWidget_2.addWidget(wight)

    def adddir(self):
        self.filelist.save()
        self.present_origin(True)
        path = QtWidgets.QFileDialog.getExistingDirectory(self, '请选择一个目录')
        if path != '':
            if self.checkBox.isChecked():
                files = []
                for paths, dirs, file in walk(path):
                    for i in file:
                        files.append(join(paths, i))
            else:
                files = []
                for i in listdir(path):
                    i = join(path, i)
                    if not isdir(i):
                        files.append(i)
            exist = []
            for i in self.filelist.Id_Item.values():
                exist.append(i.id)
            exist = set(exist)
            files = set(files)
            files = files.difference(exist)
            files = list(files)
            files.sort()
            for i in list(files):
                if '$' in i:
                    continue
                file = self.filelist.new(i)
                item = QtWidgets.QListWidgetItem()
                item.setText(file.name + file.suffix)
                item.setToolTip(file.origin)
                item.setWhatsThis(file.id)
                self.listWidget.addItem(item)

    def addfile(self):
        self.filelist.save()
        self.present_origin(True)
        files = QtWidgets.QFileDialog.getOpenFileNames(self, '选择多个文件')[0]
        exist = []
        for i in self.filelist.Id_Item.values():
            exist.append(i.id)
        exist = set(exist)
        files = set(files)
        files = files.difference(exist)
        for i in list(files):
            if '$' in i:
                continue
            file = self.filelist.new(i)
            item = QtWidgets.QListWidgetItem()
            item.setText(file.name + file.suffix)
            item.setToolTip(file.origin)
            item.setWhatsThis(file.id)
            self.listWidget.addItem(item)

    def move_up(self):
        """上移一格"""
        try:
            for i in range(self.listWidget.count()):
                item = self.listWidget.item(i)
                if item.isSelected():
                    if i == 0:
                        raise IndexError
                    self.listWidget.takeItem(i)
                    self.listWidget.insertItem(i - 1, item)
                    self.listWidget.setCurrentItem(item)
        except IndexError:
            QtWidgets.QMessageBox.critical(self, '错误', '已经到头了！')

    def move_down(self):
        """下移一格"""
        num = self.listWidget.count()
        li = list(range(num))
        li.reverse()
        try:
            for i in li:
                item = self.listWidget.item(i)
                if item.isSelected():
                    if i == num - 1:
                        raise IndexError
                    self.listWidget.takeItem(i)
                    self.listWidget.insertItem(i + 1, item)
                    self.listWidget.setCurrentItem(item)
        except IndexError:
            QtWidgets.QMessageBox.critical(self, '错误', '已经到底了！')

    def delete(self):
        self.filelist.save()
        num = 0
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i - num)
            if item.isSelected():
                self.filelist.delete(item.whatsThis())
                self.listWidget.takeItem(i - num)
                num += 1

    def clear(self):
        self.listWidget.clear()
        self.filelist.save()
        self.filelist.clear()
        self.pushButton_9.setText('原名称')
        self.lineEdit.clear()

    def change_single_name(self):
        self.filelist.save()
        wightitem = self.listWidget.currentItem()
        item = self.filelist.Id_Item[wightitem.whatsThis()]
        self.window = single.main(item, wightitem)
        self.window.show()

    def item_click(self):
        item = self.listWidget.currentItem()
        if item is not None:
            text = self.filelist.Id_Origin[item.whatsThis()]
            text = text.replace('\\', '/')
            text = text.replace('//', '/')
            self.lineEdit.setText(text)

    def present_origin(self, origin=False):
        if origin:
            if self.pushButton_9.text() == '现名称':
                for i in range(self.listWidget.count()):
                    item = self.listWidget.item(i)
                    name = self.filelist.Id_Item[item.whatsThis()]
                    name = name.name + name.suffix
                    item.setText(name)
                self.pushButton_9.setText('原名称')
        else:
            if self.pushButton_9.text() == '原名称':
                for i in range(self.listWidget.count()):
                    item = self.listWidget.item(i)
                    name = split(self.filelist.Id_Origin[item.whatsThis()])[1]
                    item.setText(name)
                self.pushButton_9.setText('现名称')
            elif self.pushButton_9.text() == '现名称':
                for i in range(self.listWidget.count()):
                    item = self.listWidget.item(i)
                    name = self.filelist.Id_Item[item.whatsThis()]
                    name = name.name + name.suffix
                    item.setText(name)
                self.pushButton_9.setText('原名称')

    def roll_back(self):
        self.listWidget.clear()
        self.filelist.rollback()
        for i in self.filelist.Id_Item.values():
            item = QtWidgets.QListWidgetItem()
            item.setText(i.name + i.suffix)
            item.setToolTip(i.origin)
            item.setWhatsThis(i.id)
            self.listWidget.addItem(item)
        self.lineEdit.clear()

    def confirm(self):
        self.tableWidget.setRowCount(len(self.filelist.Id_Item))
        for index, i in enumerate(list(self.filelist.Id_Item.values())):
            text1 = i.path
            text2 = i.name + i.suffix
            text3 = split(i.origin)[1]
            if '\\' in text1:
                text1 = text1.replace('\\', '/')
            if '//' in text1:
                text1 = text1.replace('//', '/')
            item1 = QtWidgets.QTableWidgetItem(text1)
            item1.setToolTip(text1)
            item2 = QtWidgets.QTableWidgetItem(text3)
            item2.setToolTip(text3)
            item3 = QtWidgets.QTableWidgetItem(text2)
            item3.setToolTip(text2)
            self.tableWidget.setItem(index, 0, item1)
            self.tableWidget.setItem(index, 1, item2)
            self.tableWidget.setItem(index, 2, item3)
        self.stackedWidget.setCurrentIndex(1)

    def rebound(self):
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            item.setHidden(False)

    def filtrate(self):
        type_ = self.comboBox_2.currentIndex()
        re = self.checkBox_2.isChecked()
        select = self.checkBox_3.isChecked()
        way = self.lineEdit_2.text()
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            if item.isSelected() and select:
                continue
            file = self.filelist.Id_Item[item.whatsThis()]
            text = ''
            if type_ == 0:
                text = file.name
            elif type_ == 1:
                text = file.suffix
            elif type_ == 2:
                text = file.name + file.suffix
            if re:
                if match(way, text) is None:
                    item.setHidden(True)
            else:
                if way not in text:
                    item.setHidden(True)

    def rename(self):
        self.filelist.rename()
        self.stackedWidget.setCurrentIndex(0)

    def function_change(self):
        self.stackedWidget_2.setCurrentIndex(self.comboBox.currentIndex())

    def way_change(self):
        self.config.config['general']['filtrate']['way'] = self.comboBox_2.currentIndex()

    def re_change(self):
        if self.checkBox_2.isChecked():
            self.config.config['general']['filtrate']['re'] = '1'
        else:
            self.config.config['general']['filtrate']['re'] = ''

    def save_change(self):
        if self.checkBox_3.isChecked():
            self.config.config['general']['filtrate']['save'] = '1'
        else:
            self.config.config['general']['filtrate']['save'] = ''

    def context_change(self):
        self.config.config['general']['filtrate']['context'] = self.lineEdit_2.text()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = main()
    ui.setupUi(ui)
    ui.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
    ui.show()
    sys.exit(app.exec_())
