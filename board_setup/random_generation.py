from random import randint
from board_setup.board_io import board_save

def random_gen():
    """This function generates a random board with a size and mine count
        of the player's choosing.
    """
    rows = input('How many rows should the board have?(At least 2)\t')
    while not rows.isdigit() or int(rows) < 2:
        input('Incorrect input. Please type in an integer larger than 1.')
    rows = int(rows)
    columns = input('How many columns should the board have?(At least 2)\t')
    while not columns.isdigit() or int(columns) < 2:
        input('Incorrect input. Please type in an integer larger than 1.')
    columns = int(columns)
    max_mines = rows * columns
    mine_count = input(f'How many mines should the board have?(more than 0,\
less than {max_mines})\t')
    correct_mine_count = False
    while not correct_mine_count:
        if mine_count.isdigit():
            mine_count = int(mine_count)
            if 0 < int(mine_count) < max_mines:
                correct_mine_count = True
            else:
                mine_count = input(
                    f'Incorrect input. It must be 0 < count < {max_mines}')
        else:
            mine_count = input('Incorrect input. Please type in an integer.')
    board = []
    for row in range(0, rows):
        templist = []
        for column in range(0, columns):
            templist.append(0)
        board.append(templist)
    counter = 0
    while counter < mine_count:
        row = randint(0, rows-1)
        column = randint(0, columns-1)
        if board[row][column] != 1:
            board[row][column] = 1
            counter += 1
    choice = input('Do you want to 1)Just play or 2)Save this board first?')
    while choice not in ('1', '2'):
        choice = input('Type in 1 to play or 2 to save this map first.')
    if choice == '1':
        return board
    if choice == '2':
        save_name = input('Please name the board.')
        board_save(board, save_name)
        return board
