# -*- coding:utf-8 -*-
# AUTHOR: Sun

import tkinter as tk
from tkinter import ttk

from ui.base import Base
from messager import Client


class Confirm(Base):
    def __init__(self, root: tk.Frame | tk.Tk, client: Client):
        super().__init__(root, 'confirm', client)

        self.revocation_button = self.create_button(0, 0, '撤销')
        self.confirm_button = self.create_button(0, 1, '确认')

        for i in range(2):
            self.root.grid_columnconfigure(i, weight=1)
        self.root.grid_rowconfigure(0, weight=1)


if __name__ == '__main__':
    pass
