# -*- coding:utf-8 -*-
# AUTHOR: SUN
from re import sub

from function.replace_window import Ui_Form


class main(Ui_Form):
    def __init__(self, renamer):
        super(main, self).__init__()
        self.main = renamer
        self.config = self.main.config.read('replace')

    def setupUi(self, form):
        super(main, self).setupUi(form)
        self.pushButton.clicked.connect(self.replace)
        self.pushButton_2.clicked.connect(self.delete)
        self.textEdit.textChanged.connect(self.replace_key)
        self.textEdit_2.textChanged.connect(self.replace_to)
        self.textEdit_3.textChanged.connect(self.delete_key)
        self.checkBox.clicked.connect(self.replace_re)
        self.checkBox_2.clicked.connect(self.delete_re)

        self.textEdit.setText(self.config['replace']['key'])
        self.textEdit_2.setText(self.config['replace']['to'])
        self.textEdit_3.setText(self.config['delete']['key'])
        self.checkBox.setChecked(bool(self.config['replace']['re']))
        self.checkBox_2.setChecked(bool(self.config['delete']['re']))

    def replace(self):
        self.main.filelist.save()
        target = self.textEdit.toPlainText()
        to = self.textEdit_2.toPlainText()
        a = []
        for i in range(self.main.listWidget.count()):
            item = self.main.listWidget.item(i)
            if item.isSelected():
                a.append(item)
        if self.checkBox.isChecked():
            if len(a) == 0:
                for i in range(self.main.listWidget.count()):
                    item = self.main.listWidget.item(i)
                    if item.isHidden():
                        continue
                    file = self.main.filelist.Id_Item[item.whatsThis()]
                    name = sub(target, to, file.name)
                    file.name = name
                    item.setText(file.name+file.suffix)
            else:
                for item in a:
                    file = self.main.filelist.Id_Item[item.whatsThis()]
                    name = sub(target, to, file.name)
                    file.name = name
                    item.setText(file.name + file.suffix)
        else:
            if len(a) == 0:
                for i in range(self.main.listWidget.count()):
                    item = self.main.listWidget.item(i)
                    if item.isHidden():
                        continue
                    file = self.main.filelist.Id_Item[item.whatsThis()]
                    name = file.name.replace(target, to)
                    file.name = name
                    item.setText(file.name+file.suffix)
            else:
                for item in a:
                    file = self.main.filelist.Id_Item[item.whatsThis()]
                    name = file.name.replace(target, to)
                    file.name = name
                    item.setText(file.name + file.suffix)

    def delete(self):
        self.main.filelist.save()
        target = self.textEdit_3.toPlainText()
        a = []
        for i in range(self.main.listWidget.count()):
            item = self.main.listWidget.item(i)
            if item.isSelected():
                a.append(item)
        if self.checkBox.isChecked():
            if len(a) == 0:
                for i in range(self.main.listWidget.count()):
                    item = self.main.listWidget.item(i)
                    if item.isHidden():
                        continue
                    file = self.main.filelist.Id_Item[item.whatsThis()]
                    name = sub(target, '', file.name)
                    file.name = name
                    item.setText(file.name + file.suffix)
            else:
                for item in a:
                    file = self.main.filelist.Id_Item[item.whatsThis()]
                    name = sub(target, '', file.name)
                    file.name = name
                    item.setText(file.name + file.suffix)
        else:
            if len(a) == 0:
                for i in range(self.main.listWidget.count()):
                    item = self.main.listWidget.item(i)
                    if item.isHidden():
                        continue
                    file = self.main.filelist.Id_Item[item.whatsThis()]
                    name = file.name.replace(target, '')
                    file.name = name
                    item.setText(file.name + file.suffix)
            else:
                for item in a:
                    file = self.main.filelist.Id_Item[item.whatsThis()]
                    name = file.name.replace(target, '')
                    file.name = name
                    item.setText(file.name + file.suffix)

    def replace_key(self):
        self.config['replace']['key'] = self.textEdit.toPlainText()

    def replace_to(self):
        self.config['replace']['to'] = self.textEdit_2.toPlainText()

    def replace_re(self):
        if self.checkBox.isChecked():
            self.config['replace']['re'] = '1'
        else:
            self.config['replace']['re'] = ''

    def delete_key(self):
        self.config['delete']['key'] = self.textEdit_3.toPlainText()

    def delete_re(self):
        if self.checkBox_2.isChecked():
            self.config['delete']['re'] = '1'
        else:
            self.config['delete']['re'] = ''


if __name__ == '__main__':
    pass
