from flask import Blueprint, jsonify, request

from api import db
from api.models import Article  # type: ignore


articles = Blueprint("articles", __name__, url_prefix="/articles")


@articles.route("/", methods=["GET", "POST"])
def all_articles():
    if request.method == "GET":
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

    if request.method == "POST":
        """
        POST to /articles/
        Create new article from request json
        return newly-created article as response with 201 status code.
        """

        # validate request
        # TODO:
        # - abstract into function
        # - class method?
        if not request.json:
            return jsonify({"error": "request body is missing or is invalid json"}), 400
        if "title" not in request.json:
            return jsonify({"error": "title is required"}), 400
        if "content" not in request.json:
            return jsonify({"error": "article body is required"}), 400

        # TODO:
        # - create mapper?
        # - abstract to function that accepts request json
        #   and returns new Article instance?
        #   put this function in Article class as method?
        title: str = request.json["title"]
        content: str = request.json["content"]

        new_article: Article = Article(title=title, content=content)
        db.session.add(new_article)
        db.session.commit()

        # retrieve newly-created article
        # TODO:
        # - abstract method to create response data from model?
        # - put this in Article class? As __repr__ ?
        slug: str = new_article.slug
        new_article: Article = Article.query.filter_by(slug=slug).first()
        response_data: dict = dict(
            id=new_article.id,
            title=new_article.title,
            slug=new_article.slug,
            content=new_article.content,
            date_created=new_article.date_created,
        )

        return jsonify(response_data), 201


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
