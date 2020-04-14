import inject
from flask import request
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('name', required=False, type=str)


class Store(Resource):

    def get(self, store_id=None):
        db = inject.instance('DB')
        if store_id is not None:
            store = db.stores.get_store_by_id(store_id)
            return store
        else:
            args = parser.parse_args()
            name = args["name"]
            store = db.stores.get_store_by_name(name)
            return store

    def post(self):
        db = inject.instance('DB')
        store_id = db.stores.add(request.json)
        return {'store_id': store_id}, 201

    def put(self, store_id):
        db = inject.instance('DB')
        db.stores.update_store_by_id(store_id, request.json)
        return {'status': 'success'}

# @stores_bl.route('/store', methods=['POST'])
# def create_store():
#     db = inject.instance('DB')
#     store_id = db.stores.add(request.json)
#     return jsonify({'store_id': store_id}), 201


# @stores_bl.route('/store/<int:store_id>')
# def get_store(store_id):
#     db = inject.instance('DB')
#     store = db.stores.get_store_by_id(store_id)
#     return jsonify(store)


# @stores_bl.route('/store/<int:store_id>', methods=['PUT'])
# def update_store(store_id):
#     db = inject.instance('DB')
#     db.stores.update_store_by_id(store_id, request.json)
#     return jsonify({'status': 'success'})
