# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask, jsonify, request

# __name__ gives each file a unique name.
# app is a new object of Flask class
app = Flask(__name__)

# tell the app what requests it'll
# understand. Use decorators
# http://google.com/

# / : means root page or home page or an endpoint
# simply a forward slash means home page


stores = [

    {
        'name': 'Store_1',
        'items': [
            {
                'name': 'lemon',
                        'price': '20'
            },
            {
                'name': 'orange',
                        'price': '40'
            }

        ]

    },
    {
        'name': 'Store_2',
        'items': [
            {
                'name': 'apple',
                        'price': '10'
            },
            {
                'name': 'banana',
                        'price': '60'
            }

        ]
    }
]


@app.route('/')
def home():
    return 'Hello world!'


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_data = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_data)
    return jsonify(stores)


@app.route('/store/<string:name>')
def get_store(name):
    for x in stores:
        if x['name'] == name:
            return jsonify(x)
    return jsonify({'message': 'not found!'})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
    return jsonify(store['items'])


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return 'not found'


# http://localhost:5000/store/getSI/?a=Store_2&b=apple
@app.route('/store/getSI/', methods=['GET'])
def getSI():
    for store in stores:
        if store['name'] == request.args.get('a'):
            for item in store['items']:
                if item['name'] == request.args.get('b'):
                    return item['price']
    return 'store not found'


app.run(port=5000)
