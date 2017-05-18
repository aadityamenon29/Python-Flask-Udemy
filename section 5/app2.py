# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from user import UserRegister
import sys
import os


app = Flask(__name__)
api = Api(app)

app.secret_key = 'adi'

jwt = JWT(app, authenticate, identity)

items = []

# no need to jsonify, as flask_restful returns json versoin of dictionary


class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists".format(name)}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('price', type=float, required=True, help="This field cannot be left blank!")
        #data = request.get_json()
        data = parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        with open("test.txt", "a") as fo:
            fo.write("This Data\n")
        with open("test.txt", "a") as fo:
            fo.write("This Dataxxxxxxx\n")
        return {'itemss': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
app.run(port=4001)
