from datetime import datetime

from db import db
from models.models import comment


def save_comment(content: str):
    task_id = content.split(' ', 1)[0]  # contentの頭からスペースまでをtask_idとして抽出
    formatted_comment = comment(
        task_id=task_id, content=content.strip(), created_at=datetime.utcnow())
    db.session.add(formatted_comment)
    db.session.commit()
    return True  # 保存が成功した場合はTrueを返す
