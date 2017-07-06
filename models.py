from app import db
from datetime import datetime

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(70))
    body = db.Column(db.String(500))
    pubdate = db.Column(db.DateTime)

    def __init__(self, title, body, pubdate = None):
        self.title = title
        self.body = body
        if pubdate is None:
            pubdate = datetime.now()
        self.pubdate = pubdate
