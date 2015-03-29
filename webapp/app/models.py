from app import db
import json

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    board = db.Column(db.Text)
    turn = db.Column(db.String(128))
    winner = db.Column(db.String(128))
    full = db.Column(db.Boolean)
    _serial = db.Column(db.Boolean)
    _moves = db.Column(db.Integer)

    def __init__(self):
        self.turn = "x"
        self.winner = None
        self.full = False
        self._serial = True
        self._moves = 0
        self.board = json.dumps([[None, None, None],
                                 [None, None, None],
                                 [None, None, None]])

    def serialize(self):
        if not self._serial:
            self.board = json.dumps(self.board)
            self._serial = True

    def unserialize(self):
        if self._serial:
            self.board = json.loads(self.board)
            self._serial = False

    def to_json(self):
        return {
            'id': self.id,
            'board': self.board,
            'turn': self.turn,
            'winner': self.winner,
            'full': self.full,
        }

    def make_move(self, coords, side):
        self.unserialize()
        self.board[coords[0]][coords[1]] = side
        self.turn = "x" if side == "o" else "o"
        self._moves += 1

    def check_full(self):
        if self._moves == 9:
            self.full = True

        return self.full

    def check_win(self):
        self.unserialize()
        # rows
        if self.board[0][0] == self.board[0][1] == self.board[0][2]:
            self.winner = self.board[0][0]
        if self.board[1][0] == self.board[1][1] == self.board[1][2]:
            self.winner = self.board[1][0]
        if self.board[2][0] == self.board[2][1] == self.board[2][2]:
            self.winner = self.board[2][0]
        # cols
        if self.board[0][0] == self.board[1][0] == self.board[2][0]:
            self.winner = self.board[0][0]
        if self.board[0][1] == self.board[1][1] == self.board[2][1]:
            self.winner = self.board[0][1]
        if self.board[0][2] == self.board[1][2] == self.board[2][2]:
            self.winner = self.board[0][2]
        # diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            self.winner = self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            self.winner = self.board[0][2]

        if self.winner:
            return True

        return False
