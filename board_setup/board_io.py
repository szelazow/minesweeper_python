from os import listdir


def board_save(board, name):
    ''' This function allows the player to save a board as a .txt file.'''
    with open(f'board_setup/saved_games/{name}.txt', 'w') as file_handle:
        for row in board:
            tempstr = ''
            for column in row:
                tempstr += (f'{row[column]},')
            line = f'{tempstr[:-1]}\n'
            file_handle.write(line)

def board_load(name):
    ''' This function allows the player to load a board from a .txt file.'''
    board = []
    with open(f'board_setup/saved_games/{name}.txt', 'r') as file_handle:
        for line in file_handle:
            templist = []
            line = line.rstrip()
            for field in line.split(','):
                templist.append(int(field))
            board.append(templist)
    return board


def saved_games_list():
    '''This function lists savefiles for the player.'''
    saved_files = listdir('board_setup/saved_games')
    processed_names = []
    for file_name in saved_files:
        file_name = file_name[:-4]
        processed_names.append(file_name)
    return processed_names
