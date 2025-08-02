README

Created with: python 3.13.0

Files in this project:

- "Prog2.py" (main file that will run)
- "Trace Runs" is a folder that contains files representing different runs of the file Prog2.py
- "LoganGriffin_ProgrammingAssignment2.pdf" contains the project write up and analysis
- "prog2_SP25" is the assignment document

Problem Statement:
You are consulting for a group of people (who would prefer not to be mentioned here by name) whose job consists of monitoring and analyzing electronic signals coming from ships in the Atlantic ocean. They want a fast algorithm for a basic primitive that arises frequently: “untangling” a superposition of two known signals. Specifically, they are picturing a situation in which each of two ships is emitting a short sequence of 0s and 1s over and over, and they want to make sure that the signal they are hearing is simply an interweaving of these two emissions, with nothing extra added in. The short sequence emitted by each ship is known to the ship and to you, the receiver. Given a string x consisting of 0s and 1s, we write xk to denote k copies of x concatenated together. We say that string x′ is a repetition of x if it is a prefix of xk for some number k. So, x′ = 10110110110 is a repetition of x =101. We say that a string s is an interweaving of x and y if its symbols can be partitioned into two (not necessarily contiguous) subsequence s′ and s′′ so that s′ is a repetition of x and s′′ is a repetition of y. Each symbol in s must belong to exactly one of s′ of s′′. For example, if x = 101 and y = 0, then s = 100010101 is an interweaving of x and y since characters 1,2,5,7,8, and 9 form 101101– a repetition of x– and the remaining characters 3,4,6 form 000– a repetition of y. In terms of our application, x and y are the repeating sequences from the two ships, and s is the signal we are receiving. We want to make sure s “unravels” into simple repetitions of x and y. You want a “fast algorithm for ...‘untangling’ a superposition of two known signals”, x and y. You receive some set of symbols s. You do not know if the signal you receive has its first symbol in x, y, or a symbol that is extra and added in. You need to use your knowledge of x and y and the received signal s to determine if s consists only of valid interwoven symbols from x and y. That may require your solution to discard some symbols at the beginning or end of s to get to at least a full match of x and a full match of y. The received signal could be too short to do this. If you can’t determine that the signal is an interweaving of x and y, either because s is not long enough to do so or because s contains symbols not in x or y then you cannot decide that s is an interweaving of x and y.

Description:
This algorithm addresses the problem statement above. The signal S, signal x, and signal y are input by the user. The algorithm then takes the signal S and determines if it contains an interweaving of x and y. The general method for determining this is as follows: iterate over the length of S. For each character in S, consider the interweaving starts at that character by creating a new "state" to keep track of (states are stored as shown below). For each character iterated over in S, the algorithm also updates the stored states corresponding to the substrings from the beginning of S to the current character. For example, say S = 101101. When looking at the 3rd 1 occurrence, a nested for loop will updates the states for the substrings 11, 011, and 1011. There is also a dictionary of entries that are stored by substring with a list of states attached to each substring. That way, if the substring has already been seen once, the algorithm will not update the states leading to that substring, as it already knows them. There is also a simple check during every state update to see if the 'x' and 'y' cumulative substrings stored in the state contain a complete signal of each, respectively. If they do, the program ends as it can be said S contains an interweaving of x and y.


State format:
    state = {
                'x': cumulative substring of repeating x strings for this specific state,
                'y': cumulative substring of repeating y strings for this specific state,
                'x_expected': character needed to continue repeating x strings,
                'y_expected': character needed to continue repeating y strings
            }

To Run:
1) Open the command line/terminal
2) Be in the directory with the Griffin_Assignment2 folder
3) Ensure python is installed (python --version should return version)
4) Run the following line: "python Prog2.py"
5) Follow the prompts to enter the total signal S, signal x, and signal y.

Functions in Prog2.py:
1) new_state(next_char, x, y, seen_states, entries)
	Creates either 1 or 2 new states based on if the character passed matches the first 	character in the string x, string y, or both. This function calls the check_if_new_state 	function.
2) update_state(prefix, new_prefix, next_char, x, y, seen_states, entries)
	Updates either 1 or 2 new states based on if the character passed matches the expected 	characters for the stored x or y strings in the state being examined. If the character 	matches x_expected, the 'x' substring will be added and that will be the new state. If 	the character matches y_expected, the 'y' substring will be added and that will be the 	new state. If the character matches both, the current state will be updated into 2 new 	states.
3) check_if_new_state(state_id, state, seen_states, new_key, entries, x, y)
	Takes in a state and checks to see if it is a new state. If it is new, it then checks to 	see if the state has enough information to determine that it is a valid interweaving 	from the overall signal. If it is a solution, it returns true. If it's a new state but 	not a solution, it adds that state to the seen_states set and creates an entry in the 	entries dictionary for it.
4) untangle(S, x, y, entries, counter)
	Takes in a signal S, signal x, and signal y, as binary strings and determines if S 	contains an interweaving of x and y. The function iterates over each character in S, 	and, for each character, iterates over the substrings from the beginning of S up to the 	current character.
5) get_string(prompt)
	Prompts the user for input based on the prompt passed to the function. It then checks to 	see if the input only contains 0s and 1s. If the input is invalid, it will keep 	prompting for input.
6) main()
	Contains prompts for S, x, and y, calls to untangle, and print messages for the final 	output.

Input:
This program depends on user input. The user is prompted to enter the total signal S, signal x, and signal y.

Output: 
The program will include the input strings in a sentence that states whether an interweaving was found.

