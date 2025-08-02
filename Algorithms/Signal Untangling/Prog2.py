"""
Filename: Prog2.py
Author: Logan Griffin
Created 4/9/25
Description: This file takes a binary string and determines if it can be untangled into the superposition of two interwoven binary signals.
"""
import sys

def new_state(next_char, x, y, seen_states, entries):
    """
    Creates either 1 or 2 new states based on if the character passed matches the first character in the string x, string y, or both. This function calls the check_if_new_state function.

    @param next_char: A character {0, 1} that is currently being examined in the outer loop of untangle().
    @param x: A string representing 1 of the signals in the interweaving.
    @param y: A string representing the other signal in the interweaving.
    @param seen_states: A set storing the substrings and states that have been seen already. Stored in the format: (prefix, chars delegated to x, chars delegated to y, length of chars delegated to x, length of chars delegated to y).
    @param entries: A dictionary storing the states for each prefix. For each prefix, there is a list of states associated with it.

    """    

    # store character as new variable
    new_key = next_char

    # lengths of both input signals
    length_x = len(x)
    length_y = len(y)

    # if the character is the beginning of x and y
    if x[0] == next_char and y[0] == next_char:

            # create new state with first character going to x
            new_state_x = {
                'x': next_char,
                'y': '',
                'x_expected': x[1 % length_x],
                'y_expected': y[0 % length_y]
            }

            # create new state ID
            state_id_x = (new_key, new_state_x['x'], new_state_x['y'], len(new_state_x['x']), len(new_state_x['y']))

            # call function to check if state is new
            check_if_new_state(state_id_x, new_state_x, seen_states, new_key, entries, x, y)  

            # create new state with first character going to y
            new_state_y = {
                'x': '',
                'y': next_char,
                'x_expected': x[0 % length_x],
                'y_expected': y[1 % length_y]
            }       
        
            # create new state ID
            state_id_y = (new_key, new_state_y['x'], new_state_y['y'],  len(new_state_y['x']), len(new_state_y['y']))

            # printing to show process
            print("New x state is: ")
            print(new_state_x)
            print("New y state is: ")
            print(new_state_y)

            # call function to check if state is new
            check_if_new_state(state_id_y, new_state_y, seen_states, new_key, entries, x, y)       

    # if character only matches x first character
    elif x[0] == next_char:

        # create new state with first character going to x
        new_state_x = {
            'x': next_char,
            'y': '',
            'x_expected': x[1 % length_x],
            'y_expected': y[0 % length_y]
        }

        # create new state ID
        state_id_x = (new_key, new_state_x['x'], new_state_x['y'], len(new_state_x['x']), len(new_state_x['y']))

        # printing to show process
        print("New x state is: ")
        print(new_state_x)

        # call function to check if state is new
        check_if_new_state(state_id_x, new_state_x, seen_states, new_key, entries, x, y)

    # if only matches y first character
    elif y[0] == next_char:

        # create new state with first character going to y
        new_state_y = {
            'x': '',
            'y': next_char,
            'x_expected': x[0 % length_x],
            'y_expected': y[1 % length_y]
        } 

        # create new state ID
        state_id_y = (new_key, new_state_y['x'], new_state_y['y'], len(new_state_y['x']), len(new_state_y['y']))

        # printing to show process
        print("New y state is: ")
        print(new_state_y)   

        # call function to check if state is new
        check_if_new_state(state_id_y, new_state_y, seen_states, new_key, entries, x, y)

