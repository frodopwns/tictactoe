from flask import render_template, request,flash, redirect, url_for, abort
from app import app, db
from app.models import Game


@app.route('/game/<int:id>/join/<side>', methods=['POST', 'GET'])
def game(id, side):
    #Getting game by primary key:
    game = Game.query.get(id)

    if game:
        game.unserialize()
    else:
        abort(404)

    side = side.lower()
    if side not in ['x', 'o']:
        abort(404)

    if request.method == 'POST':
        print request.form
        choice = map(int, request.form['coords'].split(","))
        side = request.form['side']
        if game.turn == side:

            game.make_move(choice, side)
            if game.check_win():
                flash("winner!")
            elif game.check_full():
                flash("game over with tie!")

            game.serialize()
            db.session.add(game)
            db.session.commit()
            game.unserialize()
            flash("game updated")
            return redirect(url_for("game", id=game.id, side=side))


    return render_template('game.html', game=game, side=side)


@app.route('/new/<side>')
def new(side):
    game = Game()
    db.session.add(game)
    db.session.commit()
    return redirect(url_for('game', id=game.id, side=side))


@app.route('/' )
def index():
    games = Game.query.all()
    for game in games:
        game.unserialize()
    return render_template('index.html', games=games)