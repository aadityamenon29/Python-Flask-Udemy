# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

app.secret_key = 'adi'

jwt = JWT(app, authenticate, identity)

# no need to jsonify, as flask_restful returns json versoin of dictionary

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

# to prevent python from running app if app.py is imported somewhere
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=4002, debug=True)
