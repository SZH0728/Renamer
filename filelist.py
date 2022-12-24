# -*- coding:utf-8 -*-
# AUTHOR: SUN
from copy import copy
from os.path import split

from Wapi.process import main


class FileId(object):
    def __init__(self):
        self.num = 0

    def get(self):
        self.num += 1
        return hex(self.num)

    def clear(self):
        self.num = 0


class FileListItem(object):
    def __init__(self, path: str, id_: str):
        self.origin = path
        path = split(path)
        index = path[1].rfind(r'.')
        self.path = path[0]
        self.name = path[1][:index]
        self.suffix = path[1][index:]
        self.id = id_


class FileList(object):
    def __init__(self):
        self.ID = FileId()
        self.Id_Origin = {}
        self.Id_Item = {}
        self.history = []

    def new(self, path):
        id_ = self.ID.get()
        self.Id_Item[id_] = FileListItem(path, id_)
        self.Id_Origin[id_] = path
        return self.Id_Item[id_]

    def rename(self):
        window = main(self)
        window.exec_()

    def delete(self, id_):
        del self.Id_Item[id_]

    def save(self):
        dic = {}
        for i in self.Id_Item.values():
            dic[i.id] = copy(i.name+i.suffix)
        self.history.append(dic)

    def rollback(self):
        try:
            dic = self.history.pop()
        except IndexError:
            self.Id_Item = []
        else:
            self.Id_Item.clear()
            for key, value in dic.items():
                self.Id_Item[key] = FileListItem(value, key)

    def clear(self):
        self.Id_Item.clear()


if __name__ == '__main__':
    pass
