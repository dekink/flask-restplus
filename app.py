from flask import Flask, Blueprint
from flask_restplus import Resource, Api, fields


app = Flask(__name__)
blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, doc='/documentation')

app.register_blueprint(blueprint)

app.config['SWAGGER_UI_JSONEDITOR'] = True

a_language = api.model('Language', {'language': fields.String('The language.'),
                                    'id': fields.Integer('ID')})

languages = []
python = {'language': 'Python', 'id': 1}
languages.append(python)

@api.route('/language')
class Launguage(Resource):

    @api.marshal_with(a_language, envelope='the_data')
    def get(self):
        return languages

    @api.expect(a_language)
    def post(self):
        new_language = api.payload
        new_language['id'] = len(languages) + 1
        languages.append(new_language)
        return {'result': 'Language added'}, 201

@api.route('/user')
class User(Resource):
    def get(self):
        return {'user': 'daeun'}
    def post(self):
        return {'hey': 'dd'}

if __name__ == '__main__':
    app.run(debug=True)
