from flask import render_template, request, redirect, url_for, abort, jsonify
from app import app, db
from app.models import Game


@app.route('/game/<int:id>/join/<side>', methods=['GET'])
def game(id, side):
    """
    Renders game from stored state
    """
    #Getting game by primary key:
    game = Game.query.get(id)
    # unserialize the game board so jinja can loop through it
    # if there is no game with this id then return a 404
    if game:
        game.unserialize()
    else:
        abort(404)

    # lower case the side input and ensure it is 'x' or 'o'
    side = side.lower()
    if side not in ['x', 'o']:
        abort(404)

    return render_template('game.html', game=game, side=side)


@app.route('/update', methods=['POST'])
def update():
    """
    Handles Ajax POST from jquery onClick
    """
    if request.method == 'POST':
        # get data from request object
        id = request.form['id']
        turn = request.form['turn']
        x, y = int(request.form['loc'][0]), int(request.form['loc'][1])
        game = Game.query.get(id)

        if game:
            game.unserialize()
        else:
            abort(404)
        game.make_move([x, y], turn)
        game.check_full()
        game.check_win()
        game.serialize()
        db.session.add(game)
        db.session.commit()

    return jsonify(**game.to_json())


@app.route('/new/<side>', methods=['GET'])
def new(side):
    """
    Creates a new game and redirects to it
    """
    game = Game()
    db.session.add(game)
    db.session.commit()
    return redirect(url_for('game', id=game.id, side=side))


@app.route('/', methods=['GET'])
def index():
    """
    Renders all games on front page...should be paginated normally.
    """
    games = Game.query.all()
    for game in games:
        game.unserialize()
    return render_template('index.html', games=games)