# -*- coding:utf-8 -*-
# AUTHOR: Sun

from abc import ABC, abstractmethod
from typing import Iterable, Any
from dataclasses import dataclass, field
from os.path import join, split, exists
from re import compile


@dataclass()
class File:
    current_path: str
    current_name: str
    target_name: str = field(init=False, default=None)
    target_path: str = field(init=False, default=None)

    def __post_init__(self):
        self.target_name = self.current_name
        self.target_path = self.current_path

    @property
    def current_full_path(self):
        return join(self.current_path, self.current_name)

    @property
    def target_full_path(self):
        return join(self.target_path, self.target_name)


class Base(ABC):
    def __getitem__(self, item: int):
        return self.select_current_by_id(item)

    def __iter__(self):
        for i in self.select():
            yield i
    
    @staticmethod
    def create_file_by_full_path(path: str) -> File:
        path, name = split(path)
        return File(path, name)

    @staticmethod
    def create_file_by_path_name(path: str, name: str) -> File:
        return File(path, name)

    @staticmethod
    def is_exist(file: File) -> bool:
        return exists(file.current_full_path)

    @abstractmethod
    def insert(self, file: File) -> bool:
        pass

    @abstractmethod
    def select(self, path: str = None, name: str = None, id_: int = None, current: bool = True) -> list[File]:
        pass

    @abstractmethod
    def update(self, file: File) -> File:
        pass

    def select_current(self, path: str = None, name: str = None, id_: int = None) -> list[File]:
        return self.select(path, name, id_, True)

    def select_target(self, path: str = None, name: str = None, id_: int = None) -> list[File]:
        return self.select(path, name, id_, False)

    def regex_select(self, path: str = None, name: str = None, current: bool = True) -> list[File]:
        if path:
            path = compile(path)

        if name:
            name = compile(name)

        result: list[File] = []
        for i in self.select(current=current):
            if path and not path.match(i.current_path):
                continue
            if name and not name.match(i.current_name):
                continue
            result.append(i)

        return result

    def regex_select_current(self, path: str = None, name: str = None) -> list[File]:
        return self.regex_select(path, name, True)

    def regex_select_target(self, path: str = None, name: str = None) -> list[File]:
        return self.regex_select(path, name, False)

    def insert_by_full_path(self, path: str) -> bool:
        file = self.create_file_by_full_path(path)
        return self.insert(file)

    def insert_by_path_name(self, path: str, name: str) -> bool:
        file = self.create_file_by_path_name(path, name)
        return self.insert(file)

    def insert_files(self, files: Iterable) -> list[tuple[File, bool]]:
        result: list[tuple[File, bool]] = []

        for file in files:
            result.append((file, self.insert(file)))
        return result

    def select_current_by_name(self, name: str) -> list[File]:
        return self.select_current(name=name)

    def select_current_by_path(self, path: str) -> list[File]:
        return self.select_current(path=path)

    def select_current_by_id(self, id_: int) -> list[File]:
        return self.select_current(id_=id_)

    def select_target_by_name(self, name: str) -> list[File]:
        return self.select_target(name=name)

    def select_target_by_path(self, path: str) -> list[File]:
        return self.select_target(path=path)

    def select_target_by_id(self, id_: int) -> list[File]:
        return self.select_target(id_=id_)

    def regex_select_current_by_name(self, name: str) -> list[File]:
        return self.regex_select(name=name)

    def regex_select_current_by_path(self, path: str) -> list[File]:
        return self.regex_select(path=path)

    def regex_select_target_by_name(self, name: str) -> list[File]:
        return self.regex_select(name=name, current=False)

    def regex_select_target_by_path(self, path: str) -> list[File]:
        return self.regex_select(path=path, current=False)


if __name__ == '__main__':
    pass
