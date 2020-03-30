
def get_hamiltonian_coordinate(board_size, coordinate):
    x, y = coordinate[0], coordinate[1]

    if x > 0 and x < board_size - 1 and y == 0:
        x -= 1
    
    if x % 2 == 0:
        if y == board_size -1:
            x += 1
        else:
            y += 1

    if x % 2 == 1:
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