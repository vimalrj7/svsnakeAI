from snek import *
from time import sleep
from messing_around import *

if __name__ == "__main__":
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
        curr_frame = get_curr_frame()
        next_move = choose_move(head, tail, food, BOARD_SIZE, board[0], CYCLE_ALLOWANCE, curr_frame)
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
        win = 1
        print("WIN!")
        length += 1

    else:
        win = 0 
    
    end_game(byref(board))
    
    with open("data/data1.csv", 'a') as f:
        f.write("{}, {}, {}\n".format(score, length, win))
    
    print("{}, {}, {}\n".format(score, length, win))
    

    
    

