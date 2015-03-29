from app.models import Game

wins = [
    [[0, 0, 'x'], [1, 0, 'o'], [0, 1, 'x'], [2, 0, 'o'], [0, 2, 'x']],
    [[1, 0, 'x'], [2, 0, 'o'], [1, 1, 'x'], [2, 0, 'o'], [1, 2, 'x']],
    [[2, 0, 'x'], [1, 0, 'o'], [2, 1, 'x'], [1, 1, 'o'], [2, 2, 'x']],
    [[0, 0, 'x'], [2, 1, 'o'], [1, 0, 'x'], [2, 2, 'o'], [2, 0, 'x']],
    [[0, 1, 'x'], [2, 0, 'o'], [1, 1, 'x'], [2, 2, 'o'], [2, 1, 'x']],
    [[0, 2, 'x'], [2, 0, 'o'], [1, 2, 'x'], [2, 1, 'o'], [2, 2, 'x']],
    [[0, 0, 'x'], [0, 1, 'o'], [1, 1, 'x'], [2, 1, 'o'], [2, 2, 'x']],
    [[0, 2, 'x'], [0, 1, 'o'], [1, 1, 'x'], [2, 1, 'o'], [2, 0, 'x']],
]

ties = [
    [[0, 0, 'x'], [0, 1, 'o'], [0, 2, 'x'],
     [1, 0, 'o'], [1, 1, 'o'], [1, 2, 'x'],
     [2, 0, 'x'], [2, 1, 'x'], [2, 2, 'o']],
]


def test_wins():
    for scenario in wins:
        g = Game()
        for move in scenario:
            g.make_move([move[0],move[1]], move[2])

        assert g.check_win()


def test_ties():
    for scenario in ties:
        g = Game()
        for move in scenario:
            g.make_move([move[0],move[1]], move[2])

        assert g.check_full()