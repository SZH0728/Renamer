# -*- coding:utf-8 -*-
# AUTHOR: SUN
from os import listdir, walk
from os.path import isdir, join


def get_files(path: str):
    """
    获取指定目录下的文件(不包括子文件夹中文件)
    :param path: 指定目录
    :return: 文件列表
    """
    r = []
    for i in listdir(path):
        i = join(path, i)
        if not isdir(i):
            r.append(i)
    return r


def get_files_deep(path: str):
    """
    获取指定目录下的文件(包括子文件夹中文件)
    :param path: 指定目录
    :return: 文件列表
    """
    r = []
    for paths, dirs, files in walk(path):
        for i in files:
            r.append(join(paths, i))
    return r


if __name__ == '__main__':
    pass
