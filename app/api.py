# from db import configure_database, db
from db import configure_database, db
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api, Resource
from models.requests import (comments_post_requests,
                             generate_comment_get_requests)
from models.validators import comments_validator
from services.comments.delete_db import delete_db
from services.comments.get_db import get_comments
from services.comments.post_db import save_comment
from services.generate_comment.generate_comment import generate_comment

app = Flask(__name__)
configure_database(app)
migrate = Migrate(app, db, directory="app/migrations")
api = Api(app)


@api.route('/comments')
class Comments(Resource):
    def get(self):
        results = get_comments()
        return {'result': results}

    @api.expect(comments_post_requests, validate=True)
    def post(self):
        args = comments_post_requests.parse_args()
        if not comments_validator(args['content']):
            return {"result": "content内容が無効です。"}, 400

        results = save_comment(args['content'])
        return {"result": results}, 201

    def delete(self):
        result = delete_db()
        return {'result': result}, 200


@api.route('/generate-comment')
class Generate_Comment(Resource):
    @api.expect(generate_comment_get_requests, validate=True)
    def get(self):
        args = generate_comment_get_requests.parse_args()
        result = generate_comment(args['content'])
        return {'result': result}


if __name__ == "__main__":
    load_dotenv()
    app.run(port=8888)
