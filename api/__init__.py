# from flask import Flask, Blueprint
# from flask_pymongo import PyMongo
# from flask_restplus import Resource, Api, fields
# from . import user_api


# def create_app(object_name):
#     app = Flask(__name__)
#     app.config.from_object(object_name)
#     app.config['MONGO_DBNAME'] = 'test_database'
#     app.config['MONGO_URI'] = 'mongodb://localhost:27017'

#     mongo = PyMongo(app)
#     blueprint = Blueprint(app, __name__, url_prefix='/api')
#     api = Api(blueprint, doc='/documentation')
#     app.register_blueprint(blueprint)
#     return app

from flask import Blueprint
from flask_restplus import Api


blueprint = Blueprint('api', __name__, url_prefix='/api')
api_user = Api(blueprint, doc='/doc')
