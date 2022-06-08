from threading import Thread
from os.path import isfile, join, split
from os import listdir
from copy import copy  # 进行真正的复制
import re


class error(BaseException):
    """所有异常的基类"""
    pass


class same_name_error(error):
    """重名错误"""
    pass


class traversal(Thread):
    """
    扫描指定目录下所有文件，包括子文件夹中文件
    使用子线程的方式，防止程序假死
    """
    def __init__(self):
        super(traversal, self).__init__()
        self.setDaemon(True)
        self._files = []  # 所有文件的完整路径
        self._path = ''  # 开始目录
    
    def run(self):
        self.view(self._path)
        
    def view(self, path):
        """
        扫描文件并存入self._files
        :param path: 开始目录
        """
        for i in listdir(path):
            if not isfile(join(path, i)):
                self.view(join(path, i))
            else:
                self._files.append(join(path, i))
    
    def start(self, path):
        """
        开始扫描
        :param path: 开始目录
        """
        self._path = path
        super(traversal, self).start()
    
    @property
    def files(self):
        """属性：已发现文件路径"""
        return self._files
    
    @property
    def lenth(self):
        """属性：已发现文件数目"""
        return len(self._files)
        

class File_list(object):
    def __init__(self):
        self.history = []  # 修改历史
        self.files = {}  # 原名称——现名称

    @property
    def orginal_name(self):
        """返回字典：现名称——原名称"""
        return dict(zip(self.files.values(), self.files.keys()))

    @property
    def name_list(self):
        """属性：返回现名称列表"""
        r = []
        for i in self.files.values():
            i = split(i)[1]
            i = re.sub(r'\..*$', '', i)
            r.append(i)
        return r

    def change_one_file(self, org: str, new: str):
        """
        单个文件名称修改
        :param org: 原文件名
        :param new: 现文件名（仅名称）
        """
        path = split(self.files[org])[0]
        self.files[org] = join(path, new)

    def insert(self, files: list, where: int):
        """
        添加文件
        :param files: 插入文件的绝对路径
        :param where: 插入位置
        """
        self.submit()
        front_key = list(self.files.keys()[:where - 1])
        front_value = list(self.files.values()[:where - 1])
        behind_key = list(self.files.keys()[where:])
        behind_value = list(self.files.values()[where:])
        self.files = dict(zip(front_key+files+behind_key, front_value+files+behind_value))
        self._same_name_test()
        return self.name_list

    def delelate(self, files: list):
        """
        删除文件
        :param files: 删除文件的绝对路径
        """
        self.submit()
        for i in files:
            del self.files[i]
        return self.name_list

    def move_up(self, files: list):
        """
        文件位置上移一格
        :param files: 需要移动的文件
        """
        for i in files:
            where = list(self.files.keys()).index(i)
            value = self.files[i]
            del self.files[i]
            front_key = list(self.files.keys()[:where - 1])
            front_key.insert(-2, i)
            front_value = list(self.files.values()[:where - 1])
            front_value.insert(-2, value)
            behind_key = list(self.files.keys()[where:])
            behind_value = list(self.files.values()[where:])
            self.files = dict(zip(front_key + behind_key, front_value + behind_value))
        return self.name_list

    def move_down(self, files: list):
        """
        文件位置下移一格
        :param files: 需要移动的文件
        """
        for i in files:
            where = list(self.files.keys()).index(i)
            value = self.files[i]
            del self.files[i]
            front_key = list(self.files.keys()[:where - 1])
            front_value = list(self.files.values()[:where - 1])
            behind_key = list(self.files.keys()[where:])
            behind_key.insert(1, i)
            behind_value = list(self.files.values()[where:])
            behind_value.insert(1, value)
            self.files = dict(zip(front_key + behind_key, front_value + behind_value))
        return self.name_list

    def submit(self):
        """保存至历史"""
        self.history.append(copy(self.files))

    def revocation(self):
        """撤销"""
        if len(self.history) == 0:
            self.files = []
            return self.files
        else:
            self.files = self.history.pop()
            return self.name_list

    def _same_name_test(self):
        """重名检查"""
        if len(self.files.values()) != len(tuple(self.files.values())):
            raise same_name_error('出现重名文件')

    def replace(self, key='', new='', re_=False):
        """
        移除关键词
        :param key: 关键词
        :param new: 替换为
        :param re_: 是否启用正则表达式
        """
        self.submit()
        for k, v in self.files.items():
            path, v = split(v)
            v, suffix = re.findall(r'($.*)(\..*$)', v)
            if re_:
                self.files[k] = join(path, re.sub(key, new, v)+suffix)
            else:
                self.files[k] = join(path, v.replace(key, new)+suffix)
        self._same_name_test()
        return self.name_list


if __name__ == '__main__':
    pass
