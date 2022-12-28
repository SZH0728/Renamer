# -*- coding:utf-8 -*-
# AUTHOR: SUN
from re import findall

from function.sequence_window import Ui_Form


class main(Ui_Form):
    def __init__(self, renamer):
        super(main, self).__init__()
        self.main = renamer
        self.config = self.main.config.read('sequence')

    def setupUi(self, form):
        super(main, self).setupUi(form)
        self.pushButton.clicked.connect(self.rename)
        self.textEdit.setPlaceholderText("""自定义方法格式：
字符串中{auto(#)|index}会被替换为序号
参数说明：{auto(#)|index}
auto: 自动补全(也可以使用数字)
#: 补全的字符
auto(#)不填写意味着不使用补全""")

        self.comboBox.currentIndexChanged.connect(self.range_change)
        self.comboBox_2.currentIndexChanged.connect(self.sequence_change)
        self.comboBox_3.currentIndexChanged.connect(self.type_change)
        self.textEdit.textChanged.connect(self.words_change)

        self.comboBox.setCurrentIndex(int(self.config['range']))
        self.comboBox_2.setCurrentIndex(int(self.config['sequence']))
        self.comboBox_3.setCurrentIndex(int(self.config['type']))
        self.textEdit.setText(self.config['words'])

    def rename(self):
        self.main.filelist.save()
        ran = []
        if self.comboBox.currentIndex() == 0:
            for i in range(self.main.listWidget.count()):
                ran.append(self.main.listWidget.item(i))
        elif self.comboBox.currentIndex() == 1:
            for i in range(self.main.listWidget.count()):
                item = self.main.listWidget.item(i)
                if not item.isHidden():
                    ran.append(item)
        elif self.comboBox.currentIndex() == 2:
            for i in range(self.main.listWidget.count()):
                item = self.main.listWidget.item(i)
                if item.isSelected():
                    ran.append(item)

        if self.comboBox_2.currentIndex() == 1:
            ran.reverse()

        name = self.textEdit.toPlainText()
        if self.comboBox_3.currentIndex() == 0:
            for index, item in enumerate(ran):
                file = self.main.filelist.Id_Item[item.whatsThis()]
                file.name = name+str(index+1)
                item.setText(file.name+file.suffix)
        elif self.comboBox_3.currentIndex() == 1:
            length = len(str(len(ran)))
            for index, item in enumerate(ran):
                file = self.main.filelist.Id_Item[item.whatsThis()]
                index = str(index+1)
                index = '0'*(length-len(index))+index
                file.name = name+index
                item.setText(file.name+file.suffix)
        elif self.comboBox_3.currentIndex() == 2:
            for index, item in enumerate(ran):
                file = self.main.filelist.Id_Item[item.whatsThis()]
                file.name = str(index+1)
                item.setText(file.name+file.suffix)
        elif self.comboBox_3.currentIndex() == 3:
            length = len(str(len(ran)))
            for index, item in enumerate(ran):
                file = self.main.filelist.Id_Item[item.whatsThis()]
                index = str(index+1)
                index = '0'*(length-len(index))+index
                file.name = index
                item.setText(file.name+file.suffix)
        elif self.comboBox_3.currentIndex() == 4:
            """
            自定义方法格式：
            字符串中{auto(#)|index}会被替换为序号
            参数说明：{auto(#)|index}
            auto: 自动补全(也可以使用数字)
            #: 补全的字符
            auto(#)不填写意味着不使用补全
            """
            length = len(str(len(ran) + 1))
            name_key = findall(r'\{(auto|\d+?)\((.*?)\)\|index\}', name)
            for index, item in enumerate(ran):
                index += 1
                index = str(index)
                file = self.main.filelist.Id_Item[item.whatsThis()]
                file_name = str(name)
                file_name = file_name.replace('{index}', index)
                for i in name_key:
                    if i[0] == 'auto':
                        number = str(i[1]*(length-len(index)))+index
                        file_name = file_name.replace('{auto(%s)|index}' % i[1], number)
                    else:
                        number = str(i[1] * (int(i[0]) - len(index))) + index
                        file_name = file_name.replace('{%s(%s)|index}' % (i[0], i[1]), number)
                item.setText(file_name+file.suffix)
                file.name = file_name

    def range_change(self):
        self.config['range'] = self.comboBox.currentIndex()

    def sequence_change(self):
        self.config['sequence'] = self.comboBox_2.currentIndex()

    def type_change(self):
        self.config['type'] = self.comboBox_3.currentIndex()

    def words_change(self):
        self.config['words'] = self.textEdit.toPlainText()


if __name__ == '__main__':
    pass
