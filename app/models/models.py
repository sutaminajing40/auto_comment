from datetime import datetime

from db import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.String(10), nullable=False)  # 課題番号を指定するカラム
    content = db.Column(db.String(1000), nullable=False)  # コメント本文のカラム
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # コメント作成時間

    def __repr__(self):
        return f"<Comment {self.content}>"
