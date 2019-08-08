"""
import Flask class from flask
create instance of Flask class as 'app'
add single route to return string
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World'
