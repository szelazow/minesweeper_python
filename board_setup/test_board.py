from board import Board
from io import StringIO

testing_board = [[0, 0, 0, 1, 1, 0],
                 [0, 1, 1, 1, 0, 0],
                 [0, 1, 0, 0, 0, 0]]


def test_board_create():
    board = Board(testing_board)
    assert len(board.board()) == 3
    assert len(board.board()[0]) == 6
    assert board.mines() == 6


def test_board_nearby_fields():
    board = Board(testing_board)
    assert [0, 1] in board.get_nearby_fields(0, 0)
    assert [1, 0] in board.get_nearby_fields(0, 0)
    assert [1, 1] in board.get_nearby_fields(0, 0)
    assert len(board.get_nearby_fields(0, 0)) == 3


def test_board_field_interact(monkeypatch):
    board = Board(testing_board)
    inputs = StringIO('1\n0\n1')
    monkeypatch.setattr('sys.stdin', inputs)
    monkeypatch.setattr('sys.stdin', inputs)
    board.field_interact()
    assert board.board()[1][0].is_activated() is True
