# -*- coding:utf-8 -*-
# AUTHOR: Sun

from abc import ABC, abstractmethod
from typing import Iterable, Any
from dataclasses import dataclass, field
from os.path import join, split, exists
from re import compile


@dataclass()
class File:
    id: int = field(init=False, default=None)
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
        result = self.select(id_=item)
        if len(result) != 1:
            raise ValueError(f'{item} is not unique')
        else:
            return result[0]

    def __iter__(self):
        for i in self.select():
            yield i

    @staticmethod
    def is_exist(file: File) -> bool:
        return exists(file.current_full_path)

    @abstractmethod
    def insert(self, file: File) -> File:
        pass

    @abstractmethod
    def select(self,
               path: str = None,
               name: str = None,
               id_: int = None,
               current: bool = True,
               limit: int = None,
               ) -> list[File]:
        pass

    @abstractmethod
    def update(self, file: File) -> File:
        pass

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

    def insert_file_by_full_path(self, path: str) -> File:
        path, name = split(path)
        return self.insert_file_by_path_name(path, name)

    def insert_file_by_path_name(self, path: str, name: str) -> File:
        return self.insert(File(path, name))

    def insert_files(self, files: Iterable) -> list[File]:
        result: list[File] = []

        for file in files:
            result.append(self.insert(file))
        return result


if __name__ == '__main__':
    pass
