"""
models.py
defines database models
---
https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
"""

from datetime import datetime

from api import db


class Article(db.Model):
    """
    Model for articles/blog posts
    """

    __tablename_ = "articles"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(280))
    content = db.Column(db.String())
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return "<Article {}>".format(self.title)
