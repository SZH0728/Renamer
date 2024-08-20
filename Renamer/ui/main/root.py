# -*- coding:utf-8 -*-
# AUTHOR: Sun
import tkinter as tk

from ui.base import Base
from ui.main.basic import Basic
from ui.main.confirm import Confirm
from ui.main.form import Form
from ui.main.method import *


class Frame(Base):
    def __init__(self, root: tk.Frame | tk.Tk):
        super().__init__(root, 'main')

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        self.root.grid(column=0, row=0, sticky='nsew')

        self.root.grid_columnconfigure(0, weight=250)
        self.root.grid_columnconfigure(1, weight=330)
        self.root.grid_columnconfigure(2, weight=20)

        self.root.grid_rowconfigure(0, weight=20)
        self.root.grid_rowconfigure(1, weight=370)
        self.root.grid_rowconfigure(2, weight=10)

        self.form = Form(self.root)
        self.form.grid(column=0, row=0, rowspan=3, sticky='nsew')

        self.basic = Basic(self.root)
        self.basic.grid(column=1, row=0, columnspan=2, sticky='nsew')

        self.confirm = Confirm(self.root)
        self.confirm.grid(column=2, row=2, sticky='nsew')


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('600x400')
    frame = Frame(window)
    window.mainloop()
