# -*- coding:utf-8 -*-
# AUTHOR: Sun

from abc import ABC, abstractmethod
from typing import Callable
import tkinter as tk
from tkinter import ttk

from messager import Message


class Base(ABC):
    def __init__(self, root: tk.Frame | tk.Tk, name: str):
        self.root = tk.Frame(root, name=name, highlightbackground="black", highlightcolor="red", highlightthickness=2)
        self.command_path: dict[str, Callable | Base] = {}

    def create_button(self, row: int, column: int, text: str) -> tk.Button:
        button = tk.Button(self.root, text=text, width=10)
        button.grid(row=row, column=column, padx=5, pady=5, sticky='ew')
        return button

    def create_check_box(self, row: int, column: int, text: str) -> tk.Checkbutton:
        check_box = tk.Checkbutton(self.root, text=text)
        check_box.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')
        return check_box

    def create_combo_box(self, row: int, column: int, values: list) -> ttk.Combobox:
        combo_box = ttk.Combobox(self.root, values=values)
        combo_box.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')
        return combo_box

    def create_line_edit(self, row: int, column: int) -> tk.Entry:
        line_edit = ttk.Entry(self.root)
        line_edit.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')
        return line_edit

    def create_list_box(self, row: int, column: int) -> tk.Listbox:
        list_box = tk.Listbox(self.root)
        list_box.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')
        return list_box

    def grid(self, *args, **kwargs):
        self.root.grid(*args, **kwargs)

    def process(self, message: Message):
        if '.' in message.path:
            path, follow = message.path.split('.', 1)

            if path not in self.command_path:
                raise KeyError(f'{path} not in command path')

            if not isinstance(self.command_path[path], Base):
                raise TypeError(f'{self.command_path[path]} is not a Base')

            message.path = follow
            self.command_path[path].process(message)

        else:
            if message.path not in self.command_path:
                raise KeyError(f'{message.path} not in command path')

            if not callable(self.command_path[message.path]):
                raise TypeError(f'{self.command_path[message.path]} is not a callable')

            self.command_path[message.path](message)


if __name__ == '__main__':
    pass
