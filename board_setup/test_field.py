from field import Field

board_data = [[1, 0, 0],
              [0, 0, 0]]


def test_field_create():
    field = Field(False, board_data, 3)
    assert type(field) is Field
    assert field.has_mine() is False
    assert field.mines_near() == 3
