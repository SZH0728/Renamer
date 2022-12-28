# -*- coding:utf-8 -*-
# AUTHOR: SUN
from function.suffix_window import Ui_Form


class main(Ui_Form):
    def __init__(self, renamer):
        super(main, self).__init__()
        self.main = renamer
        self.config = self.main.config.read('suffix')

    def setupUi(self, form):
        super(main, self).setupUi(form)
        self.pushButton.clicked.connect(self.rename)

        self.textEdit.textChanged.connect(self.key_change)
        self.lineEdit.textChanged.connect(self.to_change)

        self.textEdit.setText(self.config['key'])
        self.lineEdit.setText(self.config['to'])

    def rename(self):
        suffix = self.textEdit.toPlainText().split('|')
        target = self.lineEdit.text()

        if target[0] != '.':
            target = '.'+target

        for index, i in enumerate(suffix):
            if i[0] != '.':
                suffix[index] = '.'+i

        ran = []
        for i in range(self.main.listWidget.count()):
            item = self.main.listWidget.item(i)
            if item.isSelected():
                ran.append(item)
        if len(ran) == 0:
            for i in range(self.main.listWidget.count()):
                item = self.main.listWidget.item(i)
                if not item.isHidden():
                    ran.append(item)

        for i in ran:
            file = self.main.filelist.Id_Item[i.whatsThis()]
            if file.suffix in suffix:
                file.suffix = target
                i.setText(file.name+target)

    def key_change(self):
        self.config['key'] = self.textEdit.toPlainText()

    def to_change(self):
        self.config['to'] = self.lineEdit.text()


if __name__ == '__main__':
    pass
