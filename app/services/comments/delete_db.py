from db import db
from models.models import comment


def delete_db():
    comment.query.delete()
    db.session.commit()
    return True
