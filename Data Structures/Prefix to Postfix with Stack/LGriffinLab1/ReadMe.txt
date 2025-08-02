LGriffinLab1 ReadMe

To Compile: 
1) Be in the directory that has the JAVA files
2) "javac Stack.java Lab1.java"

To Run:
1) Be in the directory that holds the LGriffinLab1 directory.
2) "java LGriffinLab1.src.Lab1 "Input file abosulute path" "Output file absolute path"

What are Prefix and Postfix Expressions: 
A prefix expression is a math expression that consists of only operators and operands. There are no parentheses or other delimiters. In a prefix expression, the operator comes before the operand. For example, +AB represents A+B. A postfix expression is the opposite. The operators come after the operands. A+B would be represented as AB+. Prefix and Postfix expressions are more efficient in code because no delimiters have to be dealt with. 

LGriffinLab1 Program:
The Lab1 program can be executed on the command line by entering the input file name followed by the output file name

Expected Inputs:
The program is expecting a file with a different, valid prefix expression on each line.

Expected Outputs:
The program will output the equivalent postfix expression, on a new line, for each line/expression it reads in.

Files:
There are two classes, a Stack class and a Lab class. The Stack class was written using arrays and is a limited version of the java Stack class. There are methods to push, pop, check if empty, and peek. There is also a method to print the stack that can be used for debugging/testing purposes. The Stack class uses strings to populate the arrays. The Lab class consists of the main method and a separate method to determime the type of character. The method for determining type of character converts to ascii value for evaluation.

Process: 
1) The program will check for the correct number of comnmand line arguments (2: input and output file).
2) The program will attempt to open both files
3) The program will read the first line, if it exists.
4) Each valid character will be added to a stack. In this step, any blank spaces will be ignored. If an invalid character is found, the program will mark that line as invalid and will print to the output file saying that is the case.
5) If the statement contained only valid characters, the program will iterate through the stack, assigning the terms to another stack representing the expression. if a letter is next, it will be passed directly to the stack. If an operator is next, the expression stack will be popped twice, and a term containing both items and the operator will be pushed back to the stack. 
6) After the initial stack from the line that was read in is emptty, the program will write the expression to the output file. 

Other Notes: 
1) A valid prefix expression should contain one less operator than operand. The program will keep counts for each and determine if the statement is invalid after the prefix stack is empty. 
2) Any errors that are encountered will result in "The expression on this line was invalid" being written to the output file on the line corresponding to the line number that was read in.
