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
        self.label.setText('本软件已开源于GitHub\n详情请访问 https://github.com/zhehao0728/Renamer')
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.comboBox.addItems(['整个列表', '选中范围'])
        self.comboBox_2.addItems(['正序', '倒序'])
        self.comboBox_3.addItems(['名称+序号', '仅序号', '自定义'])
        self.checkBox.clicked.connect(self.replace_delelate)
        self.pushButton_6.clicked.connect(self.add_files)
        self.listWidget.clicked.connect(self.list_click)
        self.listWidget.doubleClicked.connect(self.change_single_name)
        self.pushButton_7.clicked.connect(self.change_single_name)
        self.checkBox_4.clicked.connect(self.show_origin_name)
        self.pushButton_9.clicked.connect(self.move_up)
        self.pushButton_10.clicked.connect(self.move_down)
        self.pushButton_8.clicked.connect(self.delete)
        self.pushButton_11.clicked.connect(self.addfiles)
        self.pushButton_5.clicked.connect(self.delect_word)
        self.pushButton_4.clicked.connect(self.replace_word)
        self.pushButton.clicked.connect(self.roll_back)
        self.pushButton_2.clicked.connect(self.rename)
        self.pushButton_3.clicked.connect(self.roll_rename)

    def closeEvent(self, a0: QtGui.QCloseEvent):
        """关闭窗口时执行"""
        self.close()  # 必要代码

    def save(self):
        """保存历史记录"""
        al = []
        for i in range(self.listWidget.count()):
            i = self.listWidget.item(i)
            al.append(i.whatsThis())
        self.filelist.save(al)

    def replace_delelate(self):
        """替换对话框与删除对话框的切换"""
        if self.checkBox.isChecked():
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.stackedWidget.setCurrentIndex(0)

    def add_files(self):
        """向列表中添加文件"""
        self.save()
        self.checkBox_4.setChecked(False)
        path = QtWidgets.QFileDialog.getExistingDirectory(self, '请选择一个目录')
        if path != '':
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

    def list_click(self):
        """文件列表中项的点击操作"""
        self.label.setText(self.listWidget.currentItem().toolTip())

    def change_single_name(self):
        """更改单个文件名称"""
        self.save()
        self.checkBox_4.setChecked(False)
        text, flag = QtWidgets.QInputDialog.getText(self, '名称修改', '请输入新名称',
                                                    QtWidgets.QLineEdit.Normal, self.listWidget.currentItem().text())
        if flag:
            self.filelist.find_by_id(self.listWidget.currentItem().whatsThis()).name = text
            self.listWidget.currentItem().setText(
                self.filelist.find_by_id(self.listWidget.currentItem().whatsThis()).name)

    def show_origin_name(self):
        """展示原名称"""
        if self.checkBox_4.isChecked():
            names = self.filelist.origin_list
            for i in range(self.listWidget.count()):
                i = self.listWidget.item(i)
                i.setText(names[i.whatsThis()])
        else:
            names = self.filelist.name_list
            for i in range(self.listWidget.count()):
                i = self.listWidget.item(i)
                i.setText(names[i.whatsThis()])

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
                    if i == num-1:
                        raise IndexError
                    self.listWidget.takeItem(i)
                    self.listWidget.insertItem(i+1, item)
                    self.listWidget.setCurrentItem(item)
        except IndexError:
            QtWidgets.QMessageBox.critical(self, '错误', '已经到底了！')

    def delete(self):
        """删除文件"""
        self.save()
        self.checkBox_4.setChecked(False)
        num = 0
        files = []
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i - num)
            if item.isSelected():
                self.listWidget.takeItem(i - num)
                files.append(item.whatsThis())
                num += 1
        self.filelist.delete(files)
        if len(files) == 0:
            flag = QtWidgets.QMessageBox.question(self, '无选择内容', '您没有选择任何需要删除的对象\n是否清空整个列表？(注：这会同时清除历史记录)', )
            if flag == QtWidgets.QMessageBox.Yes:
                self.listWidget.clear()
                self.filelist = FileList()
                self.label.setText('本软件已开源于GitHub\n详情请访问 https://github.com/zhehao0728/Renamer')

    def addfiles(self):
        """添加文件"""
        self.save()
        self.checkBox_4.setChecked(False)
        files, filetype = QtWidgets.QFileDialog.getOpenFileNames(self, "选择多个文件")
        add = self.filelist.add(files)
        for key, value in add.items():
            item = QtWidgets.QListWidgetItem()
            item.setText(value.name)
            item.setWhatsThis(key)
            item.setToolTip(value.origin)
            self.listWidget.addItem(item)

    def replace_word(self):
        """替换关键词"""
        self.save()
        self.checkBox_4.setChecked(False)
        self.filelist.replace(self.lineEdit.text(), self.lineEdit_2.text(), self.checkBox_2.isChecked())
        dic = self.filelist.name_list
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            item.setText(dic[item.whatsThis()])

    def delect_word(self):
        """删除关键词"""
        self.save()
        self.checkBox_4.setChecked(False)
        self.filelist.replace(self.textEdit_2.toPlainText(), '', self.checkBox_2.isChecked())
        dic = self.filelist.name_list
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            item.setText(dic[item.whatsThis()])

    def roll_back(self):
        """撤销"""
        self.checkBox_4.setChecked(False)
        files = self.filelist.roll_back()
        self.listWidget.clear()
        for key, value in files.items():
            item = QtWidgets.QListWidgetItem()
            item.setText(value.name)
            item.setWhatsThis(key)
            item.setToolTip(value.origin)
            self.listWidget.addItem(item)

    def roll_rename(self):
        """按序命名"""
        self.save()
        self.checkBox_4.setChecked(False)

        ran = []
        if self.comboBox.currentIndex() == 0:
            for i in range(self.listWidget.count()):
                ran.append(self.listWidget.item(i))
        elif self.comboBox.currentIndex() == 1:
            for i in range(self.listWidget.count()):
                item = self.listWidget.item(i)
                if item.isSelected():
                    ran.append(item)

        if self.comboBox_2.currentIndex() == 0:
            pass
        elif self.comboBox_2.currentIndex() == 1:
            ran.reverse()

        if self.comboBox_3.currentIndex() == 0:
            for index, i in enumerate(ran):
                text = self.textEdit.toPlainText()
                i.setText(text+str(index+1))
                event = self.filelist.find_by_id(i.whatsThis())
                event.name = text+str(index+1)
        elif self.comboBox_3.currentIndex() == 1:
            for index, i in enumerate(ran):
                i.setText(str(index+1))
                event = self.filelist.find_by_id(i.whatsThis())
                event.name = str(index+1)
        elif self.comboBox_3.currentIndex() == 2:
            for index, i in enumerate(ran):
                text = self.textEdit.toPlainText()
                index += 1
                while r'{index}' in text:
                    text = text.replace(r'{index}', str(index))
                i.setText(text)
                event = self.filelist.find_by_id(i.whatsThis())
                event.name = text

    def rename(self):
        """重命名"""
        self.checkBox_4.setChecked(False)
        flag = QtWidgets.QMessageBox.question(self, '重命名', '确定重命名？')
        if flag == QtWidgets.QMessageBox.Yes:
            try:
                self.filelist.rename()
            except BaseException as e:
                QtWidgets.QMessageBox.critical(self, '重命名失败', '重命名失败,因为\n'+str(e))
            else:
                dic = self.filelist.path_list
                for i in range(self.listWidget.count()):
                    item = self.listWidget.item(i)
                    item.setToolTip(dic[item.whatsThis()])
                QtWidgets.QMessageBox.information(self, '重命名', '文件重命名成功！')


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Ui()
    MainWindow.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
    MainWindow.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
