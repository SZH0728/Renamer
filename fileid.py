# -*- coding:utf-8 -*-
# AUTHOR: SUN
from error import IdOutOfLength


class FileId(object):
    def __init__(self, length: int):
        """
        :param length: id长度
        """
        self.number = 0
        self.length = length

    def get(self):
        """
        获取下一个id
        :return: 下一个id
        """
        self.number += 1
        if len(str(self.number)) <= self.length:
            return '0'*(self.length - len(str(self.number))) + str(self.number)
        else:
            raise IdOutOfLength('id(%d)长度(%d)超过设定值(%d)' % (self.number, len(str(self.number)), self.length))

    def clear(self):
        """
        清空id
        """
        self.number = 0


if __name__ == '__main__':
    pass
