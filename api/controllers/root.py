from flask import Blueprint, jsonify

root = Blueprint("root", __name__)


@root.route("/", methods=["GET"])
def api_directory():
    return jsonify(dict(endpoints=["/articles/", "/articles/<slug>"])), 200
