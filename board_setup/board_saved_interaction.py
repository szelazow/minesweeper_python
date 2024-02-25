from board_setup.board_io import saved_games_list, board_load
import os


def saved_board_manipulation():
    print('Please select the save you want to use or delete\
            from the list below(type in the identificator):')
    saved_games = saved_games_list()
    for i in range(0, len(saved_games)):
        print(f'{i}: {saved_games[i]}')
    selected_map = saved_games[int(input())]
    while selected_map not in saved_games:
        input('This is not a valid map identificator. Check the list again,\
             and try once more.')
    option = input("Select operation:\n1 - load board\n2 - delete board\n")
    while option not in ['1', '2']:
        option = input('This is not a valid option. Please type in 1 or 2.')
    if option == '1':
        board = board_load(selected_map)
        return board
    if option == '2':
        os.remove(f'board_setup/saved_games/{selected_map}.txt')
