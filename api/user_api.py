from flask_restplus import Resource
from . import api_user

# @api_user.route('/user')
# class User(Resource):
#     def get(self):
#         return {'hello': 'world!!'}
#     def post(self):
#         user_db = mongo.db.users
#         user.insert({'name': 'kk', 'phone': '010-3333-3333'})
#         return {'result': 'Added User!'}, 201

@api_user.route('/user')
class User(Resource):
    def get(self):
        return {'user': 'daeun'}
    def post(self):
        return {'hey': 'dd'}