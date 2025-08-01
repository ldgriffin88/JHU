import random

class SmartVacuum: 

    def __init__(self, location_row, location_col):
        self.performance_score = 0
        self.location_row = location_row
        self.location_col = location_col
        self.memory: dict[tuple[int,int], float] = {}

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

    def assess (self, array, rows, cols):

        current_row = self.location_row
        current_col = self.location_col
        
        # add current location
        self.memory[(current_row, current_col)] = array[current_row][current_col]


        # if along left wall
        if (current_col == 0):    
            # consider location to the right
            self.memory[(current_row, current_col + 1)] = array[current_row][current_col + 1]

            # if not at top left corner or bottom left corner
            # consider location above and below
            if (current_row > 0 and current_row < rows):
                self.memory[(current_row - 1, current_col)] = array[current_row - 1][current_col]

                self.memory[(current_row + 1, current_col)] = array[current_row + 1][current_col]

            else:
                # if at top left corner, consider location below
                if (current_row == 0):
                    self.memory[(current_row + 1, current_col)] = array[current_row + 1][current_col]
                
                else: # if at bottom left corner, consider location above
                    self.memory[(current_row - 1, current_col)] = array[current_row - 1][current_col]

        # if on top row
        # top left is eliminated by if above
        if (current_row == 0 and current_col != 0):
            # consider location below and left
            self.memory[(current_row + 1, current_col)] = array[current_row + 1][current_col]

            self.memory[(current_row, current_col - 1)] = array[current_row][current_col - 1]

            # if not at top right, consider right
            if (current_col < cols):
                self.memory[(current_row, current_col + 1)] = array[current_row][current_col + 1]

        # if on right wall
        # top right is eliminated by if above
        if (current_col == cols and current_row != 0):
            # consider location above and left
            self.memory[(current_row - 1, current_col)] = array[current_row - 1][current_col]

            self.memory[(current_row, current_col - 1)] = array[current_row][current_col - 1]

            # if not at bottom right, consider below
            if (current_row < rows):
                self.memory[(current_row + 1, current_col)] = array[current_row + 1][current_col]

        # if on bottom wall
        # bottom right and bottom left are eliminated by if above
        if (current_row == rows and current_col != 0 and current_col != cols):
            # if reaches here, not in a corner
            # consider up, right, and left
            self.memory[(current_row - 1, current_col)] = array[current_row - 1][current_col]

            self.memory[(current_row, current_col + 1)] = array[current_row][current_col + 1]

            self.memory[(current_row, current_col - 1)] = array[current_row][current_col - 1]

        
        # if somewhere in middle of grid, look all directions
        if ((0 < current_row < rows) and (0 < current_col < cols)):
            self.memory[(current_row - 1, current_col)] = array[current_row - 1][current_col]

            self.memory[(current_row, current_col - 1)] = array[current_row][current_col - 1]

            self.memory[(current_row, current_col + 1)] = array[current_row][current_col + 1]           

            self.memory[(current_row + 1, current_col)] = array[current_row + 1][current_col]

    def determineMove(self, rows, cols):

            # check which locations have dirt
            # for those locations, calculate the score based on dirtiness and distance
            # choose the best one and move that way
            # take difference of column and row of best move and current location
            # move accordingly

            best_location = None
            best_score = -1    

            for (r, c), dirtiness in self.memory.items():
                
                if dirtiness <= 0:
                    continue

                distance = abs(r - self.location_row) + abs(c - self.location_col)

                if distance == 0:
                    # to avoid division by zero
                    continue

                score = dirtiness / distance

                if score > best_score:
                    best_score = score
                    best_location = (r,c)

                
            # have the best location
            if best_location == None:

                random_moves = []
                if self.location_row > 0:
                    random_moves.append("UP")
                if self.location_row < rows - 1:
                    random_moves.append("DOWN")
                if self.location_col > 0:
                    random_moves.append("LEFT")
                if self.location_col < cols - 1:
                    random_moves.append("RIGHT")
                # move randomly
                random_move = random.choice(random_moves)
                
                if random_move == "UP":
                    self.moveUp()
                elif random_move == "DOWN":
                    self.moveDown()
                elif random_move == "LEFT":
                    self.moveLeft()
                elif random_move == "RIGHT":
                    self.moveRight()
            
            else: 
                    
                target_row, target_column = best_location

                row_difference = target_row - self.location_row
                column_difference = target_column - self.location_col

                possible_moves = []

                if row_difference < 0:
                    # go up
                    possible_moves.append("UP")

                elif row_difference > 0:
                    # go down
                    possible_moves.append("DOWN")

                if column_difference < 0:
                    # go left
                    possible_moves.append("LEFT")
                elif column_difference > 0:
                    # go right
                    possible_moves.append("RIGHT")

                
                move = random.choice(possible_moves)

                if move == "UP":
                    self.moveUp()
                elif move == "DOWN":
                    self.moveDown()
                elif move == "LEFT":
                    self.moveLeft()
                elif move == "RIGHT":
                    self.moveRight()
                
            


            


            

                
    