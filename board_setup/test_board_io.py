from board_io import board_save, board_load, saved_games_list


def test_board_IO():
    test_board = [[1, 1, 1, 1],
                  [0, 0, 0, 0],
                  [0, 1, 1, 0]]
    board_save(test_board, 'test_board')
    saved_games = saved_games_list()
    assert 'test_board' in saved_games
    load_test = board_load('test_board')
    assert load_test == test_board
    