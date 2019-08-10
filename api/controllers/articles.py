from flask import Blueprint, jsonify, request

from api import db
from api.models import Article

articles = Blueprint("articles", __name__, url_prefix="/articles")


@articles.route("/", methods=["GET"])
def get_all_articles():
    """
    GET /articles/
    Query database for all articles,
    return all data as json
    """
    response_data = []
    articles = Article.query.all()
    for article in articles:
        article_data = {}
        article_data["id"] = article.id
        article_data["title"] = article.title
        article_data["content"] = article.content
        response_data.append(article_data)
    return jsonify(response_data), 200
