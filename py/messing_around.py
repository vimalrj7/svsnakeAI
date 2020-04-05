from snek import *
from math import *
from hamiltonian import *

def get_food_coordinates(board_size, board):
    food = [-1,-1]
    for i in range(0, board_size):
        for j in range(0, board_size):
            if board[i][j] != 0:
                food[1] = i
                food[0] = j
    return food

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
    
def short_moves(head_coords, food_coords, board):
    x, y = head_coords[0], head_coords[1]
    print("X:",x,"Y:",head_coords[1])
    moves = []
    
    if food_coords[0] > x:
        moves.append([x+1, y])
    elif food_coords[0] < x:
        moves.append([x-1, y])

    if food_coords[1] > y:
        moves.append([x, y+1])
    elif food_coords[1] < y:
        moves.append([x, y-1])

    print("POSSIBLE MOVES:", moves)
    clean_moves = []

    for move in moves:
        x = move[0]
        y = move[1]

        if board[y][x] != 1:
            clean_moves.append(move)
        else:
            print("REJECTED [{}, {}]".format(x,y))

    return clean_moves

def choose_move(head_coords, tail_coords, food_coords, board_size, board):
    ham = hamiltonian(board_size)

    head_val = ham.get_number(head_coords)
    tail_val = ham.get_number(tail_coords)

    ham_move = ham.get_coordinate(head_coords)

    print("Head at:", head_val)
    print("Tail at:", tail_val)
    
    if food_coords != [-1, -1]:
        food_val = ham.get_number(food_coords)
    else:
        print("No food, going ham!")
        return ham_move

    moves = short_moves(head_coords, food_coords, board)
    
    distanceto_tail = ham.get_distance(head_val, tail_val) - 1
    distanceto_food = ham.get_distance(head_val, food_val)

    for move in moves:
        move_number = ham.get_number(move)
        print("Distance to tail:", distanceto_tail)
        print("Distance to food:", distanceto_food)
        distanceto_move = ham.get_distance(head_val, move_number)
        print("Distance to move:", distanceto_move)
        if distanceto_move < distanceto_tail and distanceto_move <= distanceto_food:
            print("Taking shortcut!")
            return move
    
    print("Can't take shortcut, going ham!")
    return ham_move
    

    

    
