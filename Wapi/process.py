# -*- coding:utf-8 -*-
# AUTHOR: SUN
from os import rename
from os.path import join

from PyQt5 import QtWidgets, QtCore

from Wapi.process_window import Ui_Form


class main(Ui_Form, QtWidgets.QDialog):
    def __init__(self, filelist):
        super(main, self).__init__()
        self.renamer = thread(filelist)
        self.renamer.rate.connect(self.rate_change)
        self.setupUi(self)
        self.renamer.start()

    def setupUi(self, form):
        super(main, self).setupUi(form)
        self.pushButton.clicked.connect(self.cancel)

    def rate_change(self, rate):
        self.progressBar.setValue(rate[0])
        self.label.setText(self.label.text() + rate[2])
        if len(rate[1]) != 0:
            text = self.textEdit.toPlainText()
            text += '\n'.join(rate[1])
            text += '\n'
            self.textEdit.setText(text)
        if rate[0] == 100:
            self.label.setText('重命名完成！')
            self.pushButton.setText('确认')

    def cancel(self):
        if self.pushButton.text() == '取消':
            msg = QtWidgets.QMessageBox.question(self, '取消操作', '确认取消吗？', QtWidgets.QMessageBox.Yes |
                                                 QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
            if msg == QtWidgets.QMessageBox.Yes:
                self.renamer.stop_condition = 1
        elif self.pushButton.text() == '确认':
            self.close()


class thread(QtCore.QThread):
    rate = QtCore.pyqtSignal(object)

    def __init__(self, filelist):
        super(thread, self).__init__()
        self.filelist = filelist
        self.stop_condition = 0

    def run(self):
        error = []
        number = len(self.filelist.Id_Item) / 100
        time = 0
        has = 0
        for key, value in self.filelist.Id_Item.items():
            time += 1
            has += 1

            if self.stop_condition == 1:
                break
            path = join(value.path, value.name + value.suffix)
            try:
                rename(value.origin, path)
            except BaseException as e:
                error.append(str(e))
            else:
                self.filelist.Id_Origin[key] = path
                value.origin = path

            if time >= number:
                self.rate.emit([(has / (number * 100)) * 100, list(error), value.name + value.suffix])
                time = 0
                error.clear()
        self.rate.emit([100, error, ''])


if __name__ == '__main__':
    pass
