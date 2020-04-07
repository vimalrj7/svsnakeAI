class hamiltonian:
    '''
    All the functions required to run a hamiltonian cycle and perform hamiltonian operations.
    '''
    def __init__(self, board_size):
        '''
        Need the board_size to initalize the class.
        (int) -> None
        '''
        self.board_size = board_size

    def get_coordinate(self, coordinate):
        '''
        Gets the next hamiltonian coordinate in the cycle based on the current one.\n
        (int[2]) -> int[2]
        '''
        
        x, y = coordinate[0], coordinate[1]

        #the final horizontal stretch going back to the origin
        if x > 0 and x < self.board_size - 1 and y == 0:
            x -= 1
        
        else:
            #even columns 
            if x % 2 == 0:
                #shift into the next column
                if y == self.board_size - 1:
                    x += 1
                #move up the column
                else:
                    y += 1

            else:
                #at row the before the top and not in the last column, take a right
                if y == 1 and x != self.board_size - 1:
                    x += 1
                #at the last column but not in top corner, go up
                elif x == self.board_size - 1 and y != 0:
                    y -= 1
                #at the last column in the top corner, go left
                elif x == self.board_size -1 and y == 0:
                    x -=1
                #move down the column otherwise
                else:
                    y -= 1

        return [x, y]

    def get_number(self, coordinate):
        '''
        Gets the hamiltonian number for a coordinate on the board.\n
        (int[2]) -> int
        '''
        
        #initialize start and number to zero
        start, number = [0, 0], 0 

        #keep getting next coordinate and adding 1 to the hamiltonian number
        #until the start reaches the coordinate entered
        while start != coordinate:
            start = self.get_coordinate(start)
            number += 1

        #return the resulting number
        return number

    def get_distance(self, head_coords, item_coords):
        '''
        Gets the hamiltonian distance between the head and another coordinate on the board.\n
        (int[2], int[2]) -> int
        '''

        #convert the coordinates to their respective hamiltonian number
        head = self.get_number(head_coords)
        item = self.get_number(item_coords)

        #returns the hamiltonian distance based on the location of the head
        #relative to the item to account for wrap around options
        if head <= item:
            return item - head
        elif head > item:
            return (self.board_size**2 - (head - item))



    
