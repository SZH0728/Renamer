# -*- coding:utf-8 -*-
# AUTHOR: Sun

import tkinter as tk
from tkinter import ttk

from ui.base import Base


class Form(Base):
    def __init__(self, root: tk.Frame | tk.Tk):
        super().__init__(root, 'form')

        self.list_box = self.create_list_box(0, 0)
        self.line_edit = self.create_line_edit(1, 0)

        self.root.grid_rowconfigure(0, weight=380)
        self.root.grid_rowconfigure(1, weight=20)

        self.root.grid_columnconfigure(0, weight=1)


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('600x400')
    form = Form(window)
    window.mainloop()
