from models.models import comment


def get_comments():
    all_comments = comment.query.all()  # 全コメントデータを取得
    comments_list = [
        {
            'task_id': c.task_id,
            'content': c.content,
            'created_at': c.created_at.isoformat()
        } for c in all_comments
    ]  # 必要な情報をリストに格納
    return comments_list
