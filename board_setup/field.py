class Field:
    """ This class represents a single field.
        It essentially only exits within a board,
        it holds information on the amount of mines around a field,
        whether it is a mine,
        and is responsible for the graphic
        representation of fields.
    """
    def __init__(self, has_mine, board_data, mines_near):
        self._is_activated = False
        self._nearby_bombs = mines_near
        self._has_mine = has_mine
        self._has_flag = False
        self._mines_near = mines_near

    def activation(self, board):             # handles activating a field
        if self._has_mine is True:
            self._is_activated = True
            self._has_flag = False
            board.mine_activated()
        else:
            self._is_activated = True
            self._has_flag = False

    def has_mine(self):
        return self._has_mine

    def mines_near(self):
        return self._mines_near

    def is_activated(self):
        return self._is_activated

    def change_flag_status(self):
        self._has_flag = not self._has_flag

    def __str__(self):                      # represents a field graphically
        if self._has_flag is True:
            return 'P'
        elif self._is_activated == 0:
            return '*'
        elif self._is_activated == 1:
            if self._has_mine is False:
                return f'{self._mines_near}'
            else:
                return '@'
