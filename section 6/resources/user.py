# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from flask_restful import Resource, reqparse
import sqlite3
import sys
sys.path.insert(0, 'A:/Internship - Summer 2017/Python flask/section 6')
from models.user import UserModel


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        with open("new_test.txt", "a") as fo:
            fo.write("UserRegister - post\n")
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {'message': 'User already exists'}, 400
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))
        connection.commit()
        connection.close()
        return {'message': 'user created successfully'}, 201
