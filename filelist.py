# -*- coding:utf-8 -*-
# AUTHOR: SUN
from re import sub
from os.path import split, join
from os import rename
from fileid import FileId


class FileListItem(object):
    def __init__(self, path: str, id_: str):
        """

        :param path:
        """
        self.id = id_
        self.origin = path
        path = split(path)
        self.path = path[0]
        self.name = path[1]

    def delete(self, keyw: str, regex: bool or str):
        """

        :param keyw:
        :param regex:
        """
        if type(regex) == bool and not regex:
            while keyw in self.name:
                self.name.replace(keyw, '')
        else:
            self.name = sub(regex, '', self.name)

    def replace(self, keyw: str, target: str, regex: bool or str):
        """
        :param keyw:
        :param target:
        :param regex:
        """
        if type(regex) == bool and not regex:
            while keyw in self.name:
                self.name.replace(keyw, target)
        else:
            self.name = sub(regex, target, self.name)

    def rename(self):
        rename(self.origin, join(self.path, self.name))


class FileList(object):
    def __init__(self):
        self.files = {}
        self.history = []
        self.fileid = FileId(4)

    def add(self, files: list):
        """

        :param files:
        :return:
        """
        dic = {}
        for i in files:
            id_ = self.fileid.get()
            self.files[id_] = FileListItem(i, id_)
            dic[id_] = self.files[id_]
        return dic

    def delete(self, include: list):
        """

        :param include:
        """
        for i in include:
            self.files.pop(i)

    def save(self, order: list):
        """

        :param order:
        """
        dic = {}
        for i in order:
            dic[i] = self.files[i]

    def find_by_name(self, name: str):
        """

        :param name:
        :return:
        """
        r = []
        for i in self.files.values():
            if i.name == name:
                r.append(i)
        return r

    def rename(self):
        """

        """
        for i in self.files:
            i.rename()


if __name__ == '__main__':
    pass
