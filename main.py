from board_setup.board import Board
from board_setup.board_saved_interaction import saved_board_manipulation
from board_setup.random_generation import random_gen
from summary.post_game_summary import post_game_summary
import time


def main():
    """ This function essentially exist in order to
        combine the effects of other functions.
    """
    print("Welcome to Minesweeper.\nWould you like to generate a new\
map,or use a saved one?")
    option = input(
        'Type in 1 to generate a new map,\
type in 2 to access pregenerated maps.\t')
    while option not in ('1', '2'):
        option = input('Incorrect selection. Type in \
            1 for a new map or 2 for pregenerated maps.\t')
    if option == '1':
        board_data = random_gen()
    if option == '2':
        board_data = saved_board_manipulation()
    if not board_data: exit("map deleted. Exiting")
    board = Board(board_data)
    board_for_3BV = Board(board_data)
    starting_time = time.time()
    game_end = False
    print(board)
    while game_end is False:
        board.field_interact()
        board.check_win_condition()
        if board.win_condition() is True:
            game_end = True
        if board.mine_activated() is True:
            game_end = True
    end_time = time.time()
    post_game_summary(board, board_for_3BV, starting_time, end_time)


if __name__ == "__main__":
    main()
