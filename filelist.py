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
        类FlieList专用对象
        :param path: 文件完整路径
        :param id_: 文件唯一编码，应为FileId所生成
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
        目标字符替换
        :param keyw: 关键词
        :param target: 替换为
        :param regex: 是否使用正则
        """
        if not regex:
            while keyw in self._name:
                self._name = self._name.replace(keyw, target)
        else:
            self._name = sub(keyw, target, self._name)

    def rename(self):
        """重命名"""
        rename(self.origin, join(self.path, self.name))
        self.origin = join(self.path, self.name)


class FileList(object):
    def __init__(self):
        self.files = {}
        self.history = []
        self.fileid = FileId(6)

    @property
    def name_list(self):
        """
        :return: id-name字典
        """
        r = {}
        for i in self.files.values():
            r[i.id] = i.name
        return r

    @property
    def origin_list(self):
        """
        :return:id-origin字典
        """
        r = {}
        for i in self.files.values():
            r[i.id] = split(i.origin)[1]
        return r

    @property
    def path_list(self):
        """
        :return:id-path字典
        """
        r = {}
        for i in self.files.values():
            r[i.id] = i.origin
        return r

    def add(self, files: list):
        """
        添加文件
        :param files: 文件路径的列表
        :return: 新增的FileListItem对象
        """
        dic = {}
        for i in files:
            id_ = self.fileid.get()
            self.files[id_] = FileListItem(i, id_)
            dic[id_] = self.files[id_]
        return dic

    def delete(self, include: list):
        """
        删除文件
        :param include: 文件的id
        """
        for i in include:
            self.files.pop(i)

    def save(self, order: list):
        """
        保存历史记录
        :param order: 文件id顺序
        """
        dic = {}
        for i in order:
            dic[i] = copy(self.files[i])
        self.history.append(dic)

    def find_by_name(self, name: str):
        """
        通过名称查找
        :param name: 名称
        :return: 符合的FileListItem对象
        """
        r = []
        for i in self.files.values():
            if i.name == name:
                r.append(i)
        return r

    def find_by_id(self, id_: str):
        """
        通过id查找
        :param id_: id
        :return: 符合的FileListItem对象
        """
        return self.files[id_]

    def replace(self, keyw: str, target: str, regex: bool or str):
        """
        目标字符替换
        :param keyw: 关键词
        :param target: 替换为
        :param regex: 是否使用正则
        """
        for i in self.files.values():
            i.replace(keyw, target, regex)

    def roll_back(self):
        """
        撤销到上一次保存
        :return: id-FileListItem对象的字典
        """
        try:
            self.files = self.history.pop()
        except IndexError:
            pass
        return self.files

    def rename(self):
        """
        重命名
        """
        for i in self.files.values():
            i.rename()


if __name__ == '__main__':
    pass
