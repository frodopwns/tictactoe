from flask import render_template, request,flash, redirect, url_for, abort
import json
from app import app, db
from app.models import Game


def unserialize_board(b):
    b.board = json.loads(b.board)
    return b

def serialize_board(b):
    b.board = json.dumps(b.board)
    return b


@app.route('/game/<int:id>/join/<side>', methods=['POST', 'GET'])
def game(id, side):
    #Getting game by primary key:
    game = Game.query.get(id)

    if game:
        game = unserialize_board(game)
    else:
        abort(404)

    if request.method == 'POST':
        print request.form
        choice = map(int, request.form['coords'].split(","))
        side = request.form['side']
        if game.turn == side:
            game.board[choice[0]][choice[1]] = side
            game.board = json.dumps(game.board)
            game.turn = "x" if side == "o" else "o"
            db.session.add(game)
            db.session.commit()
            game.board = json.loads(game.board)
            flash("game updated")


    side = side.lower()
    if side not in ['x', 'o']:
        abort(404)



    return render_template('game.html', game=game, side=side)


@app.route('/' )
def index():
    games = map(unserialize_board, Game.query.all())
    return render_template('index.html', games=games)