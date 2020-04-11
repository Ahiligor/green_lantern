from flask import Flask, jsonify, request

import inject


class NoSuchUserError(Exception):
    def __init__(self, user_id):
        self.message = f'No such user_id {user_id}'


app = Flask(__name__)


@app.errorhandler(NoSuchUserError)
def my_error_handler(e):
        return jsonify({'error': e.message}), 404


@app.route('/users', methods=['POST'])
def create_user():
    db = inject.instance('DB')
    user_id = db.users.add(request.json)
    return jsonify({'user_id': user_id}), 201


@app.route('/users/<int:user_id>')
def get_user(user_id):
    db = inject.instance('DB')
    user = db.users.get_user_by_id(user_id)
    return jsonify(user)


@app.route('/goods', methods=['POST'])
def create_goods():
    db = inject.instance('DB')
    number_of_created_goods = db.goods.add_many(request.json)
    return jsonify({'number of items created': number_of_created_goods}), 201


@app.route('/goods')
def get_goods():
    db = inject.instance('DB')
    return jsonify(db.goods.get_all())
