from flask_restplus import Namespace
from flask import Blueprint
from flask_restplus import Api

#namespace
api_user = Namespace('user', description='api_user.py')
api_audio = Namespace('audio', description='api_audio.py')

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, doc='/documentation')
api.add_namespace(api_audio)
api.add_namespace(api_user)

#query
parser = api.parser()
parser.add_argument('actor_id', type=str, required=True)

user_post_parser = api.parser()
user_post_parser.add_argument('Content-Type', location='form')
