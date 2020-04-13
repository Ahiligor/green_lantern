import inject
from flask import Flask
from flask_restful import Api

from errors import NoSuchUserError, my_error_handler, NoSuchStoreError
from fake_storage import FakeStorage
from routes import users_bl, goods_bl
from routes.stores import Store


def configure(binder):
    db = FakeStorage()
    binder.bind('DB', db)


def make_app():
    # configure our database
    inject.clear_and_configure(configure)

    app = Flask(__name__)
    # API
    api = Api(app)
    api.add_resource(Store, "/store", "/store/<int:store_id>")
    # register blueprints and error handlers
    app.register_blueprint(users_bl)
    app.register_blueprint(goods_bl)

    app.register_error_handler(NoSuchUserError, my_error_handler)
    app.register_error_handler(NoSuchStoreError, my_error_handler)
    return app
