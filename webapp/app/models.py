from app import db
import json

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    board = db.Column(db.Text)
    turn = db.Column(db.String(128))

    def __init__(self):
        self.turn = "x"
        self.board = json.dumps([[None, None, None], [None, None, None], [None, None, None]])