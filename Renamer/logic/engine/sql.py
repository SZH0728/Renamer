# -*- coding:utf-8 -*-
# AUTHOR: Sun

from sqlite3 import connect

from logic.engine.base import File, Base


class Sqlite(Base):
    def __init__(self, db_path: str = None):
        if db_path:
            self.connect = connect(db_path)
        else:
            self.connect = connect(':memory:')

        self.cursor = self.connect.cursor()

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS files ( 
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                current_path TEXT NOT NULL,
                current_name TEXT NOT NULL,
                target_path TEXT NOT NULL,
                target_name TEXT NOT NULL
                );
        ''')
        self.connect.commit()

    def __del__(self):
        self.cursor.close()
        self.connect.close()

    def insert(self, file: File) -> File:
        self.cursor.execute(
            'INSERT INTO files (current_path, current_name, target_path, target_name) VALUES (?, ?, ?, ?);',
            (file.current_path, file.current_name, file.target_path, file.target_name)
        )
        self.connect.commit()
        return File(**self.cursor.execute('SELECT * FROM files WHERE id = ?;', (self.cursor.lastrowid,)).fetchone())

    def select(self, path: str = None, name: str = None, id_: int = None,
               current: bool = True, limit: int = None) -> list[File]:
        target = {}

        if id_:
            target['id'] = id_
        if path:
            target['path'] = path
        if name: 
            target['name'] = name

        sql = ''
        for key, value in target.items():
            sql += f'{f"current_{key}" if current else f"target_{key}"} = "{value}" AND '
        sql = f'SELECT * FROM files WHERE {sql[:-4]} {f"LIMIT {limit}" if limit else ""};'

        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return [File(**row) for row in result]

    def update(self, file: File) -> File:
        self.cursor.execute(
            'UPDATE files SET current_path = ?, current_name = ?, target_path = ?, target_name = ? WHERE id = ?;',
            (file.current_path, file.current_name, file.target_path, file.target_name, file.id)
        )
        self.connect.commit()
        return File(**self.cursor.execute('SELECT * FROM files WHERE id = ?;', (file.id,)).fetchone())


if __name__ == '__main__':
    Sqlite('./data.db')
