# -*- coding:utf-8 -*-
# AUTHOR: SUN

class ReNmaerError(BaseException):
    """所有异常基类"""
    pass


class FileListError(ReNmaerError):
    """FileList类与其相关类的异常"""
    pass


class IdOutOfLength(ReNmaerError):
    """id长度超过设定值"""
    pass


if __name__ == '__main__':
    pass
