from snek import *
from math import *

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

def get_hamiltonian_number(board_size, coordinate):
    start, number = [0, 0], 0
    while start != coordinate:
        start = get_hamiltonian_coordinate(board_size, start)
        number += 1
    return number

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

def shortest_path(coordinate, food_coordinate):
    difference = [0, 0]
    difference[0], difference[1] = food_coordinate[0] - coordinate[0], food_coordinate[1] - coordinate[1]
    change = [1, 1]
    distance = abs(difference[0]) + abs(difference[1])
    moves = [[0,0] for i in range(abs(distance))]

    if difference != [0, 0]:
        if difference[0] < 0:
            change[0] = -1
        if difference[1] < 0:
            change[1] = -1
        
        for i in range(abs(difference[0])):
            moves[i][0] = coordinate[0] + (i + 1)*change[0]
            moves[i][1] = coordinate[1]
            
        for j in range(i + 1, distance):
            moves[j][1] = coordinate[1] + (j - i)*change[1]
            moves[j][0] = moves[i][0]
            
    return moves

def choose_move(head_coords, tail_coords, food_coords, short_moves, board_size):
    head_val = get_hamiltonian_number(board_size, head_coords)
    tail_val = get_hamiltonian_number(board_size, tail_coords)
    food_val = get_hamiltonian_number(board_size, food_coords)

    ham_move = get_hamiltonian_number(board_size, head_coords)


    for move in short_moves:
        if move == ham_move:
            continue
        move_val = get_hamiltonian_number(board_size, move)
        if head_val < tail_val:
            if move_val < tail_val:
                return move
        if head_val > tail_val:
            if move_val > head_val and move_val < ((board_size**2)-1):
                move_val -= ((board_size**2)-1)
                if move_val < tail_val:
                    return move
            elif move_val > -1 and move_val < tail_val:
                return move

    print("Can't take shortcut, following hamiltonian")

    return ham_move


print(shortest_path([1,2], [3,0]))

move = choose_move([1,2], [1,0], [3,0], [[1,1], [2,2]], 4)
print(move)

            
    

    