def update_state(prefix, new_prefix, next_char, x, y, seen_states, entries):
    """
    Updates either 1 or 2 new states based on if the character passed matches the expected characters for the stored x or y strings in the state being examined.

    States passed to this function will look like:
    state = {
                'x': cumulative substring of repeating x strings for this specific state,
                'y': cumulative substring of repeating y strings for this specific state,
                'x_expected': character needed to continue repeating x strings,
                'y_expected': character needed to continue repeating y strings
            }

    If the character matches x_expected, the 'x' substring will be added and that will be the new state. If the character matches y_expected, the 'y' substring will be added and that will be the new state. If the character matches both, the current state will be updated into 2 new states.

    @param prefix: A substring of the characters that have already been iterated over.
    @param new_prefix: A substring of the characters that have already been iterated over + the current character.
    @param next_char: A character {0, 1} that is currently being examined in the outer loop of untangle().
    @param x: A string representing 1 of the signals in the interweaving.
    @param y: A string representing the other signal in the interweaving.
    @param seen_states: A set storing the substrings and states that have been seen already. Stored in the format: (prefix, chars delegated to x, chars delegated to y, length of chars delegated to x, length of chars delegated to y).
    @param entries: A dictionary storing the states for each prefix. For each prefix, there is a list of states associated with it.
    @return: boolean True or False based on what the calls to check_if_new_state return.

    """ 

    # only update prefixes that exist already
    # new prefix is prefix + current character in S
    if prefix in entries and new_prefix not in entries:

        # for each state associated with that substring
        for state in entries[prefix]:

            # printing to show process
            print("State being examined: ")
            print(state)

            # take next characters
            x_next = state['x_expected']
            print("X next is: " + x_next)
            y_next = state['y_expected']
            print("Y next is: " + y_next)

            # if next_char matches for both substrings in that state
            if x_next == next_char and y_next == next_char:

                # update the states
                updated_state_x = {
                    'x': state['x'] + next_char,
                    'y': state['y'],
                    'x_expected': x[(len(state['x']) + 1)  % len(x)],
                    'y_expected': state['y_expected']
                }
                
                # create new state ID
                state_id_x = (new_prefix, updated_state_x['x'], updated_state_x['y'], len(updated_state_x['x']), len(updated_state_x['y']))
                
                # check if new state - function will return true if interweaving has been found
                if check_if_new_state(state_id_x, updated_state_x, seen_states, new_prefix, entries, x, y):
                    return True

                # update the state
                updated_state_y = {
                    'x': state['x'],
                    'y': state['y'] + next_char,
                    'x_expected': state['x_expected'],
                    'y_expected': y[(len(state['y']) + 1)  % len(y)]
                } 
                
                # create new state ID
                state_id_y = (new_prefix, updated_state_y['x'], updated_state_y['y'], len(updated_state_y['x']), len(updated_state_y['y']))
                
                # check if new state - function will return true if interweaving has been found
                if check_if_new_state(state_id_y, updated_state_y, seen_states, new_prefix, entries, x, y):
                    return True    
                
                # printing to show process
                print("UPDATED x state is: ")
                print(updated_state_x)
                print("UPDATED y state is: ")
                print(updated_state_y)   

            # if next_char can only go to x substring of the state
            elif x_next == next_char:
                
                # update the state
                updated_state_x = {
                    'x': state['x'] + next_char,
                    'y': state['y'],
                    'x_expected': x[(len(state['x']) + 1) % len(x)],
                    'y_expected': state['y_expected']
                }

                # create new state ID
                state_id_x = (new_prefix, updated_state_x['x'], updated_state_x['y'], len(updated_state_x['x']), len(updated_state_x['y']))

                # check if new state - function will return true if interweaving has been found 
                if check_if_new_state(state_id_x, updated_state_x, seen_states, new_prefix, entries, x, y):
                    return True
                
                # printing to show process
                print("UPDATED x state is: ")
                print(updated_state_x)

            # if next_char can only go to y substring of the state
            elif y_next == next_char:

                # update the state
                updated_state_y = {
                    'x': state['x'],
                    'y': state['y'] + next_char,
                    'x_expected': state['x_expected'],
                    'y_expected': y[(len(state['y']) + 1)  % len(y)]
                } 
                
                # create new state ID
                state_id_y = (new_prefix, updated_state_y['x'], updated_state_y['y'], len(updated_state_y['x']), len(updated_state_y['y']))

                # check if new state - function will return true if interweaving has been found 
                if check_if_new_state(state_id_y, updated_state_y, seen_states, new_prefix, entries, x, y):
                    return True
                
                # printing to show process
                print("UPDATED y state is: ")
                print(updated_state_y)  

            print("\n")

    # printing to show process
    print("Entries are currently: ")
    
    for key, states in entries.items():
        print(f"{key}: {states}")

    print("\n")
    return False

