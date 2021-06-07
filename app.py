#import development as development
import sqlite3 as sql
from sqlite3 import Error
from flask import Flask, request
from flask import render_template

from controllers.GameController import GameController

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
#FLASK_ENV = development
create_connection(r"C:\sqlite\db\mastermind.db")


@app.route('/')
def home():
    return render_template('homepage.html')

game_controller = GameController()

@app.route('/game', methods=['GET', 'POST'])
def game():

    if request.form.get("turn") == None:

        nickname = request.form.get("nickname")
        double_colors = request.form.get("double-colors")
        number_amount = request.form.get("color-amount", type=int)
        position_amount = request.form.get("position-amount", type=int)
        cheat = request.form.get('cheat')
    
        game_controller.create_game(nickname, double_colors, number_amount, position_amount, cheat)

    elif request.form.get("numberInput1") is not None:
        input_list = []
        for i in range(game_controller.get_game().get_position_amount()):
            input_list.append(request.form.get("numberInput" + str(i+1)))
        
        game_controller.next_turn(game_controller.get_game().get_turn(), input_list) 

    return render_template('game.html',
        nickname=game_controller.get_game().get_player().get_nickname(),
        position_amount=game_controller.get_game().get_position_amount(),
        number_amount=game_controller.get_game().get_number_amount(),
        cheat = game_controller.get_game().get_cheat(),
        block_row_list = list(game_controller.get_game().get_block_row_list()),
        computer_code = game_controller.get_game().get_computer_code().get_string_code(game_controller.get_game().get_computer_code()))

@app.route('/leaderboard')
def statistics():
    return render_template('leaderboard.html')
