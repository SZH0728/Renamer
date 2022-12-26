# -*- coding:utf-8 -*-
# AUTHOR: SUN
from os.path import split

from function.subtitle_window import Ui_Form
from main import main as rename


class main(Ui_Form):
    def __init__(self, renamer: rename):
        super(main, self).__init__()
        self.main = renamer

    def setupUi(self, form):
        super(main, self).setupUi(form)
        self.textEdit.setText('.mp4|.mkv|.avi|.webm')
        self.textEdit_2.setText('.ass')
        self.pushButton.clicked.connect(self.renamer)

    def renamer(self):
        video_suffix = self.textEdit.toPlainText().split('|')
        for index, i in enumerate(video_suffix):
            if i[0] != '.':
                video_suffix[index] = '.'+i

        subtitle_suffix = self.textEdit_2.toPlainText().split('|')
        for index, i in enumerate(subtitle_suffix):
            if i[0] != '.':
                subtitle_suffix[index] = '.'+i

        video = []
        subtitle = {}
        id_item = {}
        for i in range(self.main.listWidget.count()):
            item = self.main.listWidget.item(i)
            file = self.main.filelist.Id_Item[item.whatsThis()]
            if file.suffix in subtitle_suffix:
                name = split(file.origin)[1]
                index = name.rfind(r'.')
                id_item[file.id] = item
                subtitle[name[:index]] = file
            elif file.suffix in video_suffix:
                video.append(file)

        if self.comboBox.currentIndex() == 0:
            for i in video:
                name = split(i.origin)[1]
                index = name.rfind(r'.')
                try:
                    file = subtitle[name[:index]]
                except KeyError:
                    pass
                else:
                    file.name = i.name
                    id_item[file.id].setText(file.name+file.suffix)
        elif self.comboBox.currentIndex() == 1:
            for i in video:
                name = split(i.origin)[1]
                index = name.rfind(r'.')
                name = name[:index]
                for key, value in subtitle.items():
                    if name in key:
                        value.name = value.name.replace(name, i.name)
                        id_item[value.id].setText(value.name+value.suffix)


if __name__ == '__main__':
    pass
