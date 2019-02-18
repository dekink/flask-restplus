from flask_restplus import Resource
from . import swagger as sw
from . import model as m
from flask import request
import json


# @api_user.route('/user')
# class User(Resource):
#     def get(self):
#         return {'hello': 'world!!'}
#     def post(self):
#         user_db = mongo.db.users
#         user.insert({'name': 'kk', 'phone': '010-3333-3333'})
#         return {'result': 'Added User!'}, 201

user_doc = []
doc = {
    'name': 'daeun',
    'phone': '010-5555-5555'
}

@sw.api_user.route('/<string:num>')
@sw.api_user.doc(params={'num': 'The number'})
class User(Resource):
    @sw.api_user.marshal_with(m.user_db, envelope='result')
    def get(self, num):
        num = int(num) + 1
        return user_doc

    @sw.api.representation('multipart/form-data')
    @sw.api_user.expect(m.user_db) #payload
    # @sw.api_user.doc(body=m.user_post, parser=user_post_parser)
    def post(self, num):
        # form_data = request.form.to_dict()
        # data = json.loads(form_data['json_data'])
        doc = sw.api_user.payload
        user_doc.append(doc)
        return {
            'result': {
                'number': num,
                'status': 'added'
        }}
