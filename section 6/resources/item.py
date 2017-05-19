# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
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
            item.insert()
        except:
            return {'msg': 'exception thrown'}, 500

        # should always return json/dic, cannot return objects
        return item.jsonify(), 201

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE name = ?"
        result = cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return {'msg': 'item is deleted!'}

    def put(self, name):
        # data = request.get_json()
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, data['price'])
        if item is None:
            try:
                updated_item.insert()
            except:
                return {'msg': 'an error occured while inserting'}, 500
        else:
            try:
                updated_item.update()
            except:
                return {'msg': 'an error occured while updating'}, 500
        return updated_item.jsonify()


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
