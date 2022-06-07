from threading import Thread
from os.path import isfile, join
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

    def add_files(self, files: dict, where: int):
        """
        添加文件
        :param files:
        :param where:
        """
        self.submit()
        front = self.files[:where]
        behind = self.files[where:]
        self.files = front + files + behind

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
            return self.files

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
            if re_:
                self.files[k] = re.sub(key, new, v)
            else:
                self.files[k] = v.replace(key, new)
        self._same_name_test()
        return self.files


if __name__ == '__main__':
    pass
