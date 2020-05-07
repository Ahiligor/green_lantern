from itertools import count
from store_app import NoSuchUserError, NoSuchStoreError, NoSuchManagerIDError


class FakeStorage:
    def __init__(self):
        self._users = FakeUsers()
        self._goods = FakeGoods()
        self._stores = FakeStores()

    @property
    def users(self):
        return self._users

    @property
    def goods(self):
        return self._goods

    @property
    def stores(self):
        return self._stores


class FakeUsers:
    def __init__(self):
        self._users = {}
        self._id_counter = count(1)

    def add(self, user):
        user_id = next(self._id_counter)
        self._users[user_id] = user
        return user_id

    def get_user_by_id(self, user_id):
        try:
            return self._users[user_id]
        except KeyError:
            raise NoSuchUserError(user_id)

    def update_user_by_id(self, user_id, user):
        if user_id in self._users:
            self._users[user_id] = user
        else:
            raise NoSuchUserError(user_id)


class FakeGoods:
    def __init__(self):
        self._goods = {}
        self._id_counter = count(1)

    def add(self, products):
        good_qty = 0
        for good in products:
            good_id = next(self._id_counter)
            good_qty += 1
            self._goods[good_id] = good
        return good_qty

    def get_goods(self):
        response = []
        # import pdb;pdb.set_trace()
        for key, values in self._goods.items():
            response.append({"id": key, **values})
        return response

    def update_goods(self, goods):
        updated = 0
        no_id = []
        for good in goods:
            good_id = good['id']
            if good_id in self._goods:
                self._goods[good_id] = good
                updated += 1
            else:
                no_id.append(good['id'])
        return {'successfully_updated': updated, 'errors': {'no such id in goods': no_id}}


class FakeStores:
    def __init__(self):
        self._stores = {}
        self._id_counter = count(1)

    def add(self, store):
        try:
            store_id = next(self._id_counter)
            self._stores[store_id] = store
            return store_id
        except KeyError:
            raise NoSuchUserError(store['manager_id'])

    def get_store_by_id(self, store_id):
        # import pdb;pdb.set_trace()
        try:
            return self._stores[store_id]
        except KeyError:
            raise NoSuchStoreError(store_id)

    def update_store_by_id(self, store_id, store):
        if store_id in self._stores:
            self._stores[store_id] = store
        else:
            raise NoSuchStoreError(store_id)
