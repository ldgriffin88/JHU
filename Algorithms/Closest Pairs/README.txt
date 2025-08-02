README

Crated with: python 3.13.0

Files in this project:
- "Closest_Pairs.py" (main file that will run)
- "Red-Black_Tree.py" (implements red-black tree)
- "Data Points for Analysis - n100_m1-4950.txt" contains testing data when the program was run with 100 random points for all valid number of pairs
- "Trace Runs" is a folder containing test data. The naming of the files in the folder indicate the number of points and the value of m that was used. 
- "LoganGriffin_ProgrammingAssignment1.pdf" contains project write up and analysis.
- "prog1_SP25" is the assignment document
 
Description:
This algorithm finds the closest m pairs of points from a set, P, of points in a 2-D plane. The number of points, bounds for points, and number of pairs to return is determined by the user through prompts. The general method for returning the pairs is as follows: 1) Sort the set by x-value. 2) Recursively split set P in half at the median of the set. 3) When there is less than 4 elements in a set, brute force compare the distances and add them to a red-black tree. 4) After this is done for two sides of a set, do a vertical strip test to compare points that may be closer to each other but on opposing sides of the median value. If there are already an adequate number of pairs found, use the largest distance stored in the tree and create those bounds around the median. Find distances between points from the lower side of the median with points on the upper side of the median as long as they are in the bounds. For each future distance found, compare it to the largest distance stored in the tree. If it is smaller, delete the largest distance in the tree and insert the new distance that was just found. If there is not an adequate number of pairs so far, keep brute force comparing until there is enough pairs. At the end of the recursive calls, there will be a tree with m nodes, each representing a distance and two points.

To Run:
1) Open command line/terminal
2) Be in the Directory with the Griffin_Assignment1 folder
3) Ensure python is installed (python --version should return version)
4) Run the following line: "python Closest_Pairs.py"
5) Enter integer values for the prompts

Functions in Closest_Pairs.py
1) merge(A, p, q, r) - merges subarrays as part of merge sort. It merges the two subarrays by the x-value of a tuple in ascending order.
2) merge_sort(A, p, r) - sorts tuples by their x-value in ascending order.
3) three_or_less(P, m, rbt, counter) - used when the input set P consists of three or less points. Calculates the distances between all the points in the set and inserts them into an instance of a red-black tree
4) distance(p1, p2, counter) - calculates the Euclidean distance between a pair of points (x1, y1), (x2, y2)
5) split_median(P) - splits a set into two subsets at the median and returns the two subsets. The median is included in the subset that makes up the upper half of values.
6) compare_points(P, m, rbt, counter) - finds the distances between pairs of points and inserts them into an instance of a red-black tree.
7) strip_test(lower, upper, rbt, m, counter) - compares points from two subarrays across a median value. The elements in lower and upper are tuples representing ordered pairs. They are both sorted by x-value, with all values in upper being greater than all values in lower. If the red-black tree (rbt) storing the distances already has m values, this function uses the max distance from the tree to define bounds around the median from median - max to median + max. If rbt does not have m values, the function compares all points in lower to all points in upper. When the function calculates the distance between two points, it either adds it to rbt if the size is less than m, or compares it to the max distance in the tree if rbt size is already m. if rbt size is m and the new distance is less than the max distance, the function deletes the max element and replaces it with the new distance and points.
8) pairs(P, m, rbt, counter) - recursive function to calculate the closest m pairs of points by Euclidean distance from set of points P.

Functions in Red_Black_Tree:
Includes standard functions minimum, maximum, insert, insert-fixup, delete, delete-fixup, transplant, left_rotate, right_rotate, and print_tree.

Input: 
This program depends on user input. The user is prompted to enter integer values for the number of points, the lower bounds for x and y, and the number of pairs to return. After this, the program will randomly generate points within the bounds.

Output:
The program will print the input values that were generated, followed by the closest m distances and which points the distances were obtained from. There is also a comparison counter that will be printed at the end.