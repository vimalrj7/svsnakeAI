from snek import *
from hamiltonian import *


def get_food_coordinates(board_size, board):
    '''
    Find the coordinates of the food on the board.\n
    (int, int[2]) -> int[2]
    '''
    
    #the coordinates that are returned if no food is found
    food = [-1, -1]

    #searches occupany array for existence of food
    for i in range(0, board_size):
        for j in range(0, board_size):
            if board[i][j] != 0:
                food[1] = i
                food[0] = j

    #returns the coordinates of the food found
    return food


def convert_to_move(current, new):
    '''
    Converts a change in one coordinate to an axis and direction format.\n
    (int[2], int[2]) -> (int, int)
    '''

    #finds the difference in x and y between the next move and current position
    difference = [0, 0]
    difference[0], difference[1] = new[0] - current[0], new[1] - current[1]

    axis, direction = 0, 0

    #determines the axis and direction pair for the difference
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

    #returns the axis and direction pair
    return axis, direction
    

def short_moves(head_coords, food_coords, board):
    '''
    Determines the next possible moves to complete the shortest path to the coordinate given.\n
    (int[2], int[2], c_struct) -> int[][2]
    '''

    x, y = head_coords[0], head_coords[1]
    moves = []

    #only finds the change in x needed
    if food_coords[0] > x:
        moves.append([x+1, y])
    elif food_coords[0] < x:
        moves.append([x-1, y])

    #only finds the change in y needed
    if food_coords[1] > y:
        moves.append([x, y+1])
    elif food_coords[1] < y:
        moves.append([x, y-1])

    clean_moves = []

    #checks if the shortcut move is occupied
    for move in moves:
        x = move[0]
        y = move[1]

        if board.occupancy[y][x] != 1:
            clean_moves.append(move)

    #returns all the non-occupied moves
    return clean_moves


def choose_move(head_coords, tail_coords, food_coords, board_size, board, cycle_allowance, current_frame):
    '''
    Determines the most appropriate move to take based on several cases.\n
    (int[2], int[2], int[2], int, c_struct, int, int) -> int[2]
    '''

    #creates an instance of the hamiltonian class
    ham = hamiltonian(board_size)

    #generates the next move in the hamiltonian cycle
    ham_move = ham.get_coordinate(head_coords)

    #only tries to take shortcuts if food is present
    if food_coords != [-1, -1]:
        #calculates the hamiltonian distances from the head to the specified coordinates
        distanceto_tail = ham.get_distance(head_coords, tail_coords) - 1
        distanceto_food = ham.get_distance(head_coords, food_coords)
        distanceto_right = ham.get_distance(head_coords, [board_size - 1, 0])

        #calculates the time out for the given cycle allowance and board size
        time_out = (4 * board_size - 4) * cycle_allowance

        #if it's possible to get to the food using the hamiltonian cycle without timing out 
        if distanceto_food <= (time_out - current_frame):
            return ham_move
        
        #if not it will generate shortcuts to take
        moves = short_moves(head_coords, food_coords, board)
        
        for move in moves:
            #if the snake is only 1 long, it will only take shortcuts
            if distanceto_tail == -1:
                return move

            #calculates the hamiltonian distance to the shortcut
            distanceto_move = ham.get_distance(head_coords, move)

            #only takes the shortcut if it's not overtaking the tail in the hamiltonian path
            if distanceto_move < distanceto_tail and distanceto_move <= distanceto_food:
                return move

            #if the food is far behind the snake in the hamiltonian path, it will take a shortcut to the top right of the board
            if head_coords[1] != 0 and distanceto_move > distanceto_food and distanceto_food > distanceto_right:
                shortcuts = short_moves(head_coords, [board_size - 1, 0], board)
                for shortcut in shortcuts:
                    if distanceto_right < distanceto_tail:
                        return shortcut
        
        #takes shortcut to top right even if all the shortcuts to the food are rejected
        if head_coords[1] != 0 and distanceto_food > distanceto_right:
            shortcuts = short_moves(head_coords, [board_size - 1, 0], board)
            for shortcut in shortcuts:
                if distanceto_right < distanceto_tail:
                    return shortcut
    
    #if there is no food, it defaults to the hamiltonian cycle
    return ham_move

    

    
