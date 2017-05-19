# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sqlite3
import sys
sys.path.insert(0, 'A:/Internship - Summer 2017/Python flask/section 6')
from db import db


class UserModel(db.Model):

    # the following code creates a mapping between the attributes of the objects of this class listed in init method, and the columns of the db table users
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

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
