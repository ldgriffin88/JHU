import numpy
import sys
import random
import copy
"""
File: vacuum_agent.py
Author: Logan Griffin
Date: 6-17-2025

Description: This file includes classes for 3 different types of vacuum robots (BasicVacuum, Vacuum, and SmartVacuum). This file reads from a text file that should be specified as "environ.txt" The main function reads the file and creates a grid of dirtiness values for each vacuum to use, declares a starting location for each vacuum, and states how many moves the vacuum has.Descriptions of how each vacuum works are in their class definition.

The main function reads the "environ.txt" file once and creates one instance of each type of vacuum. It then runs each vacuum for the number of moves specifiedon the grid from the txt file. It outputs every move the vacuum takes along with its performacne score. The grid is printed every 5 moves. The BasicVacuum is run first, then the regular Vacuum, then the SmartVacuum.

TO RUN: be in this file's directory. Ensure that "environ.txt" is also in the directory.

RUN: 
    Command prompt: vacuum_agent.py < environ.txt > output.txt
    Powershell: Get-Content ./environ.txt -Raw | python vacuum_agent.py > ./output.txt
"""




class BasicVacuum:
    """
    Description: This class simulates a basic vacuum. THe basic vacuum can only see its current location within a grid. First, it determines whether its current location is dirty or not. If it's dirty, the vacuum will suck and then randomly move to another location. If it's clean, the vacuum will simply move randomly. This process repeats for the allotted number of steps.

    Attributes:
        - location_row
        - location_col
    """

    def __init__(self, location_row, location_col):
        """
        Initializes basic vacuum with a location row, location column and a performance score of 0.
        """
        self.performance_score = 0
        self.location_row = location_row
        self.location_col = location_col

    def checkDirt(self, array):
        """
        Checks the vacuum's current location in an array to see if it is dirty. Returns True if the location is dirty.
        """
        if (array[self.location_row][self.location_col] > 0):
            return True
        
    def suck(self, array):
        """
        Takes in an array and zeros out the dirtiness score on the vacuum's current location. That dirtiness score is added to the vacuum's performance score.
        """
        # add increment performance score
        self.performance_score = self.performance_score + array[self.location_row][self.location_col]

        print(f"S ", round(self.performance_score, 2))

        # set location to be clean
        array[self.location_row][self.location_col] = 0

    def moveLeft(self):
        """
        Moves the vacuum's location in the grid one column to the left.
        """
        self.location_col = self.location_col - 1
        print("L ", round(self.performance_score, 2))
        
    def moveRight(self):
        """
        Moves the vacuum's location in the grid one column to the right.
        """
        self.location_col = self.location_col + 1
        print("R ", round(self.performance_score, 2))

    def moveUp(self):
        """
        Moves the vacuum's location in the grid one row up.
        """
        self.location_row = self.location_row - 1
        print("U ", round(self.performance_score, 2))

    def moveDown(self):
        """
        Moves the vacuum's location in the grid one row down.
        """
        self.location_row = self.location_row + 1
        print("D ", round(self.performance_score, 2))

    def determineMove(self, rows, cols):
        """
        Takes the vacuum's current location and determines it's possible moves based on the grid size (rows, cols). Then chooses randomly from the possible moves and moves the vacuum.
        """
        current_row = self.location_row
        current_col = self.location_col
        possible_moves = []

        # if not on right wall, can move right
        if (current_col < cols):
            possible_moves.append((current_row, current_col + 1))

        # if not on left wall, can move left
        if (current_col > 0):
            possible_moves.append((current_row, current_col - 1))

        # if not on bottom row, can move down
        if (current_row < rows):
            possible_moves.append((current_row + 1, current_col)) 

        # if not on top row, can move up
        if (current_row > 0):
            possible_moves.append((current_row - 1, current_col))

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

