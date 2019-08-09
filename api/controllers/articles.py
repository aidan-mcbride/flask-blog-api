from flask import Blueprint, jsonify

articles = Blueprint("articles", __name__, url_prefix="/articles")

# MOCK DATA
# TODO: persist in database
mock_articles = [
    {"title": "Blog Post 1", "content": "Post body"},
    {"title": "Blog Post 2", "content": "Post body"},
    {"title": "Blog Post 3", "content": "Post body"},
]


@articles.route("/")
def get_all_articles():
    return jsonify(mock_articles)
