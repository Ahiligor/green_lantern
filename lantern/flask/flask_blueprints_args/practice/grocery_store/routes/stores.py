import inject
from flask import request
from flask_restful import Resource


class Store(Resource):

    def get(self, store_id):
        db = inject.instance('DB')
        store = db.stores.get_store_by_id(store_id)
        return store

    def post(self):
        db = inject.instance('DB')
        store_id = db.stores.add(request.json)
        return {'store_id': store_id}, 201

    def put(self, store_id):
        db = inject.instance('DB')
        db.stores.update_store_by_id(store_id, request.json)
        return {'status': 'success'}