class Vacuum(BasicVacuum):
    """
    Description: This class simulates a slightly more intelligent vacuum than a basic vacuum. This vacuum can now see the 4 locations next to it. From those locations, it uses a greedy choice to move to the location with the highest dirtiness value. If two possible moves have the same dirtiness value, the vacuum will randomly choose between them.

    Inherits from BasicVacuum class:
    - moveUp()
    - moveDown()
    - moveLeft()
    - moveRight()
    - checkDirt(array)
    - suck(array)

    Own Methods:
    - determineMove(array, rows, cols)

    """ 
    def __init__(self, location_row, location_col):
        """
        Initializes basic vacuum with a location row, location column and a performance score of 0 by calling inherited constructor.
        """
        super().__init__(location_row, location_col)

    def determineMove(self, array, rows, cols):
        """
        Determines which direction the vacuum can and should move based on a greedy choice and its location in the grid.
        """
        # get current location
        current_row = self.location_row
        current_col = self.location_col

        # to store possible moves
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


        # initialize score and locations
        best_score = 0
        best_locations = []

        # look through possible moves and find the highest value
        for move in possible_moves:
            # add to list of best moves
            if (move[2] == best_score):
                best_locations.append(move)
            # if better score, clear list and add current move
            elif (move[2] > best_score):
                best_score = move[2]
                best_locations.clear()
                best_locations.append(move)

        # choose randomly if zeros or more than one best choice
        if len(best_locations) > 1 or best_score == 0:
            best_choice = random.choice(best_locations)
        else: 
            # if only one best choice
            best_choice = best_locations[0]

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

class SmartVacuum(BasicVacuum): 
    """
    Description: This class simulates a vacuum that is smarter than a regular vacuum. A SmartVacuum can remember where it has been and the adjacent locations it has seen. To determine it's moves, it calculates a score for every loaiton it has seen that was dirty. It then chooses the best location and moves to it or towards it. If there are multiple locations that have the same best score, the vacuum will choose randomly. If the best location is diagonal from the vacuum's current location, it will move in the direction of the best score immediately next to it that is on the path to the diagonal location.

    Inherits from BasicVacuum class:
    - moveUp()
    - moveDown()
    - moveLeft()
    - moveRight()
    - checkDirt(array)
    - suck(array)

    Own Methods:
    - determineMove
    - assess
    """ 
    def __init__(self, location_row, location_col):
        """
        Initializes basic vacuum with a location row, location column and a performance score of 0 by calling inherited constructor. A dictionary is also created to store the vacuums memory. The dictionary is keyed by location and maps to the dirtiness value at that location.
        """
        super().__init__(location_row, location_col)

        # create dictionary for storing locations and values
        self.memory: dict[tuple[int,int], float] = {}

    def assess (self, array, rows, cols):
        """
        Uses the vacuum's current location to look at the surrounding locations and add their dirtiness value to its memory.
        """
        # get location
        current_row = self.location_row
        current_col = self.location_col
        
        # add current location to dictionary
        self.memory[(current_row, current_col)] = array[current_row][current_col]

        # if not on right wall, look right and add to dictionary
        if (current_col < cols):
            self.memory[(current_row, current_col + 1)] = array[current_row][current_col + 1]

        # if not on left wall, look left and add to dictionary
        if (current_col > 0):
            self.memory[(current_row, current_col - 1)] = array[current_row][current_col - 1]

        # if not on bottom row, look down and add to dictionary
        if (current_row < rows):
            self.memory[(current_row + 1, current_col)] = array[current_row + 1][current_col]

        # if not on top row, look up and add to dictionary
        if (current_row > 0):
            self.memory[(current_row - 1, current_col)] = array[current_row - 1][current_col]

    def determineMove(self, rows, cols):
            """
            To determine it's next move, the vacuum goes through all the locations it has seen that were dirty. It then calculates a score based on dirtiness divided by manhattan distance to that location. Next, it determines the location or locations that have the best score(s). If more than one location, it chooses randomly. Once a location is determined, it decides how to get there. If the location is diagonal, it will move in the direction that haas the higher dirtiness score adjacent to its current location. For example, if the best location was diagonal up and to the right, it would look at the locations directly above and to the right of it and choose whichever has the highest value.
            """
            best_locations = []
            best_score = -1    

            # go through all locations seen
            for (r, c), dirtiness in self.memory.items():
                # skip locations that don't have dirt
                if dirtiness <= 0:
                    continue

                # find manhattan distance from current location
                distance = abs(r - self.location_row) + abs(c - self.location_col)
                
                # to avoid division by zero for current location
                if distance == 0:
                    continue

                # calculate a score for that location
                score = dirtiness / distance

                # if score matches best score, add it to list
                if score == best_score:
                    best_locations.append((r,c))

                # if score is better than best score, empty list and add new score
                if score > best_score:
                    best_score = score
                    best_locations.clear()
                    best_locations.append((r,c))

            # if there are no locations worth going towards, pick randomly
            if len(best_locations) == 0:

                random_moves = []

                if self.location_row > 0:
                    random_moves.append("U")
                if self.location_row < rows - 1:
                    random_moves.append("D")
                if self.location_col > 0:
                    random_moves.append("L")
                if self.location_col < cols - 1:
                    random_moves.append("R")
                
                random_move = random.choice(random_moves)
                
                if random_move == "U":
                    self.moveUp()
                elif random_move == "D":
                    self.moveDown()
                elif random_move == "L":
                    self.moveLeft()
                elif random_move == "R":
                    self.moveRight()
            
            # if there is at least one best location
            else: 
                
                # if multiple locations have the best score, choose randomly
                target_location = random.choice(best_locations)

                target_row, target_column = target_location

                # to determine direction to go
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

                # if best choice is diagonal
                if len(possible_moves) == 2:

                    diagonal_choice = []

                    # if above, get score
                    if possible_moves.count("UP") == 1:
                        score = self.memory[(self.location_row - 1, self.location_col)]

                        diagonal_choice.append(("UP", score))

                    # if below, get score
                    if possible_moves.count("DOWN") == 1:
                        score = self.memory[(self.location_row + 1, self.location_col)]

                        diagonal_choice.append(("DOWN", score))

                    # if to the left, get score
                    if possible_moves.count("LEFT") == 1:
                        score = self.memory[(self.location_row, self.location_col - 1)]

                        diagonal_choice.append(("LEFT", score))

                    # if to the right, get score
                    if possible_moves.count("RIGHT") == 1:
                        score = self.memory[(self.location_row, self.location_col + 1)]

                        diagonal_choice.append(("RIGHT", score))

                    # take the higher score from the two possible directions
                    move = max(diagonal_choice, key=lambda pair: pair[1])[0]
                else:
                    # if not diagonal
                    move = possible_moves[0]

                # move vacuum
                if move == "UP":
                    self.moveUp()
                elif move == "DOWN":
                    self.moveDown()
                elif move == "LEFT":
                    self.moveLeft()
                elif move == "RIGHT":
                    self.moveRight()

