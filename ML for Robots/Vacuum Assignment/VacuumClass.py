import random

class Vacuum: 
    def __init__(self, location_row, location_col):
        self.performance_score = 0
        self.location_row = location_row
        self.location_col = location_col

    def checkDirt(self, array):
        if (array[self.location_row][self.location_col] > 0):
            return True
    
    def suck(self, array):
        
        # add increment performance score
        self.performance_score = self.performance_score + array[self.location_row][self.location_col]

        print(f"S ", round(self.performance_score, 2))

        # set location to be clean
        array[self.location_row][self.location_col] = 0
    
    def moveLeft(self):
        self.location_col = self.location_col - 1
        print("L ", round(self.performance_score, 2))
        
    def moveRight(self):
        self.location_col = self.location_col + 1
        print("R ", round(self.performance_score, 2))

    def moveUp(self):
        self.location_row = self.location_row - 1
        print("U ", round(self.performance_score, 2))

    def moveDown(self):
        self.location_row = self.location_row + 1
        print("D ", round(self.performance_score, 2))

    def determineMove(self, array, rows, cols):
        
        current_row = self.location_row
        current_col = self.location_col
        possible_moves = []

        # if along left wall
        if (current_col == 0):    
            # consider location to the right
            possible_moves.append((current_row, current_col + 1, array[current_row][current_col + 1]))

            # if not at top left corner or bottom left corner
            # consider location above and below
            if (current_row > 0 and current_row < rows):
                possible_moves.append((current_row + 1, current_col, array[current_row + 1][current_col]))

                possible_moves.append((current_row - 1, current_col, array[current_row - 1][current_col]))

            else:
                # if at top left corner, consider location below
                if (current_row == 0):
                    possible_moves.append((current_row + 1, current_col, array[current_row + 1][current_col]))
                
                else: # if at bottom left corner, consider location above
                    possible_moves.append((current_row - 1, current_col, array[current_row - 1][current_col]))

        # if on top row
        # top left is eliminated by if above
        if (current_row == 0 and current_col != 0):
            # consider location below and left
            possible_moves.append((current_row + 1, current_col, array[current_row + 1][current_col]))

            possible_moves.append((current_row, current_col - 1, array[current_row][current_col - 1]))

            # if not at top right, consider right
            if (current_col < cols):
                possible_moves.append((current_row, current_col + 1, array[current_row][current_col + 1]))

        # if on right wall
        # top right is eliminated by if above
        if (current_col == cols and current_row != 0):
            # consider location above and left
            possible_moves.append((current_row - 1, current_col, array[current_row - 1][current_col]))

            possible_moves.append((current_row, current_col - 1, array[current_row][current_col - 1]))

            # if not at bottom right, consider below
            if (current_row < rows):
                possible_moves.append((current_row + 1, current_col, array[current_row + 1][current_col]))

        # if on bottom wall
        # bottom right and bottom left are eliminated by if above
        if (current_row == rows and current_col != 0 and current_col != cols):
            # if reaches here, not in a corner
            # consider up, right, and left
            possible_moves.append((current_row - 1, current_col, array[current_row - 1][current_col]))

            possible_moves.append((current_row, current_col - 1, array[current_row][current_col - 1]))

            possible_moves.append((current_row, current_col + 1, array[current_row][current_col + 1]))

        
        # if somewhere in middle of grid, look all directions
        if ((0 < current_row < rows) and (0 < current_col < cols)):
            possible_moves.append((current_row - 1, current_col, array[current_row - 1][current_col]))

            possible_moves.append((current_row, current_col - 1, array[current_row][current_col - 1]))

            possible_moves.append((current_row, current_col + 1, array[current_row][current_col + 1]))           

            possible_moves.append((current_row + 1, current_col, array[current_row + 1][current_col])) 

        # print("Possible moves are: ")
        # print(possible_moves)

        best_choice = (0, 0, 0)
        # look through list and find the highest value
        for move in possible_moves:
            if (move[2] > best_choice[2]):
                best_choice = (move[0], move[1], move[2])

        #*****************add random choice here for if two squares are equal ***************************

        if (best_choice[2] == 0):
            best_choice = random.choice(possible_moves)

        # now actually move
        # if best choice is left
        if (best_choice[0] == current_row - 1):
            self.moveUp()
            
        # if best choice is right
        if (best_choice[0] == current_row + 1):
            self.moveDown()

        # if best choice is up
        if (best_choice[1] == current_col - 1):
            self.moveLeft()

        # if best choice is down
        if (best_choice[1] == current_col + 1):
            self.moveRight()

                



