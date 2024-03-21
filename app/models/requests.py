from flask_restx import reqparse

# commentsのPOSTリクエストの型を定義
comments_post_requests = reqparse.RequestParser()
comments_post_requests.add_argument(
    'content', type=str, required=True, help='Content cannot be blank')


# generate_commentのGETリクエストの型を定義
generate_comment_get_requests = reqparse.RequestParser()
generate_comment_get_requests.add_argument(
    'content', type=str, required=True, help='Content cannot be blank')