def printGrid(array, location_row, location_col, rows, cols):
    """
    This function prints the grid and places brackets around a vacuum's current location.
    """
    print("\n")

    # loop through grid
    for i in range(rows):
        for j in range(cols):
            # if index matches vacuum's location
            if i == location_row and j == location_col:
                print("[", array[i][j], "]", " ", end=" ")
            else:
                print(array[i][j], " ", end=" ")
        
        print("")

    print("\n")

def getGridFromFile():
    """
    This function creates the grid and gathers information from the "environ.txt" file.
    """
    content = sys.stdin.read().splitlines()

    grid_size = content[0].split()
    # get dimensions as ints
    rows = int(grid_size[1])
    cols = int(grid_size[2])

    # zeros array
    grid_array = numpy.zeros((rows, cols))

    # go through and assign dirtiness values
    for i in range(rows):

        dirt_line = content[2 + i].split()

        for j in range(cols):
            grid_array[i][j] = dirt_line[j]

    # get number of moves from file
    available_moves = content[2 + rows].split()
    moves_remaining = int(available_moves[1])

    # get starting location from file
    location = content[3 + rows].split()
    location_row = int(location[1])
    location_col = int(location[2])

        
    return grid_array, moves_remaining, location_row, location_col, rows, cols 

def main():
        
        # read "environ.txt" file
        grid, moves_remaining, location_row, location_col, rows, cols = getGridFromFile()    

        # copy array for each vacuum
        grid_array_1 = copy.deepcopy(grid)
        grid_array_2 = copy.deepcopy(grid)
        grid_array_3 = copy.deepcopy(grid)

        # set moves
        moves_remaining_1 = moves_remaining_2 = moves_remaining_3 = moves_remaining

        # only used for printing
        move_counter_1 = move_counter_2 = move_counter_3 = 0

        # print vacuum starting location
        print("STARTING LOCATION IS", location_row, ",", location_col)

        # create vacuums and adjust location for array reference
        vac = BasicVacuum(location_row - 1, location_col - 1)
        vac2 = Vacuum(location_row - 1, location_col - 1)
        vac3 = SmartVacuum(location_row - 1, location_col - 1)

        # # BasicVacuum running
        while moves_remaining_1 > 0:
            # print grid every 5 moves
            if (move_counter_1 % 5 == 0 and move_counter_1 > 0):
                printGrid(grid_array_1, vac.location_row, vac.location_col, rows, cols)        

            # if there is dirt, suck
            if vac.checkDirt(grid_array_1):
                move_counter_1 = move_counter_1 + 1
                vac.suck(grid_array_1)
                moves_remaining_1 = moves_remaining_1 - 1

                # stop if last move is used to suck
                if moves_remaining_1 == 0:
                    continue
                # print grid every 5 moves
                if (move_counter_1 % 5 == 0 and move_counter_1 > 0):
                    printGrid(grid_array_1, vac.location_row, vac.location_col, rows, cols) 

            move_counter_1 = move_counter_1 + 1

            # determine next move
            vac.determineMove(rows - 1, cols - 1)

            moves_remaining_1 = moves_remaining_1 - 1
            
        print("\n\n\n\n***********************")
        print(" STAGE 2 VACUUM ")
        print("***********************\n\n")

        while moves_remaining_2 > 0:
            # print grid every 5 moves
            if (move_counter_2 % 5 == 0 and move_counter_2 > 0):
                printGrid(grid_array_2, vac2.location_row, vac2.location_col, rows, cols)        

            # if there is dirt, suck
            if vac2.checkDirt(grid_array_2):
                move_counter_2 = move_counter_2 + 1
                vac2.suck(grid_array_2)
                moves_remaining_2 = moves_remaining_2 - 1

                # stop if last move is used to suck
                if moves_remaining_2 == 0:
                    continue
                # print grid every 5 moves
                if (move_counter_2 % 5 == 0 and move_counter_2 > 0):
                    printGrid(grid_array_2, vac2.location_row, vac2.location_col, rows, cols) 

            move_counter_2 = move_counter_2 + 1

            #determine next move
            vac2.determineMove(grid_array_2, rows - 1, cols - 1)

            moves_remaining_2 = moves_remaining_2 - 1

        print("\n\n\n\n***********************")
        print(" STAGE 3 VACUUM ")
        print("***********************\n\n")

        while moves_remaining_3 > 0:
            # print grid every 5 moves
            if (move_counter_3 % 5 == 0) and move_counter_3 > 0:
                printGrid(grid_array_3, vac3.location_row, vac3.location_col, rows, cols)        

            # if there is dirt
            if vac3.checkDirt(grid_array_3):
                move_counter_3 = move_counter_3 + 1
                vac3.suck(grid_array_3)
                moves_remaining_3 = moves_remaining_3 - 1

                # stop if last move is used to suck
                if moves_remaining_1 == 0:
                    continue
                # print grid every 5 moves
                if (move_counter_3 % 5 == 0 and move_counter_3 > 0):
                    printGrid(grid_array_3, vac3.location_row, vac3.location_col, rows, cols) 

            move_counter_3 = move_counter_3 + 1

            # add adjacent location to memory
            vac3.assess(grid_array_3, rows - 1, cols - 1)

            # choose next move
            vac3.determineMove(rows - 1, cols - 1)

            moves_remaining_3 = moves_remaining_3 - 1

if __name__== "__main__":
    main()




    