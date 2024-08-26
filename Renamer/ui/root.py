# -*- coding:utf-8 -*-
# AUTHOR: Sun


import tkinter as tk

from messager import Client, Message, Server
from ui.main.root import Frame
from ui.base import Process


class Root(Process):
    def __init__(self, client: Client, *args, **kwargs):
        super().__init__()
        self.client = client

        self.root = tk.Tk(*args, **kwargs)
        self.root.geometry('600x400')

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.main = Frame(self.root, self.client)
        self.main.grid(column=0, row=0, sticky='nsew')

        self.root.after(100, self.process)

        self.command_path = {
            'main': self.main
        }

    def mainloop(self):
        self.root.mainloop()

    def process(self):
        while not self.client.is_empty():
            message: Message = self.client.read()
            super().process(message)


class Main(object):
    def __init__(self, client: Client):
        self.app = Root(client)
        self.app.mainloop()


if __name__ == '__main__':
    from logging import basicConfig, DEBUG
    basicConfig(level=DEBUG)

    server = Server()
    client_first, client_second = server.get_client()

    app = Root(client_first)
    app.mainloop()
