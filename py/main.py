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
			
	while (play_on):
		#indexing at 0 dereferences the pointer
		x_head, y_head = board[0].snek[0].head[0].coord[x], \
						   board[0].snek[0].head[0].coord[y]

		x_tail, y_tail = board[0].snek[0].tail[0].coord[x], \
						   board[0].snek[0].tail[0].coord[y]

		head = [x_head, y_head]
		tail = [x_head, y_head]

		#print("SNAKE LENGTH:", board[0].cell_value[1][1])
		food = [0,0]
		for i in range(0, BOARD_SIZE):
			for j in range(0, BOARD_SIZE):
				if board[0].cell_value[i][j] != 0:
					print("FOOD FOUND!")
					food[1] = i
					food[0] = j
					print(food)

		print("FOOD at:", food)

		if food == [0,0]:
			ham_move = get_hamiltonian_coordinate(BOARD_SIZE, head)
			axis, direction = convert_to_move(head, ham_move)

		else:
			moves = short_moves(head, food)
			print("POSSIBLE MOVES:", moves)
			next_move = choose_move(head, tail, food, moves, BOARD_SIZE)
			print("NEXT MOVE:", next_move)
			axis, direction = convert_to_move(head, next_move)

		'''
		go_x = (axis == AXIS_Y and direction == 1 and y_coord == (BOARD_SIZE - 1)) or \
			   (axis == AXIS_Y and direction == -1 and y_coord == 0)
		
		go_y = (axis == AXIS_X and direction == 1 and x_coord == (BOARD_SIZE - 1)) or \
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
		sleep(0.65)
	
	#pass by reference to clean memory	
	end_game(byref(board))
