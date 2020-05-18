"""Flask server to emulate todo-list backend."""
import json
from flask import Flask, jsonify, request
app = Flask(__name__)

_lists = {}


@app.route('/lists', methods=['GET'])
def get_lists():
    lists = [dict(id=index, name=name) for index, name in enumerate(_lists)]
    return jsonify(dict(lists=lists))


@app.route('/lists', methods=['POST'])
def create_list():
    data = dict(request.json)
    list_name = data['list']['name']
    _lists[list_name] = dict(name=data['list']['name'], items={})
    return '', 200


@app.route('/authenticate', methods=['POST'])
def auth():
    return jsonify(dict(token='secret'))


@app.route('/lists/<int:list_id>', methods=['GET'])
def get_list(list_id):
    lists = [name for name in _lists.values()]
    output = dict(list=lists[list_id])
    return jsonify(output)


@app.route('/lists/<int:list_id>/items', methods=['POST'])
def create_task(list_id):
    data = dict(request.json)
    lists = [name for name in _lists.values()]
    _list = lists[list_id]
    _list['items'][data['item']['name']] = {}
    return '', 200
