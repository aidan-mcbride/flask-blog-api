# type: ignore

"""
models.py
defines database models
---
https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
"""

from datetime import datetime
from slugify import slugify

from marshmallow import fields, post_load, validates, ValidationError

from api import db, ma


class Article(db.Model):
    """
    Model for articles/blog posts
    """

    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(280), nullable=False)
    slug = db.Column(db.String(280))
    content = db.Column(db.String(), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, **kwargs):
        """
        Class Constructor
        Flask-SQLAlchemy's base model class has a constructor that simply stores all given keyword arguments as-is.
        If using a custom constructor, you can keep the base constructor by using super()
        and then add any custom initialization after:
        ---
        see:
        https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application
        (towards bottom of first section)
        https://stackoverflow.com/questions/20460339/flask-sqlalchemy-constructor
        """
        super(Article, self).__init__(**kwargs)
        # custom initialization
        self.slug = slugify(self.title)


class ArticleSchema(ma.ModelSchema):
    class Meta:
        model = Article

    # can't validate slug since it hasn't been initialized yet.
    @validates("title")
    def validate_unique_title(self, value):
        slugified_title = slugify(value)
        if Article.query.filter_by(slug=slugified_title).first():
            raise ValidationError("title must be unique")

    """
    example of how to create slugs when doing schema.load()
    """
    # @post_load
    # def create_slug(self, data):
    #     data['slug'] = slugify(data['title'])
    #     return data


"""
Initialize schemas to export
"""
article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)
