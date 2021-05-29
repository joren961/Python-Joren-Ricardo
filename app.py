import development as development
from flask import Flask, request
from flask import render_template

app = Flask(__name__, template_folder='templates')
FLASK_APP = __name__
FLASK_ENV = development


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/game', methods=['GET'])
def game():
    nickname = request.form.get("nickname")
    doubleColors = request.form.get("double-colors")
    colorAmount = request.form.get("color-amount")
    positionAmount = request.form.get("position-amount")
    return render_template('game.html',
                           nickname=nickname,
                           doubleColors=doubleColors,
                           colorAmount=colorAmount,
                           positionAmount=positionAmount)


@app.route('/leaderboard')
def statistics():
    return render_template('leaderboard.html')


if __name__ == '__main__':
    app.run(debug=True)
