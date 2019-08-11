from flask import Blueprint, jsonify, request

from api import db
from api.models import Article  # type: ignore

# typing imports
from typing import Tuple
from flask import Response

articles = Blueprint("articles", __name__, url_prefix="/articles")


@articles.route("/", methods=["GET"])
def get_all_articles() -> Tuple[Response, int]:
    """
    GET /articles/
    Query database for all articles,
    return all data as json
    """
    response_data = list()
    articles = Article.query.all()
    for article in articles:
        article_data = dict()
        article_data["id"] = article.id
        article_data["slug"] = article.slug
        article_data["title"] = article.title
        article_data["content"] = article.content
        response_data.append(article_data)
    return jsonify(response_data), 200


@articles.route("/<string:slug>", methods=["GET"])
def get_article_by_slug(slug: str):
    """
    GET: /articles/<slug>
    Query database for first article with matching slug,
    return json object containing article data
    """
    response_data = dict()
    article = Article.query.filter_by(slug=slug).first()
    if article:
        response_data["id"] = article.id
        response_data["title"] = article.title
        response_data["slug"] = article.slug
        response_data["content"] = article.content

        return jsonify(response_data), 200
    else:
        return jsonify({"error": "article not found"}), 404
