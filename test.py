# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sqlite3


connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password, text)"

cursor.execute(create_table)

user = (1, 'jo', 'jo')

insert_query = "INSERT INTO users(id, username, password) VALUES (?, ?, ?)"

cursor.execute(insert_query, user)

users = [
    (2, 'ra', 'ra'),
    (3, 'an', 'an')
]

cursor.executemany(insert_query, users)

show = "SELECT * from users"

for row in cursor.execute(show):
    print(row)


connection.commit()
connection.close()
