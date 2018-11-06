from app.model.database import *


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text)
    done = db.Column(db.Boolean)

    def __init__(self, title=None, content=None):
        self.title = title
        self.content = content
        self.done = False
