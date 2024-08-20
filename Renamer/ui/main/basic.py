# -*- coding:utf-8 -*-
# AUTHOR: Sun

import tkinter as tk
from tkinter import ttk

from ui.base import Base


class Basic(Base):
    def __init__(self, root: tk.Frame | tk.Tk):
        super().__init__(root, 'basic')

        self.file_button = self.create_button(0, 0, '文件')
        self.folder_button = self.create_button(0, 1, '文件夹')
        self.enable_child_folder_check_box = self.create_check_box(0, 2, '子文件夹')
        self.restore_button = self.create_button(1, 0, '还原')
        self.delete_button = self.create_button(1, 1, '删除')
        self.clear_button = self.create_button(1, 2, '清空')

        for i in range(3):
            self.root.grid_columnconfigure(i, weight=10)
        for i in range(2):
            self.root.grid_rowconfigure(i, weight=10)


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('600x400')
    basic = Basic(window)
    window.mainloop()
