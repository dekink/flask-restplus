from flask_restplus import Resource
from . import swagger as sw
from . import model as m
from flask import request, send_file, redirect
import json
from io import BytesIO
from functools import wraps


user_doc = []
doc = {
    'name': 'daeun',
    'phone': '010-5555-5555'
}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']
        if not token:
            return {'message': 'Token is missing.'}, 401
        if token != 'my_token':
            return {'message': 'Your token is wrong!'}, 401

        print('TOKEN: {}'.format(token))
        return f(*args, **kwargs)

    return decorated

# @sw.api.representation('multipart/form-data')
# @sw.api.representation('image/jpeg')
@sw.api_user.route('/<string:oid>')
class User(Resource):
    @sw.api_user.marshal_with(m.user_db, envelope='result')
    @token_required
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
    @token_required
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
    @token_required
    def put(self, oid):
        form_data = request.form.to_dict()
        for user in user_doc:
            if user['id'] == int(oid):
                user['param'] = form_data['param']
                user['in_files'] = form_data['in_files']
                return {
                    'result': user
                }
        return {
            'result': 'not found user'
        }


@sw.api_user.route('')
class UserParams(Resource):
    # @token_required
    # def get(self):
    #     print('keim')
    #     return {'result': user_doc}

    @token_required
    def get(self):
        with open('api/img/cat.jpg', 'rb') as f:
            img_file = BytesIO(f.read())
        return send_file(img_file, mimetype='image/jpeg', attachment_filename='cat.jpg', cache_timeout=-1)

    @token_required
    @sw.api_user.expect(sw.user_post_parser, sw.kk_parser)
    def post(self):
        form_data = request.form.to_dict()
        data = json.loads(form_data["json_data"])
        return {
            'result': data
        }
    
    @token_required
    def delete(self):
        user_doc = []
        return {
            'result': 'delete users'
        }

@sw.api_user.route('/data')
class UserFormData(Resource):
    @token_required
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
            }
        }


@sw.api_user.route('/something')
@sw.api_user.doc(params={'user_id': 'The User ID'})
class Random(Resource):
    @token_required
    @sw.api_user.hide
    def get(self):
        user_id = request.args.get('user_id')
        return {
            'result': user_id, 
            'status': 'random'
        }


@sw.api_user.route('/redirect')
class Redirect(Resource):
    @token_required
    def get(self):
        print('in redirect get')
        return redirect('http://127.0.0.1:5000/api/user/something')
