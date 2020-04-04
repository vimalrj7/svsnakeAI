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
'''