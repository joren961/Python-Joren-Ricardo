import development as development
import sqlite3 as sql
from sqlite3 import Error
from flask import Flask, request
from flask import render_template

from models.Game import Game
from models.Player import Player


def create_connection(db_file):
    conn = None
    try:
        conn = sql.connect(db_file)
        conn.execute(create_database())
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_database():
    return """ CREATE TABLE IF NOT EXISTS stats (
                                        nickname text PRIMARY KEY,
                                        cheat integer NOT NULL,
                                        play_date text NOT NULL,
                                        guesses integer NOT NULL
                                    ); """


app = Flask(__name__, template_folder='templates')
FLASK_APP = __name__
FLASK_ENV = development
create_connection(r"C:\sqlite\db\mastermind.db")


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/game', methods=['GET', 'POST'])
def game():
    nickname = request.form.get("nickname")
    double_colors = request.form.get("double-colors")
    color_amount = request.form.get("color-amount", type=int)
    position_amount = request.form.get("position-amount", type=int)
    cheat = request.form.get('cheat')
    game_model = Game(Player(nickname), double_colors, color_amount, position_amount, cheat)
    return render_template('game.html',
                           nickname=nickname,
                           position_amount=position_amount,
                           color_amount=color_amount)


@app.route('/leaderboard')
def statistics():
    return render_template('leaderboard.html')
