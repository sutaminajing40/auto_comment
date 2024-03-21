# from db import configure_database, db
from db import configure_database, db
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api, Resource
from models.requests import comments_post_requests
from models.validators import comments_validator
from services.get_db import get_comments
from services.post_db import save_comment

app = Flask(__name__)
configure_database(app)
migrate = Migrate(app, db, directory="app/migrations")
api = Api(app)


@api.route('/comments')
class Comments(Resource):
    def get(self):
        results = get_comments()
        return {'results': results}

    @api.expect(comments_post_requests, validate=True)
    def post(self):
        args = comments_post_requests.parse_args()
        if not comments_validator(args['content']):
            return {"result": "content内容が無効です。"}, 400

        results = save_comment(args['content'])
        return {"result": results}, 201

    def delete(self):
        return {'hello': 'world'}


if __name__ == "__main__":
    load_dotenv()
    app.run(port=8888)
