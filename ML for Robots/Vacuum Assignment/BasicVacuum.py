import random

class BasicVacuum: 
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

        # if not on right wall, look right
        if (current_col < cols):
            possible_moves.append((current_row, current_col + 1, array[current_row][current_col + 1]))

        # if not on left wall, look left
        if (current_col > 0):
            possible_moves.append((current_row, current_col - 1, array[current_row][current_col - 1]))

        # if not on bottom row, look down
        if (current_row < rows):
            possible_moves.append((current_row + 1, current_col, array[current_row + 1][current_col])) 

        # if not on top row, look up
        if (current_row > 0):
            possible_moves.append((current_row - 1, current_col, array[current_row - 1][current_col]))

        # choose randomly since the robot doesn't know anything
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
