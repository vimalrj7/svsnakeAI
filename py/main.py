from snek import *
from time import sleep
from algorithm import *

if __name__ == "__main__":
    #ptr to board
    board = init_board()
    
    #initialize values
    play_on = 1
    show_board(board)
    axis = AXIS_INIT
    direction = DIR_INIT
            
    while (play_on):
        
        #indexing at 0 dereferences the pointer
        x_head, y_head = board[0].snek[0].head[0].coord[x], \
                        board[0].snek[0].head[0].coord[y]

        x_tail, y_tail = board[0].snek[0].tail[0].coord[x], \
                        board[0].snek[0].tail[0].coord[y]

        #head and tail coordinates
        head = [x_head, y_head]
        tail = [x_tail, y_tail]
        
        #get food coordinates
        food = get_food_coordinates(BOARD_SIZE, board[0].cell_value)
        #get the current frame
        curr_frame = get_curr_frame()
        #find the next move in coordinate form
        next_move = choose_move(head, tail, food, BOARD_SIZE, board[0], CYCLE_ALLOWANCE, curr_frame)
        #convert the move to an axis and direction pair
        axis, direction = convert_to_move(head, next_move)

        #moves the game forward one frame
        play_on = advance_frame(axis, direction, board)
        
        #displays the board
        show_board(board)
        #creates delay
        sleep(0.1)
        
        #checks if the snake won, notifies player if won and ends the game
        if board[0].snek[0].length == BOARD_SIZE**2 - 1:
            play_on = 0
            print("=================")
            print("WIN!")
            print("=================")
    
    #pass by reference to clean memory  
    end_game(byref(board))
