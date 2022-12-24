# -*- coding:utf-8 -*-
# AUTHOR: SUN
from re import sub

from function.replace_window import Ui_Form
from main import main as rename


class main(Ui_Form):
    def __init__(self, renamer: rename):
        super(main, self).__init__()
        self.main = renamer

    def setupUi(self, form):
        super(main, self).setupUi(form)
        self.pushButton.clicked.connect(self.replace)
        self.pushButton_2.clicked.connect(self.delete)

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


if __name__ == '__main__':
    pass
