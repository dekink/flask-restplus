from .swagger import api
from flask_restplus import fields

user_db = api.model('user', {
    'name': fields.String(required=True, description='The user name'),
    'phone': fields.String(required=True, description='The phone number')
})

# user_post = api.model('user_post', {
#     'json_data' : {
#         'name': fields.String(required=True, description='The user name'),
#         'phone': fields.String(required=True, description='The phone number')}
# })
