from api import api
from flask_restx import Resource
from models.requests import parser


@api.route('/comments')
class Comments(Resource):
    def get(self):
        return {'hello': 'world'}

    @api.expect(parser)
    def post(self):
        return {'hello': 'world'}

    def delete(self):
        return {'hello': 'world'}
