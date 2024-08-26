# -*- coding:utf-8 -*-
# AUTHOR: Sun

from abc import ABC, abstractmethod
from typing import Callable
import tkinter as tk
from tkinter import ttk
from logging import getLogger

from messager import Message, Client

logger = getLogger(__name__)


class Process(object):
    def __init__(self):
        self.command_path: dict[str, Callable | Base] = {}

    def process(self, message: Message):
        if '.' in message.path:
            path, follow = message.path.split('.', 1)

            if path not in self.command_path:
                logger.error(f'{path} not in command path')
                raise KeyError(f'{path} not in command path')

            if not isinstance(self.command_path[path], Base):
                logger.error(f'{self.command_path[path]} is not a Base')
                raise TypeError(f'{self.command_path[path]} is not a Base')

            message.path = follow
            logger.debug(f'send message to {message.path}')
            self.command_path[path].process(message)

        else:
            if message.path not in self.command_path:
                logger.error(f'{message.path} not in command path')
                raise KeyError(f'{message.path} not in command path')

            if not callable(self.command_path[message.path]):
                logger.error(f'{self.command_path[message.path]} is not a callable')
                raise TypeError(f'{self.command_path[message.path]} is not a callable')

            logger.debug(f'process command {message.path} with {message.content}')
            self.command_path[message.path](message)


class Base(ABC, Process):
    def __init__(self, root: tk.Frame | tk.Tk, name: str, client: Client):
        super().__init__()
        self.root = tk.Frame(root, name=name, highlightbackground="black", highlightcolor="red", highlightthickness=2)

        self.client = client

    def create_button(self, row: int, column: int, text: str) -> tk.Button:
        button = tk.Button(self.root, text=text, width=10)
        button.grid(row=row, column=column, padx=5, pady=5, sticky='ew')
        logger.debug(f'create button {button} on ({row},{column}) with {text}')
        return button

    def create_check_box(self, row: int, column: int, text: str,
                         variable: tk.IntVar | tk.BooleanVar = None) -> tk.Checkbutton:
        check_box = tk.Checkbutton(self.root, text=text, variable=variable)
        check_box.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')
        logger.debug(f'create check box {check_box} on ({row},{column}) with {text}')
        return check_box

    def create_combo_box(self, row: int, column: int, values: list) -> ttk.Combobox:
        combo_box = ttk.Combobox(self.root, values=values)
        combo_box.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')
        logger.debug(f'create combo box {combo_box} on ({row},{column}) with {values}')
        return combo_box

    def create_line_edit(self, row: int, column: int) -> tk.Entry:
        line_edit = ttk.Entry(self.root)
        line_edit.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')
        logger.debug(f'create line edit {line_edit} on ({row},{column})')
        return line_edit

    def create_list_box(self, row: int, column: int) -> tk.Listbox:
        list_box = tk.Listbox(self.root)
        list_box.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')
        logger.debug(f'create list box {list_box} on ({row},{column})')
        return list_box

    def grid(self, *args, **kwargs):
        self.root.grid(*args, **kwargs)

    def send(self, message: Message):
        logger.debug(f'send message {message}')
        self.client.send(message)


if __name__ == '__main__':
    pass
