# -*- coding:utf-8 -*-
# AUTHOR: Sun


import tkinter as tk

from messager import Client
from ui.main.root import Frame


class Root(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('600x400')

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.main = Frame(self)
        self.main.grid(column=0, row=0, sticky='nsew')


if __name__ == '__main__':
    app = Root()
    app.mainloop()
