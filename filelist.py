# -*- coding:utf-8 -*-
# AUTHOR: SUN
from re import sub, findall
from os.path import split, join
from os import rename
from fileid import FileId
from copy import copy


class FileListItem(object):
    def __init__(self, path: str, id_: str):
        """

        :param path:
        """
        self.id = id_
        path = sub(r'/', r'\\', path)
        self.origin = path
        path = split(path)
        self.path = path[0]
        self._name = findall(r'^(.*)(\..*?)$', path[1])
        if len(self._name) != 0:
            self._suffix = self._name[0][1]
            self._name = self._name[0][0]
        else:
            self._suffix = ''
            self._name = path[1]

    @property
    def name(self):
        return self._name+self._suffix

    @name.setter
    def name(self, value: str):
        self._name = sub(self._suffix, '', value)

    def replace(self, keyw: str, target: str, regex: bool):
        """
        :param keyw:
        :param target:
        :param regex:
        """
        if not regex:
            while keyw in self._name:
                self._name = self._name.replace(keyw, target)
        else:
            self._name = sub(keyw, target, self._name)

    def rename(self):
        rename(self.origin, join(self.path, self.name))
        self.origin = join(self.path, self.name)


class FileList(object):
    def __init__(self):
        self.files = {}
        self.history = []
        self.fileid = FileId(4)

    @property
    def name_list(self):
        """

        :return:
        """
        r = {}
        for i in self.files.values():
            r[i.id] = i.name
        return r

    @property
    def origin_list(self):
        """

        :return:
        """
        r = {}
        for i in self.files.values():
            r[i.id] = split(i.origin)[1]
        return r

    @property
    def path_list(self):
        """

        :return:
        """
        r = {}
        for i in self.files.values():
            r[i.id] = i.origin
        return r

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
            dic[i] = copy(self.files[i])
        self.history.append(dic)

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

    def find_by_id(self, id_: str):
        return self.files[id_]

    def replace(self, keyw: str, target: str, regex: bool or str):
        """

        :param keyw:
        :param target:
        :param regex:
        """
        for i in self.files.values():
            i.replace(keyw, target, regex)

    def roll_back(self):
        """

        :return:
        """
        try:
            self.files = self.history.pop()
        except IndexError:
            pass
        return self.files

    def rename(self):
        """

        """
        for i in self.files:
            i.rename()


if __name__ == '__main__':
    pass
