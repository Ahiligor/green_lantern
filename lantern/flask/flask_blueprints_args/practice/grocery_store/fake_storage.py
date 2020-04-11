from itertools import count

from grocery_store.store_app import NoSuchUserError


class Repository:
    def __init__(self):
        self._db = {}
        self._id_counter = count(1)

    def add(self, item):
        item_id = next(self._id_counter)
        self._db[item_id] = item
        return item_id


class FakeStorage:
    def __init__(self):
        self._users = FakeUsers()
        self._goods = FakeGoods()

    @property
    def users(self):
        return self._users

    @property
    def goods(self):
        return self._goods


class FakeUsers(Repository):
    def get_user_by_id(self, user_id):
        try:
            return self._db[user_id]
        except KeyError:
            raise NoSuchUserError(user_id)

    def update_user_by_id(self, user_id, user):
        try:
            self._db[user_id] = user
        except KeyError:
            raise NoSuchUserError(user_id)


class FakeGoods(Repository):
    def add_many(self, items):
        for item in items:
            self.add(item)
        return len(items)

    def get_all(self):
        return [
            {**item, 'id': item_id} for item_id, item in self._db.items()
        ]
