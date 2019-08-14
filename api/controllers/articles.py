from flask import Blueprint, jsonify, request

from api import db
from api.models import Article, article_schema, articles_schema  # type: ignore

articles = Blueprint("articles", __name__, url_prefix="/articles")


def parse_errors(errors: dict) -> dict:
    """
    Takes validation errors returned by marshmallow
    and reformats them as API error messages
    """
    error_list = list()
    if isinstance(errors, dict):
        for key in errors.keys():
            message: str = errors[key][0][:-1].lower()
            error_list.append("{}: {}".format(key, message))
    return dict(errors=error_list)


@articles.route("/", methods=["GET", "POST"])
def all_articles():
    if request.method == "GET":
        articles = Article.query.all()
        return articles_schema.jsonify(articles)

    if request.method == "POST":
        if not request.json:
            return (
                jsonify(dict(errors=["request body is missing or is invalid json"])),
                400,
            )

        article, errors = article_schema.load(request.json)
        if errors:
            return jsonify(parse_errors(errors)), 400

        db.session.add(article)
        db.session.commit()

        new_article = Article.query.filter_by(slug=article.slug).first()
        return article_schema.jsonify(new_article), 201


@articles.route("/<string:slug>", methods=["GET", "PUT", "DELETE"])
def article_by_slug(slug: str):
    if request.method == "GET":
        article = Article.query.filter_by(slug=slug).first()
        if not article:
            return dict(errors=["article not found"]), 404
        return article_schema.jsonify(article)

    if request.method == "PUT":
        article = Article.query.filter_by(slug=slug).first()
        if not article:
            return dict(errors=["article not found"]), 404
        if not request.json:
            return (
                jsonify(dict(errors=["request body is missing or is invalid json"])),
                400,
            )

        """
        update article instance:
        ---
        https://marshmallow-sqlalchemy.readthedocs.io/en/latest/api_reference.html#marshmallow_sqlalchemy.ModelSchema.load
        """
        article, errors = article_schema.load(request.json, instance=article)
        if errors:
            return jsonify(parse_errors(errors)), 400

        db.session.commit()

        return article_schema.jsonify(article), 200

    if request.method == "DELETE":
        article = Article.query.filter_by(slug=slug).first()
        if not article:
            return dict(errors=["article not found"]), 404
        db.session.delete(article)
        db.session.commit()
        return "", 204
