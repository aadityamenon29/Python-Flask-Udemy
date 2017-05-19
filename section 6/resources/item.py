# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sys
sys.path.insert(0, 'A:/Internship - Summer 2017/Python flask/section 6')
from models.item import ItemModel
import sqlite3


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    @jwt_required()
    def get(self, name):
        with open("new_test.txt", "a") as fo:
            fo.write("GET ITEM\n")
        item = ItemModel.find_by_name(name)
        if item:
            return item.jsonify()
        return {'msgx': 'item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists".format(name)}, 400
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])
        try:
            item.save_to_db()
        except:
            return {'msg': 'exception thrown'}, 500

        # should always return json/dic, cannot return objects
        return item.jsonify(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete()
        return {'msg': 'item deleted yo'}

    def put(self, name):
        # data = request.get_json()
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, data['price'])
        else:
            item.price = data['price']

        item.save_to_db()
        return item.jsonify()


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * from items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})
        connection.close()
        return items
