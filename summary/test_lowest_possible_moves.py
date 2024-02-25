from lowest_possible_moves import lowest_possible_moves
from board_setup.board import Board


def test_lowest_possible_moves():
    test_board = [[0, 1, 0, 0, 0],
                  [1, 0, 1, 0, 0],
                  [0, 0, 1, 1, 1]]
    board = Board(test_board)
    lowest_moves = lowest_possible_moves(board)
    assert lowest_moves == 6

    