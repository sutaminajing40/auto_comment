from api import api
from flask_restx import fields, reqparse

# リクエストデータの解析用パーサーを設定
parser = reqparse.RequestParser()
parser.add_argument(
    'task_id', type=str, required=True, help='Task ID cannot be blank')
parser.add_argument(
    'content', type=str, required=True, help='Content cannot be blank')


# レスポンスデータのフィールドを設定
model = api.model('CommentModel', {
    'id': fields.Integer,
    'task_id': fields.String,
    'content': fields.String,
    'created_at': fields.DateTime
})
