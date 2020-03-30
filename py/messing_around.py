from snek import *

def get_hamiltonian_coordinate(board_size, coordinate):
    x, y = coordinate[0], coordinate[1]

    if x > 0 and x < board_size - 1 and y == 0:
        x -= 1
    
    else: 
        if x % 2 == 0:
            if y == board_size -1:
                x += 1
            else:
                y += 1

        else:
            #at top and not in the last column, take a right
            if y == 1 and x != board_size - 1:
                x += 1
            #at the last column but not in top corner, go up
            elif x == board_size - 1 and y != 0:
                y -= 1
            #at the last column in the top corner, go left
            elif x == board_size -1 and y == 0:
                x -=1
            else:
                y -= 1

    return [x, y]

def convert_to_move(current, new):
    difference = [0, 0]
    difference[0], difference[1] = new[0] - current[0], new[1] - current[1]

    axis, direction = 0, 0

    if difference == [0, 1]:
        axis = AXIS_Y
        direction = DOWN

    elif difference == [0, -1]:
        axis = AXIS_Y
        direction = UP
    
    elif difference == [1, 0]:
        axis = AXIS_X
        direction = RIGHT
    
    else:
        axis = AXIS_X
        direction = LEFT

    return axis, direction

    
