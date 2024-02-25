def lowest_possible_moves(board):
    """This function calculates 3BV using this algorithm:
    1) when there are fields without neighbouring mines:
    reveal fields separated from mines
    2)when there are only fields with neighbouring mines:
    reval fields near mines
    """
    counter = 0
    for id_row, row in enumerate(board.board()):
        for id_column, column in enumerate(row):
            if column.mines_near() == 0:
                if column.has_mine() is False:
                    if column.is_activated() is False:
                        counter += 1
                        column.activation(board)
                        board.revealing_nearby_empty([[id_row, id_column]])
    for row in board.board():
        for column in row:
            if column.has_mine() is False:
                if column.is_activated() is False:
                    counter += 1
    return counter
