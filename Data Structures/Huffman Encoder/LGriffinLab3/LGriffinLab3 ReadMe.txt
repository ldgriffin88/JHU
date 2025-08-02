LGriffinLab3 ReadMe

To Compile:
1) Be in the directory that has the JAVA files
2) "javac Node.java Lab3.java Heap.java"

To Run:
1) Be in the directory that holds the LGriffinLab3 Directory
2) "java LGriffinLab3.src.Lab3 "Frequency table absolute path" "Clear text absolute path" "Encoded text absolute path" "Output file absolute path"

What is Huffman Encoding:
Huffman encoding is a compression/encryption method that assigns a binary code to every character being used. The codes are based on the frequency of the respective character in a specified text. Characters used more frequenbtly will have a shorter code than characters that rarely appear. The encoding is executed by building a Huffman Tree made up of simple and complex nodes. Simple nodes represent specific characters and are leaves, while complex nodes are used to implement priority. The code for a letter can be found by followign the nodes down to the leaf it represents. Going left adds a zero to the code, while going right adds a 1 to the code. For optimal compression, the frequency list should be based on the exact image, text, etc. that is to be encoded. The entity on the receiving end must also have the frequency table in order to decode a Huffman encoded message, file, etc.

LGriffinLab3 Program:
The lab3 program can be executed on the command line by enterinng the paths of 3 input files and 1 output file. The 3 input files, in this order, shall be: freqeuncy table, clear text to encode, encoded text to decode.

Expected Inputs:
1) The frequency table should have a new entry on each line, starting on the first line in the file. On each line, the letter should come first, followed by a space, a colon (or another separator), another space, and then the frequency as a number. A valid line would be as follows: A - 19. A-19, A -19, and A- 19 are all invalid. The program reads the frequency starting at the 5th character in the string.
2) The clear text file should have a different statement, sentence, etc. on each line. The program will ignore punctuation and any characters that were not added from the frequency table. This includes spaces and punctuation.
3) The encoded text file should have a different code on each line. The program will output the corresponding characters without any spaces.

Expected Outputs:
The single output file will show all of the following:
1) The Huffman tree printed using a preorder traversal.
2) Each character and its corresponding code. These are printed as the tree is traversed from left to right.
3) Each clear text statement followed by the same statement encoded
4) Each encoded statement followed by the same statement decoded.

Files:
1) Node class - creates new nodes with data, priority, left child, and right child attributes.
2) Main class - contains the code to read the frequency table, calls the heap class to make the Huffman tree, calls the heap class to print the tree, calls heap class to print the codes for each letter, reads both clear text and encoded files, and calls heap class to return and print the decoded statements and encoded statements.
3) Heap class - creates a priority queue using an array. There are methods to remove a node, insert a node, print the tree, print the Huffman codes, merge two nodes, print the array, get the code from a letter, and get the letter from a code.

Process:
1) The program will check for the correct number of comnmand line arguments (4: 3 input and 1 output file as described above).
2) The program will attempt to open all files.
3) The program will read the first line of the first file if it exists.
4) A new Heap object is created
5) Each letter and frequency pair is read from the frequency table and added as a node to the heap serving as a priority queue.
6) All of the nodes are merged into one node by removing the two highest priority, merging them together, and inserting back into the heap.
7) The resulting node contains the entire Huffman Tree. It is printed to the output file.
8) The letter codes are printed using the printCodes method in the Heap class. The method traverses the tree recursively, writing the code for each node and writing to the output file when it reaches a leaf.
9) The clear text from the second input file is read line by line. Each line is written to the output file before it is encoded.
10) For each letter, the code is found using the getLetterCode method in the Heap class and written to the output file.
11) The encoded text from the third input file is read line by line. Each line is written to the output file before it is encoded.
12) The first number of the code is read, and the next number is added until the getLetter method finds a leaf that matches the code. Essentially, the code grows until it is matched to a leaf, at which point it is reset.
13) The input readers and output writer are closed.

Other Notes:
1) In the Heap class, the indeces in the array are treated as the tree form of an array. For each index, the parent is located at index i/2, the left child is located at index 2*i, and the right child is located at index 2*i+1. The remove method removes the root node of the tree, which is the node with the highest priority. In this case, the highest priority is the lowest frequency. 
2) If there is a tie between the prioirty value of two nodes, simple nodes are higher priority than complex nodes, alphabetical order rules priority for simple nodes, and, if two nodes are complex, the node with the lowest alphanumeric character will take priority. For example, "A" takes priority over "B", "B" takes priority over "AB", and "AB" takes priority over "CD".
