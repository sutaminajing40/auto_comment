from datetime import datetime

from db import db
from models.models import comment


def save_comment(content: str):
    # contentを最初のスペースで分割し、task_idと実際のコメント内容を分ける
    task_id, _, actual_content = content.partition(' ')
    created_at = datetime.utcnow()
    formatted_comment = comment(
        task_id=task_id, content=actual_content.strip(), created_at=created_at)
    db.session.add(formatted_comment)
    db.session.commit()
    return {'task_id': task_id,
            'content': actual_content.strip(),
            'created_at': created_at.isoformat()
            }
