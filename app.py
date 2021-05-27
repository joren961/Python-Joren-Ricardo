import flask
from flask import Flask

app = Flask(__name__)
FLASK_APP = __name__


@app.route('/')
def home():
    return flask.render_template('homepage.html')


@app.route('/game/<nickname>')
def game(nickname):
    return 'This is where the game is played'


@app.route('/leaderboard')
def statistics():
    return flask.render_template('leaderboard.html')
