# -*- coding:utf-8 -*-
# AUTHOR: Sun

import tkinter as tk
from tkinter import ttk

from ui.base import Base


class Confirm(Base):
    def __init__(self, root: tk.Frame | tk.Tk):
        super().__init__(root, 'confirm')

        self.revocation_button = self.create_button(0, 0, '撤销')
        self.confirm_button = self.create_button(0, 1, '确认')

        for i in range(2):
            self.root.grid_columnconfigure(i, weight=1)
        self.root.grid_rowconfigure(0, weight=1)


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('600x400')
    confirm = Confirm(window)
    window.mainloop()