def check_if_new_state(state_id, state, seen_states, new_key, entries, x, y):
    """
    Takes in a state and checks to see if it is a new state. If it is new, it then checks to see if the state has enough information to determine that it is a valid interweaving from the overall signal. If it is a solution, it returns true. If it's a new state but not a solution, it adds that state to the seen_states set and creates an entry in the entries dictionary for it.

    @param state_id: The state ID being passed to the function. The state passed has the format: (prefix, chars delegated to x, chars delegated to y, length of chars delegated to x, length of chars delegated to y).
    @param state: The actual state passed to the function.
    @param seen_states: A set storing the substrings and states that have been seen already. Stored in the format: (prefix, chars delegated to x, chars delegated to y, length of chars delegated to x, length of chars delegated to y).
    @param new_key: The string representing the prefix passed with the state.
    @param entries: A dictionary storing the states for each prefix. For each prefix, there is a list of states associated with it.
    @param x: A string representing 1 of the signals in the interweaving.
    @param y: A string representing the other signal in the interweaving.
    @return: boolean True or False based on if the passed state is enough to determine that there is an interweaving.

    """ 
    # if the state ID is unique
    if state_id not in seen_states:
        
        # solution check based on lengths of substrings
        # returns true if valid interweaving found
        if state_id[3] == len(x) and state_id[4] == len(y):
            return True
        # if the substrings are too short to be a solution, add them to the states that have been seen
        else:
            seen_states.add(state_id)

            # printing to show process
            # print("Seen States is: ")
            # print(seen_states)

            # if the key is unique, add to dictionary
            if new_key not in entries:
                entries[new_key] = []

            # add that state to the list for the key
            entries[new_key].append(state)

            # if no solution found at that state
            return False


def untangle(S, x, y, entries, counter):
    """
    Takes in a signal S, signal x, and signal y, as binary strings and determines if S contains an interweaving of x and y. The function iterates over each character in S, and, for each character, iterates over the substrings from the beginning of S up to the current character.

    @param S: The overall input singal string to be analyzed.
    @param x: A string representing 1 of the signals in the interweaving.
    @param y: A string representing the other signal in the interweaving.
    @param entries: A dictionary storing the states for each prefix. For each prefix, there is a list of states associated with it.
    @param counter: A counter for analysis purposes.
    @return: boolean True or False based on if update_state calls return true.

    """ 

    # get lengths of signals
    length_x = len(x)
    print("Length of x is: " + str(length_x))
    length_y = len(y)
    print("Length of y is: " + str(length_y))

    # set to store unique states for memoization
    seen_states = set()

    # go through each character in the signal string
    for i in range(len(S)):

        # counter to show process
        counter["count"] += 1

        # store current character
        next_char = S[i]
        print("Character in outer for loop: " + next_char + " at position " + str(i) + " in S.")

        # determine where to stop starting new possible substrings
        total_length = length_x + length_y
        stopping_point = len(S) - total_length
        print("Total length is: " + str(total_length))
        
        # if the interweaving can still start at current character
        if i <= stopping_point:
            # create new starting state for beginning of interweaving
            new_state(next_char, x, y, seen_states, entries) 

        # inner loop to consider substrings from beginning of S to current character in S. j decreases from i-1 to 0
        for j in range(i-1, -1, -1):

            # count to show process
            counter["count"] += 1  

            # get the prefix that might already exist in entries
            prefix = S[j:i]
            print("\n")
            print("Inner loop prefix is: " + prefix)

            # every prefix plus the new character
            new_prefix = S[j:i+1]
            print("New Prefix is: " + new_prefix)

            # check if update_state found valid solution from check_if_new_state
            if update_state(prefix, new_prefix, next_char, x, y, seen_states, entries):
                return True
      
    return False

def get_string(prompt):
    """
    Prompts the user for input based on the prompt passed to the function. It then checks to see if the input only contains 0s and 1s. If the input is invalid, it will keep prompting for input.

    @param prompt: The message to display before taking input.

    """

    # get valid input string
    while True:
        string = input(prompt).strip()

        # test if string only has binary characters
        if string and all(ch in "01" for ch in string):
            return string
        else:
            print("Invalid input. Enter a valid binary string (only 1s and 0s)")
   
def main():

    # map for storing states
    entries= {}
    counter = {'count': 0}
   
    # prompts for user
    S = get_string("Enter the entire signal string: ")
    x = get_string("Enter the code for the first ship's signal: ")
    y = get_string("Enter the code for the second ship's signal: ")
    print("\n")

    # if untangle function returns true, solution was found. Else, no solution found
    if untangle(S, x, y, entries, counter):
        print("\n\nInterweaving found.")
        print("The overall signal " + S + " contains an interweaving of " + x + " and " + y)
        print(f"States examined = {counter['count']}\n")
    else:
        print("\n\nNo interweaving found.")
        print("The overall signal " + S + " does not contain an interweaving of " + x + " and " + y)
        print(f"States examined = {counter['count']}\n")        

# run main script
if __name__ == "__main__":
    main()