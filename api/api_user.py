from flask_restplus import Resource
from . import swagger as sw
from . import model as m
from flask import request
import json


user_doc = []
doc = {
    'name': 'daeun',
    'phone': '010-5555-5555'
}


@sw.api_user.route('/<string:oid>')
class User(Resource):
    @sw.api_user.marshal_with(m.user_db, envelope='result')
    def get(self, oid):
        for user in user_doc:
            if user['id'] == int(oid):
                return {
                    'result': user
                }
        return {
            'result': 'not found user'
        }

    @sw.api_user.expect(m.user_db) #payload
    def post(self, oid):
        doc = sw.api_user.payload
        doc['id'] = len(user_doc)
        user_doc.append(doc)
        return {
            'result': {
                'oid': oid,
                'message': 'user added'
        }}

    @sw.api_user.expect(sw.user_put_parser)
    def put(self, oid):
        form_data = request.form.to_dict()
        for user in user_doc:
            if user['id'] == int(oid):
                user['param'] = form_data['param']
                user['in_files'] = form_data['in_files']
                return {
                    'result': user
                }
        return {'result': 'not found user'}


@sw.api_user.route('')
class UserParams(Resource):
    @sw.api_user.doc(params={'name': 'The User name'})
    def get(self):
        name = request.args.get('name')
        for user in user_doc:
            if user['name'] == name:
                return {
                    'result': user
                }
        return {'result': 'not found'}

    # def get(self):
    #     return {
    #         'result': user_doc
    #     }

    @sw.api_user.expect(sw.user_post_parser, sw.kk_parser)
    def post(self):
        form_data = request.form.to_dict()
        data = json.loads(form_data["json_data"])
        return {
            'result': data
        }
    
    def delete(self):
        user_doc = []
        return {
            'result': 'delete users'
        }

@sw.api_user.route('/data')
class UserFormData(Resource):
    @sw.api.representation('multipart/form-data')
    @sw.api_user.expect(m.user_post) #payload
    def post(self, oid):
        form_data = request.form.to_dict()
        data = json.loads(form_data['json_data'])
        print(data)
        # doc = sw.api_user.payload
        # user_doc.append(doc)
        return {
            'result': {
                'oid': oid,
                'message': 'user added'
        }}

@sw.api_user.route('/random')
@sw.api_user.doc(params={'user_id': 'The User ID'})
class Random(Resource):
    def get(self):
        user_id = request.args.get('user_id')
        return {
            'result': user_id, 
            'status': 'random'
        }
