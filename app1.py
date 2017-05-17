# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


items = []

# no need to jsonify, as flask_restful returns json versoin of dictionary


class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404

    def post(self, name):
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=4000, debug=True)
