from flask import Blueprint, request
from flask_restplus import Api, reqparse, Namespace


authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, doc='/documentation', authorizations=authorizations, security='apikey')

#namespace
api_user = Namespace('user', description='api_user.py')
api_audio = Namespace('audio', description='api_audio.py')
api.add_namespace(api_audio)
api.add_namespace(api_user)

#parser
parser = api.parser()
parser.add_argument('actor_id', type=str, required=True)

user_post_parser = api.parser()
user_post_parser.add_argument('json_data', type=str, location='form')
# user_post_parser.add_argument('user_url', type=str, location='files')

kk_parser = api.parser()
kk_parser.add_argument('user_url', type=str, location='files')

user_put_parser = api.parser()
user_put_parser.add_argument('param', type=int, help='Some param', location='form')
user_put_parser.add_argument('in_files', type=str, location='files')

#header
header_arguments = reqparse.RequestParser()
header_arguments.add_argument('header', type=str, required=True, location='header')


