from flask import Blueprint, jsonify, request

from api import db
from api.models import Article, article_schema, articles_schema  # type: ignore

articles = Blueprint("articles", __name__, url_prefix="/articles")


@articles.route("/", methods=["GET", "POST"])
def all_articles():
    if request.method == "GET":
        articles = Article.query.all()
        return articles_schema.jsonify(articles)

    if request.method == "POST":
        if not request.json:
            return jsonify({"error": "request body is missing or is invalid json"}), 400

        article, errors = article_schema.load(request.json)
        if errors:
            return jsonify(errors), 400

        db.session.add(article)
        db.session.commit()

        new_article = Article.query.filter_by(slug=article.slug).first()
        return article_schema.jsonify(new_article), 201


@articles.route("/<string:slug>", methods=["GET"])
def get_article_by_slug(slug: str):
    article = Article.query.filter_by(slug=slug).first()
    if not article:
        return dict(error="article not found"), 404
    return article_schema.jsonify(article)
