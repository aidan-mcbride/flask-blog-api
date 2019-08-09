from flask import Blueprint

articles = Blueprint('articles', __name__, url_prefix='/articles')

@articles.route('/')
def get_all_articles():
    return '', 200
