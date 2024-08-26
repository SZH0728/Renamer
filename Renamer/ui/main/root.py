# -*- coding:utf-8 -*-
# AUTHOR: Sun
import tkinter as tk

from messager import Client
from ui.base import Base
from ui.main.basic import Basic
from ui.main.confirm import Confirm
from ui.main.form import Form
from ui.main.method import *


class Frame(Base):
    def __init__(self, root: tk.Frame | tk.Tk, client: Client):
        super().__init__(root, 'main', client)

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        self.root.grid(column=0, row=0, sticky='nsew')

        self.root.grid_columnconfigure(0, weight=250)
        self.root.grid_columnconfigure(1, weight=330)
        self.root.grid_columnconfigure(2, weight=20)

        self.root.grid_rowconfigure(0, weight=20)
        self.root.grid_rowconfigure(1, weight=370)
        self.root.grid_rowconfigure(2, weight=10)

        self.form = Form(self.root, client)
        self.form.grid(column=0, row=0, rowspan=3, sticky='nsew')

        self.basic = Basic(self.root, client)
        self.basic.grid(column=1, row=0, columnspan=2, sticky='nsew')

        self.confirm = Confirm(self.root, client)
        self.confirm.grid(column=2, row=2, sticky='nsew')

        self.command_path = {
            'basic': self.basic,
            'confirm': self.confirm,
            'form': self.form,
        }


if __name__ == '__main__':
   pass
