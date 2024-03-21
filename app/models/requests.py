from flask_restx import reqparse

# commentsのPOSTリクエストの型を定義
comments_post_requests = reqparse.RequestParser()
comments_post_requests.add_argument(
    'content', type=str, required=True, help='Content cannot be blank')
