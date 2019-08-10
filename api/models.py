# type: ignore

"""
models.py
defines database models
---
https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
"""

from datetime import datetime
from slugify import slugify

from api import db


class Article(db.Model):
    """
    Model for articles/blog posts
    """

    __tablename_ = "articles"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(280))
    slug = db.Column(db.String(280), nullable=False)
    content = db.Column(db.String())
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, title=None, slug=None, content=None, date_created=None):
        self.title = title
        self.slug = slugify(title)
        self.content = content
        self.date_created = date_created

    def __repr__(self):
        return "<Article {}>".format(self.title)
