import development as development
from flask import Flask
from flask import render_template

app = Flask(__name__)
FLASK_APP = __name__
FLASK_ENV = development


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/game/<nickname>')
def game(nickname):
    return 'This is where the game is played'


@app.route('/leaderboard')
def statistics():
    return render_template('leaderboard.html')
