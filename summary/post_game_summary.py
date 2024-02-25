from summary.lowest_possible_moves import lowest_possible_moves


def post_game_summary(board, board_3BV, starting_time, end_time):
    """ This function is responsible for presenting
        the user with some basic information
        on post game conditons - it shows his time, the board's 3BV,
        and tells him whetever he successfully cleared the board,
        or encountered a mine.
    """
    total_time = end_time - starting_time
    best_possible = lowest_possible_moves(board_3BV)
    if board.mine_activated() is False:
        print('You won!')
    else:
        print('You lost! Better luck next time.')
    print(f'Time elapsed: {total_time}s')
    print(f"Board's 3BV: {best_possible}")
