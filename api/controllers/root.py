from flask import Blueprint

# declare blueprint to be registered in application factory
root = Blueprint('root', __name__)

@root.route('/')
def test_route():
    return {'message': 'Endpoint Exists!'}
