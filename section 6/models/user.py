# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sqlite3


class UserModel:

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        with open("new_test.txt", "a") as fo:
            fo.write("UserModel - find_by_username\n")
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * from users where username = ?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)    # row[0], row[1], row[2]
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * from users where id = ?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)    # row[0], row[1], row[2]
        else:
            user = None

        connection.close()
        return user
