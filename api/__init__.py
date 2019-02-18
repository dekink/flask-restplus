
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


from . import api_user
from . import api_audio
from . import swagger
