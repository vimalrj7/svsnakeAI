from snek import *
from math import *

reverse = 0

def get_food_coordinates(board_size, board):
    food = [-1,-1]
    for i in range(0, board_size):
        for j in range(0, board_size):
            if board[i][j] != 0:
                food[1] = i
                food[0] = j
    return food


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

def number_to_coordinate(board_size, number):
    start, coordinate = 0, [0, 0]
    while start != number:
        start += 1
        coordinate = get_hamiltonian_coordinate(board_size, coordinate)
    return coordinate

def get_converse_hamiltonian_coordinate(board_size, coordinate):
    ham_num = get_hamiltonian_number(board_size, coordinate)
    converse = 0
    
    if ham_num == 1:
        converse = board_size**2 - 1

    elif ham_num == 0:
        converse = board_size**2 - 2

    else:
        converse = ham_num - 2
    
    converse_coordinate = number_to_coordinate(board_size, converse)
    return converse_coordinate

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

def short_moves(head_coords, food_coords, board):
    x, y = head_coords[0], head_coords[1]
    print("X:",x,"Y:",head_coords[1])
    move_list = []
    
    if food_coords[0] > x:
        move_list.append([x+1, y])
    elif food_coords[0] < x:
        move_list.append([x-1, y])
        
    #move1 = [x, head_coords[1]]

    if food_coords[1] > y:
        move_list.append([x, y+1])
    elif food_coords[1] < y:
        move_list.append([x, y-1])

    #move2 = [head_coords[0], y]

    print("POSSIBLE MOVES:", move_list)
    clean_moves = []

    for move in move_list:
        x = move[0]
        y = move[1]

        if board[y][x] != 1:
            clean_moves.append(move)
        else:
            print("REJECTED [{}, {}]".format(x,y))
            

    return clean_moves

def get_hamiltonian_distance(head, item, board_size):
    if head <= item:
        return item - head
    elif head > item:
        return (board_size**2 - (head - item))

def choose_move(head_coords, tail_coords, food_coords, board_size, board):
    head_val = get_hamiltonian_number(board_size, head_coords)
    tail_val = get_hamiltonian_number(board_size, tail_coords)

    ham_move = get_hamiltonian_coordinate(board_size, head_coords)

    print("Head at:", head_val)
    print("Tail at:", tail_val)
    
    if food_coords != [-1, -1]:
        food_val = get_hamiltonian_number(board_size, food_coords)
    else:
        print("No food, going ham!")
        return ham_move

    moves = short_moves(head_coords, food_coords, board)
    
    distanceto_tail = get_hamiltonian_distance(head_val, tail_val, board_size) - 1
    distanceto_food = get_hamiltonian_distance(head_val, food_val, board_size)

    for move in moves:
        move_number = get_hamiltonian_number(board_size, move)
        print("Distance to tail:", distanceto_tail)
        print("Distance to food:", distanceto_food)
        distanceto_move = get_hamiltonian_distance(head_val, move_number, board_size)
        print("Distance to move:", distanceto_move)
        if distanceto_move < distanceto_tail or distanceto_move <= distanceto_food:
            print("Taking shortcut!")
            return move
    
    print("Can't take shortcut, going ham!")
    return ham_move
    
''' 
def choose_move(head_coords, tail_coords, food_coords, board_size, board):

    #gets the hamiltonian numbers for the head and food coordinates
    head_val = get_hamiltonian_number(board_size, head_coords)
    tail_val = get_hamiltonian_number(board_size, tail_coords)

    ham_move = get_hamiltonian_coordinate(board_size, head_coords)
    #checks if food does not exist
    if food_coords == [-1, -1]: 
        #if the the next hamiltonian move is valid, it takes
        if board[ham_move[1]][ham_move[0]] != 1:
            print("No food, going ham!")
            return ham_move
        #if it's not valid, it takes the reverse hamiltonian
        else:
            print("No food, going reverse ham!")
            reverse = get_converse_hamiltonian_coordinate(board_size, ham_move)
            return reverse

    food_val = get_hamiltonian_number(board_size, food_coords)

    moves = short_moves(head_coords, food_coords, board)
    
    for move in moves:
        #if the move generated is equal to the ham move, keep checking
        if move == ham_move:
            continue
        move_val = get_hamiltonian_number(board_size, move)
        if head_val == tail_val:
            print("Taking shorcut.")
            return move
        elif head_val < tail_val:
            if move_val < tail_val and move_val < food_val:
                print("Taking shorcut.")
                return move
        elif head_val > tail_val:
            if move_val > head_val and move_val < ((board_size**2)-1):
                move_val -= ((board_size**2)-1)
                if move_val < tail_val and move_val < food_val:
                    print("Taking shorcut.")
                    return move
            elif move_val > -1 and move_val < tail_val:
                if move_val < tail_val and move_val < food_val:
                    print("Taking shorcut.")
                    return move

    if board[ham_move[1]][ham_move[0]] != 1:
        print("Can't take shortcut. Doing Hamiltonian.")
        return ham_move
    else:
        print("Can't take shortcut or hamiltonian move. Doing converse hamiltonian.")
        reverse = get_converse_hamiltonian_coordinate(board_size, ham_move)
        return reverse
    

    print("No conditions met.")

    return ham_move
'''

print(get_hamiltonian_number(10, [8, 1]))
    

    
