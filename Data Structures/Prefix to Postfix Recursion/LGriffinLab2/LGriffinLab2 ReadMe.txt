LGriffinLab2 ReadMe

To Compile: 
1) Be in the directory that has the JAVA files
2) "javac Stack.java Lab2.java"

To Run:
1) Be in the directory that holds the LGriffinLab2 directory.
2) "java LGriffinLab2.src.Lab2 "Input file abosulute path" "Output file absolute path"

What are Prefix and Postfix Expressions: 
A prefix expression is a math expression that consists of only operators and operands. There are no parentheses or other delimiters. In a prefix expression, the operator comes before the operand. For example, +AB represents A+B. A postfix expression is the opposite. The operators come after the operands. A+B would be represented as AB+. Prefix and Postfix expressions are more efficient in code because no delimiters have to be dealt with. Lastly, an infix expression is an expression that is ordered normally (A+B).

LGriffinLab2 Program:
The Lab2 program can be executed on the command line by entering the input file name followed by the output file name

Expected Inputs:
The program is expecting a file with a different, valid prefix expression on each line.

Expected Outputs:
The program will output the prefix expression, the equivalent infix expression, and the equivalent postfix expression, on a new line, for each valid line/expression it reads in. If the line/expression is invalid, the program will output a message saying that the line did not contain a valid expression.

Files:
There are two classes, a Node class and a Lab class. The Node class stores data and references the left and right child nodes of the current node. The references allow the nodes to be arranged in a tree-like structure. The Lab class consists of the main method and separate methods to help execution. The characterType method converts a character to its ascii value for evaluation and returns an integer. The checkStatement method traverses the node structure recursively looking for invalid nodes and returns a boolean value. The buildTree method checks for errors in the expression and recursively calls itself to build out a structure of nodes based on the expression. Separate methods to recursively print the three different types of expressions (prefix, infix, and postfix) are also available.

Process: 
1) The program will check for the correct number of comnmand line arguments (2: input and output file).
2) The program will attempt to open both files
3) The program will read the first character of the first line if it exists.
4) The program will call the buildTree method and recursively build a structure of nodes based on the expression. Blank spaces will be ignored. If an invalid character is found, the node associated with that character will contain the data "Invalid" and the rest of the tree will be built. The base cases of the method are a letter (operand), an invalid character, or a new line.
5) The program will determine the validity of the statement by checking for extra characters on the line, an "Invalid" node, and looking at the number of nodes versus leaves.
6) If the statement is determined to be valid, the three different forms of the expression will be printed to the output file. 
7) The input reader and output writer will be closed.

Other Requirements/Notes: 
1) This program was written based on an input file that ahs a carriage return and ne line chracter at the end of each line. Using an input file with different characters at the end of each line may produce varying resutls.
2) Errors that occur in the program will force the program to exit, and a statement telling where the progrma failed will be printed.