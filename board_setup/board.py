from board_setup.field import Field


class Board:
    """ This class represents a minesweeper board.
        Its' most notable methods are:
        field_interact - allows the player to choose and reveal/mark a field
        revealing_nearby_empty - a recursive function responsible for revealing
        adjacent fields without mines on field activation(only fields without
        an adjacent mine cause this, and it can cascade).
        get_nearby_fields - used to grab fields surrounding a selected one,
        used for the cascade revealing effect and counting surrounding mines.
        check_win_condition - responsible for checking if all fields without
         mines were revealed.
    """
    def __init__(self, board_data):
        self._board_data = board_data
        self._rows = len(board_data)
        self._columns = len(board_data[0])
        self._total_fields = len(board_data) * len(board_data[0])
        self._row = -1
        self._column = -1
        self._win_condition = False
        self._nearby_fields = []
        self._mine_activated = False
        board = []
        for row in range(0, len(board_data)):
            templist = []
            for column in range(0, len(board_data[0])):
                mines_near = 0
                neighbors = self.get_nearby_fields(row, column)
                for new_row, new_column in neighbors:
                    if board_data[new_row][new_column] == 1:
                        mines_near += 1
                if board_data[row][column] == 1:
                    templist.append(Field(True, board_data, mines_near))
                else:
                    templist.append(Field(False, board_data, mines_near))
            board.append(templist)
        self._board = board
        mines = 0
        for row in board_data:
            for column in row:
                if column == 1:
                    mines += 1
        self._mines = mines

    def row(self):
        return self._row

    def column(self):
        return self._column

    def mines(self):
        return self._mines

    def mine_activated(self):
        return self._mine_activated

    def board(self):
        return self._board

    def field_interact(self):
        print("Select the row of the field you will interact with.\n")
        correct_row = False
        while correct_row is False:
            self._row = input()
            if self._row.isdigit() is True:
                self._row = int(self._row)
                if 0 <= self._row < self._rows:
                    correct_row = True
                else:
                    print(f"You need to pick a number between 0\
and {self._rows - 1}")
            else:
                print("You need to type in an integer.")
        print("Now select the column.")
        correct_column = False
        while correct_column is False:
            self._column = input()
            if self._column.isdigit() is True:
                self._column = int(self._column)
                if 0 <= self._column < self._columns:
                    correct_column = True
                else:
                    print(f"You need to pick a number between 0\
and {self._columns - 1}")
            else:
                print("You need to type in an integer.")
        option = input('1 - activate, 2 - flag\t')
        if option == '1':
            if self._board[self._row][self._column].has_mine() is True:
                self._mine_activated = True
            self._board[self._row][self._column].activation(self)
            self.revealing_nearby_empty([[self._row, self._column]])
        if option == '2':
            self._board[self._row][self._column].change_flag_status()

    def revealing_nearby_empty(self, current_move):
        next_move = []
        for (row, column) in current_move:
            self._board[row][column].activation(self)
            surrounding = []
            if self._board[row][column].mines_near() == 0:
                surrounding = self.get_nearby_fields(row, column)
            for new_row, new_column in surrounding:
                if self._board[new_row][new_column].is_activated() is False:
                    if self._board[new_row][new_column].has_mine() is False:
                        next_move.append([new_row, new_column])
        current_move = next_move
        if current_move != []:
            self.revealing_nearby_empty(current_move)

    def get_nearby_fields(self, row, column):
        nearby_fields_coordinates = []
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                if x != 0 or y != 0:
                    if 0 <= (row + y) < self._rows:
                        if 0 <= (column + x) < self._columns:
                            nearby_fields_coordinates.append([row+y, column+x])
        return nearby_fields_coordinates

    def check_win_condition(self):
        counter = 0
        for row in self._board:
            for column in row:
                if column.is_activated() is False:
                    counter += 1
        if counter == self._mines:
            self._win_condition = True

    def win_condition(self):
        return self._win_condition

    def __str__(self):
        board_representation = '#'
        for column in range(0, self._columns):
            board_representation += f'  {column}'
        board_representation += '\n\n'
        for row_number in range(0, self._rows):
            board_representation += str(row_number)
            for element in self._board[row_number]:
                board_representation += f'  {element}'
            board_representation += '\n'
        return board_representation
