# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList
import sys
import os


app = Flask(__name__)
api = Api(app)

app.secret_key = 'adi'

jwt = JWT(app, authenticate, identity)

# no need to jsonify, as flask_restful returns json versoin of dictionary

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

# to prevent python from running app if app.py is imported somewhere
if __name__ == '__main__':
    app.run(port=4001)
