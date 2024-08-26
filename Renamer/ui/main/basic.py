# -*- coding:utf-8 -*-
# AUTHOR: Sun

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from ui.base import Base
from messager import Client, Message, MessageUser
from logging import getLogger

logger = getLogger(__name__)


class Basic(Base):
    def __init__(self, root: tk.Frame | tk.Tk, client: Client):
        super().__init__(root, 'basic', client)
        self.enable_child_folder_select = tk.BooleanVar()

        self.file_button = self.create_button(0, 0, '文件')
        self.folder_button = self.create_button(0, 1, '文件夹')
        self.enable_child_folder_check_box = self.create_check_box(0, 2, '子文件夹', self.enable_child_folder_select)
        self.restore_button = self.create_button(1, 0, '还原')
        self.delete_button = self.create_button(1, 1, '删除')
        self.clear_button = self.create_button(1, 2, '设置')

        for i in range(3):
            self.root.grid_columnconfigure(i, weight=10)
        for i in range(2):
            self.root.grid_rowconfigure(i, weight=10)

        self.command_path = {
            'click_file_button': self.select_file,
            'click_folder_button': self.select_folder,
        }

        self.file_button.bind('<ButtonRelease-1>', self.select_file)
        self.folder_button.bind('<ButtonRelease-1>', self.select_folder)

    def select_file(self, event):
        file_path = filedialog.askopenfilename()
        if not file_path:
            return
        message = Message(MessageUser.UI, MessageUser.ENGINE, 'select.file', {'file_path': file_path})
        self.client.send(message)

    def select_folder(self, event):
        folder_path = filedialog.askdirectory()
        if not folder_path:
            return
        message = Message(MessageUser.UI, MessageUser.ENGINE, 'select.folder',
                          {'folder_path': folder_path, 'enable_child_folder': self.enable_child_folder_select.get()})
        self.client.send(message)


if __name__ == '__main__':
    pass
