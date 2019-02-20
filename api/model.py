from .swagger import api
from flask_restplus import fields
import json


user_db = api.model('user', {
    'id': fields.Integer('ID'),
    'name': fields.String(required=True, description='The user name'),
    'phone': fields.String(required=True, description='The phone number')
})

user_post = api.model('user_post', {
    'json_data': fields.Nested(user_db, description='The user data', location='form'),
    'user_url': fields.String(description='The user image url', location='files')
})
