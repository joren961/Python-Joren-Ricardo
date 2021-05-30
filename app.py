import development as development
from flask import Flask, request
from flask import render_template

from models.Game import Game
from models.Player import Player

app = Flask(__name__, template_folder='templates')
FLASK_APP = __name__
FLASK_ENV = development


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/game', methods=['GET'])
def game():
    nickname = request.form.get("nickname")
    double_colors = request.form.get("double-colors")
    color_amount = request.form.get("color-amount")
    position_amount = request.form.get("position-amount")
    cheat = request.form.get('cheat')
    game_model = Game(Player(nickname), double_colors, color_amount, position_amount, cheat)
    return render_template('game.html',
                           nickname=nickname,
                           game=game_model)


@app.route('/leaderboard')
def statistics():
    return render_template('leaderboard.html')
