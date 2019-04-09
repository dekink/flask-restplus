from flask_restplus import Resource
from . import swagger as sw


@sw.api_audio.route('')
class Audio(Resource):
    def get(self):
        return {'user': 'daeun'}

    @sw.api_user.doc(parser=sw.parser)
    def post(self):
        args = sw.parser.parse_args()
        return {'result': args['actor_id']}, 200

    def put(self):
        return {'result': 'put'}


@sw.api_audio.route('/<string:oid>')
class AudioId(Resource):
    def post(self, oid):
        return {
            'result': oid
        }
