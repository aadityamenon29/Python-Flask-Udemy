# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
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
        with open("test.txt", "a") as fo:
            fo.write("This Data\n")
        item = Item.find_by_name(name)
        if item:
            return item
        return {'msg': 'item not found'}, 404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items where name = ?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            return {'item': row[0], 'price': row[1]}
        return None

    def post(self, name):
        if Item.find_by_name(name):
            return {'message': "An item with name '{}' already exists".format(name)}, 400
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        try:
            Item.insert(item)
        except:
            return {'msg': 'exception thrown'}, 500

        # should always return json/dic, cannot return objects
        return item, 201

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO items VALUES(?,?)"
        result = cursor.execute(query, (item['name'], item['price']))
        connection.commit()
        connection.close()

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE name = ?"
        result = cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return {'msg': 'item is deleted!'}

    def put(self, name):
        #data = request.get_json()
        data = Item.parser.parse_args()
        item = Item.find_by_name(name)
        updated_item = {'name': name, 'price': data['price']}
        if item is None:
            try:
                Item.insert(updated_item)
            except:
                return {'msg': 'an error occured while inserting'}, 500
        else:
            try:
                Item.update(updated_item)
            except:
                return {'msg': 'an error occured while inserting'}, 500
        return updated_item

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "UPDATE items SET price = ? WHERE name = ?"
        result = cursor.execute(query, (item['price'], item['name']))
        connection.commit()
        connection.close()


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
