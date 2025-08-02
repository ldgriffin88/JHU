LGriffinLab4 Readme

To Compile: 
1) Be in the directory that has the JAVA files
2) "javac LinkedList.java Node.java Lab4.java"

To Run:
1) Be in the directory that holds the LGriffinLab4 Directory
2) "java LGriffinLab4.src.Lab4 "Input file folder absolute path" "Output file absolute path" "Statistics file absolute path"

What is Quick Sort (From the class ZyBook):
Quick sort is a solting algorithm that repeatedly partitions the input into low and high parts (each part unsorted), and then recursively sorts each of those parts. To partition the input, quick sort chooses a pivot to divide the data into low and high parts. The pivot can be any value within the array being sorted, commonly the value of the middle array element. Once the pivot is chosen, the quick sort algorithm divides the array into two parts, referred to as the low partition and the high partition. All values in the low partition are less than or equal to the pivot value. All values in the high partition are greater than or equal to the pivot value. The values in each partition are not necessarily sorted. Values equal to the pivot may appear in either or both of the partitions.

What is Natural Merge Sort:
Natural merge sort is a variation of the traditional merge sort that makes a separate list for all of the natural runs in the input. After all of the lists are made, the natural merge combines every two lists into one merged list. To get the merged list, the algorithm compares the lowest value in each of the lists, taking the lowest one until one of the lists is empty. At that point, the sort will append the remaining non-empty list to the merged list. The merged list is added back into the array, and the sort is called recursively taking two lists and returning one, until there is only a single list left. The single list will contain the sorted data.

Quick Sort Variations Featured:
1) Select the first item of the partition as the pivot. Treat partitions of size one and two as stopping cases.
2) Same pivot selection. For a partition of size 100 or less, use an insertion sort to finish.  
3) Same pivot selection. For a partition of size 50 or less, use an insertion sort to finish.   
4) Select the median-of-three as the pivot. Treat partitions of size one and two as stopping cases.

Expected Inputs:
The expected input files should be contained in one folder that will be passed as the first argument on the command line. The expected input files must be named in a way that the file name can be read to determine the file size. For example, a file with the title "asc50.dat" will be read and a length of 50 will be returned. The program starts reading the size at the 3rd index value of the string containing the file's title. Other naming conventions will cause the program to fail. Within the input files, the integers can be separated by tabs, spaces, or all on new lines. 

Expected Outputs:
Note: The output file will only be written to for files of size 50.
Node: The stats file will be written to for every input file.
1) For each quick sort, it will show the starting array of integers
2) For each quick sort, it will show the pivot every time the partition method is called
3) For each quick sort, it will show when two numbers are swapped and what they are
4) For quick sort variations two and three, it will show when the insertion sorts start and when the insertion sort is complete
5) For each quick sort, it will show what index values the quicksort method is being recursivelly called between
6) For each merge sort, it will show every linked list that was made from the input file
7) For each merge sort, it will show what values are being inserted to the merged list
8) For each merge sort, it will show what index the merged list is being inserted back into in the main array of linked lists
9) For every sort and file, the stats file will show the name of the file that was sorted, the type of sort performed, the size of the file, the number of comparisons, and the number of swaps. These will be separated by commas and printed on a new line for each file

Files:
1) Node class - creates new nodes with data and next attributes
2) Linked List class - creates new linked lists and has functions to insert a node, delete a node, and print the list. There are pointers maintained for the head and tail of the list
3) Main class - contains code to read in the folder of input files, set up the quick sorts, set up the merge sort, do the quick sort, and do the merge sort

Process:
1) The program will check for the correct number of command line arguments (3: one input folder, one output file, and one stats file
2) The program will attempt to access and open the folder and files
3) The program will read the first file of the folder if it exists
4) The program will determine the length of the file
5) The program will read the input values into an array for the quick sort
6) The quick sort variations 1-4 will run on the file, writing the comparisons and swaps to the stats output file, before resetting the counters following each sort
7) If the file was size 50, the process of each sort, as described above, will be written to the output file.
8) The program will read the input values for the merge sort, creating an array of linked lists that represent the natural runs in the input data
9) The program will run the merge sort method
10) This process repeats until there are no more files to be read from the input file folder

Other Notes:
1) Both the implementation of the quick sort and the natural merge sort are written recursively. Due to this, the operating environment may need to have its maximum stack size increased so that the depth of recrusion does not cause a stack overflow error. 