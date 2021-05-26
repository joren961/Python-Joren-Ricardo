from flask import Flask

app = Flask(__name__)
FLASK_APP = __name__


@app.route('/')
def hello():
    return 'Hello, World!'
