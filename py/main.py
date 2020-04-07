from snek import *
from time import sleep
from messing_around import *

if __name__ == "__main__":
    #ptr to board
    board = init_board()
    
    play_on = 1
    show_board(board)
    axis = AXIS_INIT
    direction = DIR_INIT
    current_frame = 0
            
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

        if food != [-1, -1]:
            current_frame += 1
        else:
            current_frame = 0

        next_move = choose_move(head, tail, food, BOARD_SIZE, board[0], CYCLE_ALLOWANCE, current_frame)
        #print("NEXT MOVE:", next_move)
        axis, direction = convert_to_move(head, next_move)
        #print("====================================================")

        '''
        go_x = (axis == AXIS_Y and direction == 1 and y_coord == (BOARD_SIZE - 1)) or \
               (axis == AXIS_Y and direction == -1 and y_coord == 0)
        
        go_y = (axis == AXIS_X anpyd direction == 1 and x_coord == (BOARD_SIZE - 1)) or \
               (axis == AXIS_X and direction == -1 and x_coord == 0)
               
        if go_x:
            axis = AXIS_X
            direction = RIGHT if x_coord < BOARD_SIZE // 2 else LEFT
        elif go_y:
            axis = AXIS_Y
            direction = DOWN if y_coord < BOARD_SIZE // 2 else UP
        '''

        play_on = advance_frame(axis, direction, board)
        show_board(board)
        sleep(0.01)

        if board[0].snek[0].length == BOARD_SIZE**2 - 1:
            play_on = 0
    
    #pass by reference to clean memory  
    end_game(byref(board))
