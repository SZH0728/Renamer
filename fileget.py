# -*- coding:utf-8 -*-
# AUTHOR: SUN
from os import listdir, walk
from os.path import isdir, join


def get_files(path: str):
    """

    :param path:
    :return:
    """
    r = []
    for i in listdir(path):
        i = join(path, i)
        if not isdir(i):
            r.append(i)
    return r


def get_files_deep(path: str):
    """

    :param path:
    :return:
    """
    r = []
    for paths, dirs, files in walk(path):
        for i in files:
            r.append(join(paths, i))
    return r


if __name__ == '__main__':
    pass
