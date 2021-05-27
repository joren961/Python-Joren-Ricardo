from flask import Flask

app = Flask(__name__)
FLASK_APP = __name__


@app.route('/')
def hello():
    return 'This is where the preferences are set'


@app.route('/game/<nickname>')
def game(nickname):
    return 'This is where the game is played'


@app.route('/')
def statistics():
    return 'This is where the statistics are displayed'
