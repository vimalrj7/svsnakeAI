class hamiltonian:
    def __init__(self, board_size, reverse = False):
        self.board_size = board_size
        self.reverse = reverse

    #NORMAL HAM
    def get_normal_coordinate(self, coordinate):
        x, y = coordinate[0], coordinate[1]

        if x > 0 and x < self.board_size - 1 and y == 0:
            x -= 1
        
        else: 
            if x % 2 == 0:
                if y == self.board_size - 1:
                    x += 1
                else:
                    y += 1

            else:
                #at top and not in the last column, take a right
                if y == 1 and x != self.board_size - 1:
                    x += 1
                #at the last column but not in top corner, go up
                elif x == self.board_size - 1 and y != 0:
                    y -= 1
                #at the last column in the top corner, go left
                elif x == self.board_size -1 and y == 0:
                    x -=1
                else:
                    y -= 1

        return [x, y]

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
                #at top and not in the last column, take a right
                if y == 1 and x != self.board_size - 1:
                    x -= 1
                #at the last column but not in top corner, go up
                elif x == self.board_size - 1 and y != 0:
                    y += 1
                #at the last column in the top corner, go left
                elif x == self.board_size -1 and y == 0:
                    x +=1
                else:
                    y += 1

        return [x, y]
    
    #WHAT YOU CALL
    def get_coordinate(self, coordinate):
        if self.reverse:
            return self.get_reverse_coordinate(coordinate)
        else:
            return self.get_normal_coordinate(coordinate)

    #WHAT YOU CALL
    def get_number(self, coordinate):
        start, number = [0, 0], 0
        
        while start != coordinate:
            start = self.get_coordinate(start)
            number += 1

        return number

    #WHAT YOU CALL
    def get_distance(self, head_coords, item_coords):
        head = self.get_number(head_coords)
        item = self.get_number(item_coords)
        if head <= item:
            return item - head
        elif head > item:
            return (self.board_size**2 - (head - item))



    
