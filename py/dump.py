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
            reverse = get_reverse_hamiltonian_coordinate(board_size, ham_move)
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

'''
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

    #GENERAL
    def number_to_coordinate(self, number):
        start, coordinate = 0, [0, 0]

        while start != number:
            start += 1
            coordinate = self.get_coordinate(coordinate)

        return coordinate
'''

'''
#REVERSE HAM
    def get_reverse_coordinate(self, coordinate):
        x, y = coordinate[0], coordinate[1]

        if x > 0 and x < self.board_size - 1 and y == 0:
            x += 1
        
        else: 
            if x % 2 == 0:
                if y == self.board_size - 1:
                    x -= 1
                else:
                    y -= 1

            else:
                #at top and not in the last column, take a left
                if y == 1 and x != self.board_size - 1:
                    x -= 1
                #at the last column but not in top corner, go down
                elif x == self.board_size - 1 and y != 0:
                    y += 1
                #at the last column in the top corner, go right
                elif x == self.board_size -1 and y == 0:
                    x +=1
                else:
                    y += 1

        return [x, y]
'''

'''



from snek import *
from time import sleep
from messing_around import *

def main(vimals_constant):
    #ptr to board
    board = init_board()
    
    play_on = 1
    #show_board(board)
    axis = AXIS_INIT
    direction = DIR_INIT
            
    while (play_on):
        
        #indexing at 0 dereferences the pointer
        x_head, y_head = board[0].snek[0].head[0].coord[x], \
                           board[0].snek[0].head[0].coord[y]

        x_tail, y_tail = board[0].snek[0].tail[0].coord[x], \
                           board[0].snek[0].tail[0].coord[y]

        head = [x_head, y_head]
        tail = [x_tail, y_tail]
        
        #print("====================================================")

        #gets food
        food = get_food_coordinates(BOARD_SIZE, board[0].cell_value)

        #if food != [-1, -1]:
            #print("FOOD FOUND at:", food)

        next_move = choose_move(head, tail, food, BOARD_SIZE, board[0], CYCLE_ALLOWANCE, vimals_constant)
        #print("NEXT MOVE:", next_move)
        axis, direction = convert_to_move(head, next_move)
        #print("====================================================")

        play_on = advance_frame(axis, direction, board)

        if board[0].snek[0].length == BOARD_SIZE**2 - 1:
            play_on = 0

        #show_board(board)
        #sleep(0.3)
    
    #pass by reference to clean memory
    score = get_score()
    length = (board[0].snek[0].length)
    if length == (BOARD_SIZE*BOARD_SIZE) - 1:
        win = "YES"
        length += 1
    else:
        win = "NO"

    print(win)
    
    end_game(byref(board))
    return [score, length, win]


def test():
    with open("data/data1.csv", 'w') as f:
        f.write("Sample:,Score:,Length:,Win:,Vimal's Consant:\n")
        for i in range(-20, 21, 4):
            for j in range(1,31):
                result = main(i)
                f.write("{}, {}, {}, {}, {}\n".format(j, result[0], result[1], result[2], i))

print(main(-20))
print(main(-20))
    

    
    

