"""
Filename: Closest_Pairs.py
Author: Logan Griffin
Created 3/3/25
Description: This file takes a set of points P and an integer m and returns
the m closest pairs of points within the set P.
"""

import math
import sys
import random
from Red_Black_Tree import RBT

def merge(A, p, q, r):
    """
    This merges subarrays as part of merge sort. It merges the two subarrays by the x-value of a tuple in ascending order.

    @param A: The array to be sorted.
    @param p: An integer representing the beginning of lower subarray.
    @param q: The integer the array will be split at.
    @param r: The integer representing the end of the upper subarray.
    
    """
    nL = q-p+1  # length of A[p:q]
    nR = r-q    # length of A[q+1:r]

    # new subarrays
    L = [0] * nL
    R = [0] * nR

    # copy A[p:q] into L[0:nL-1]
    for i in range(nL):
        L[i] = A[p + i]

    # copy A[q+1:r] into R[0:nR-1]
    for j in range(nR):
        R[j] = A[q + j + 1]
        
    i = 0   # i indexes the smalles remaining element in L
    j = 0   # j indedes the smalles remaining element in R
    k = p   # k indexes the location in A to fill

    # as long as each of the arrays L and R contains an unmerged element,
    # copy the smallest element back into A[p:r]
    while i < nL and j < nR:
        if L[i][0] <= R[j][0]:
            A[k] = L[i]
            i += 1
        else: 
            A[k] = R[j]
            j += 1
        k += 1
    
    # having gone through one of L and R entirely, copy the remainder
    # of the other to the end of A[p:r]
    while i < nL:
        A[k] = L[i]
        i += 1
        k += 1

    while j < nR:
        A[k] = R[j]
        j += 1
        k += 1
   
def merge_sort(A, p, r):
    """
    Merge sort algorithm to sort tuples by their x-value in ascending order.

    @param A: The array to be sorted.
    @param p: The starting index of the sort.
    @param r: The ending index of the sort.
    @return: The sorted array.

    """
    # if zero or one element
    if p >= r:
        return A
    
    # midpoint of A[p:r]
    q = (p+r) // 2   

    merge_sort(A, p, q)    # recursively sort A[p:q]
    merge_sort(A, q + 1, r)     # recrusively sort A[q+1:r]

    # merge A[p:q] and A[q+1:r] into A[p:r]
    merge(A, p, q, r)

def three_or_less(P, m, rbt, counter):
    """
    Called when the input consists of three or less points to calculate the distances between all of the points in the set.

    @param P: A set of tuples representing points with x and y-coordinate.
    @param m: The number of pairs the function should return.
    @param rbt: A red-black tree for storing the distances and points.
    @param counter: A dictionary value to hold the count for number of comparisons.
    @return: Does not return anything, only modifies rbt.

    """
    num_points = len(P)
    
    # handle if only a single point
    if num_points == 1:
        return "There is only one point in the input set."
    
    # handle if only 2 points
    if num_points == 2:
        d = distance(P[0], P[1], counter)
        rbt.insert(d, P[0],P[1])
        return 
    
    # handle if only 3 points
    if num_points == 3:
        dist1_2 = distance(P[0], P[1], counter)
        rbt.insert(dist1_2, P[0], P[1])

        dist1_3 = distance(P[0], P[2], counter)
        rbt.insert(dist1_3, P[0], P[2])

        dist2_3 = distance(P[1], P[2], counter)
        rbt.insert(dist2_3, P[1], P[2])

        # remove nodes until size of rbt = m
        while rbt.size > m:
            rbt.delete(rbt.maximum(rbt.root))
        
        return
    
def distance(p1, p2, counter):
    """
    Calculates the euclidean distance between a pair of points

    @param p1: A tuple representing the first point. 
    @param p2: A tuple representing the second point.
    @param counter: A dictionary value to hold the count for number of comparisons.
    @return: The distance between them as a float.

    """
    counter["count"] += 1
    print(f"Finding distance between: {p1} and {p2}")

    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def split_median(P):
    """
    Splits an array into two subarrays at the median. The median value is included in the upper half.

    @param P: The set of tuples to be split by x-value.
    @return lower_half: Set from beginning of P to median-1.
    @retrun upper_half: Set from median to end of P.

    """        
    # integer division to find median position
    median_index = len(P) // 2  
    
    # split into lower and upper halves
    lower_half = P[:median_index]  # elements before median
    upper_half = P[median_index:]  # median and elements after

    print("\nSet has been split into lower half:")
    for point in lower_half:
        print(f"({point[0]:.4f}, {point[1]:.4f})")
    print("\nand upper half:")
    for point in upper_half:
        print(f"({point[0]:.4f}, {point[1]:.4f})")
    print("\n")
    return lower_half, upper_half

def compare_points(P, m, rbt, counter):
    """
    Finds the distances between pairs of points and inserts them into a red-black tree.

    @param P: The set of points as an array.
    @param m: An integer representing the number of pairs to return.
    @param rbt: A red-black tree to store the distances and the pair of points.
    @param counter: A dictionary value to hold the count for number of comparisons.
    @return: Does not return anything. Only modifies rbt.

    """
    num_points = len(P)

    # compare unique pairs of points, find distance, and insert into rbt
    for i in range(num_points):
        for j in range(i + 1, num_points):
            d = distance(P[i], P[j], counter)

            # keeps size of rbt at m elements
            if rbt.size < m:
                # add entry if there are less than m
                rbt.insert(d, P[i], P[j])
            else:
                # rbt is size m, so check against the largest distance
                max_element = rbt.maximum(rbt.root)
                counter["count"] += 1

                # insert if the distance is less than max distance in tree
                if d < max_element.dist:
                    print(f"\nReplacing {max_element.dist:.4f} with {d}, {P[i]}, {P[j]}")
                    rbt.delete(max_element)
                    rbt.insert(d, P[i],P[j])

def strip_test(lower, upper, rbt, m, counter):
    """
    Compares points from two subarrays across a median value.

    The elements in lower and upper are tuples representing ordered pairs. They are both sorted by x-value, with all values in upper being greater than all values in lower. If the red-black tree (rbt) storing the distances already has m values, this function uses the max distance from the tree to define bounds around the median from median - max to median + max. If rbt does not have m values, the function compares all points in lower to all points in upper. When the function calculates the distacne between two points, it either adds it to rbt if the size is less than m, or compares it to the max distance in the tree if rbt size is already m. if rbt size is m and the new distance is less than the max distance, the function deletes the max element and replaces it with the new distance and points.

    @param lower: A subarray of tuples representing ordered pairs.
    @param upper: A subarray of tuples representing ordered pairs.
    @param rbt: A red-black tree storing points and the distances between them.
    @param m: An integer representing the number of pairs to store in the rbt and ultimately return by the program.
    @param counter: A dictionary value to hold the count for number of comparisons.
    @return: Does not return anything. Only modifies rbt.

    """
    
    # median is first element in upper
    median = upper[0][0]

    # if already found enough points, only need to look for 
    # distances that are less than the max distance that has
    # already been found away from the median
    if rbt.size == m:
        largest_distance = rbt.maximum(rbt.root).dist

        # set bounds for strip
        lower_bound = median - largest_distance
        upper_bound = median + largest_distance

        print(f"\nThe tree is now size m and the strip test has been called with bounds: {lower_bound} to {upper_bound}\n")
        # obtain points within bounds
        # finds starting index in lower for points that should be included and returns
        # length of lower if no points qualify
        starting_point = next((i for i, p in enumerate(lower) if p[0] >= lower_bound), len(lower))

        # find the ending index in upper (points in upper with x > upper_bound)
        ending_point = next((i for i, p in enumerate(upper) if p[0] > upper_bound), len(upper))
        
        points_to_compare_from_lower = lower[starting_point:]
        points_to_compare_from_upper = upper[:ending_point]

        # compare across median
        for p1 in points_to_compare_from_lower:
            for p2 in points_to_compare_from_upper:

                d = distance(p1, p2, counter)

                # check if new distance is less than max distance in tree
                max_element = rbt.maximum(rbt.root)
                counter["count"] += 1

                # if new distance is less, delete max element and insert new
                if d < max_element.dist:
                    print(f"\nReplacing {max_element.dist:.4f} with {d}, {p1}, {p2}")
                    rbt.delete(max_element)
                    rbt.insert(d, p1, p2) 

    else:
        # to compare across the median value when size is less than m
        # compare only lower vs upper (not within themselves)
        for p1 in lower:
            for p2 in upper:
                
                d = distance(p1, p2, counter)

                # keeps size of heap at m elements
                if rbt.size < m:
                    # add entry if there are less than m
                    rbt.insert(d, p1, p2)
                else:
                    max_element = rbt.maximum(rbt.root)
                    counter["count"] += 1

                    if d < max_element.dist:
                        print(f"\nReplacing {max_element.dist:.4f} with {d}, {p1}, {p2}")
                        rbt.delete(max_element)
                        rbt.insert(d, p1, p2)
        
def pairs(P, m, rbt, counter):
    """
    Calculates the closest m pairs of points (by Euclidean distance) from set of points P and stores them in a red-black tree (rbt).

    @param P: The set of points as ordered pairs [(x1, y1), (x2, y2), ...].
    @param m: The number of pairs to store in rbt.
    @param rbt: Red-black tree to store the pairs of points and their distances.
    @param counter: A dictionary value to hold the count for number of comparisons.

    """
    num_points = len(P)

    # find median if 4 points or less and split into subarrays
    if num_points >= 4:
        lower, upper = split_median(P)

        # recursive calls to pairs function
        pairs(lower, m, rbt, counter)
        pairs(upper, m, rbt, counter)

        strip_test(lower, upper, rbt, m, counter)
    else:
        # brute force compare if there are less than 4 elements
        compare_points(P, m, rbt, counter)

    return

print("\nThis program generates the closest distances within a set of points. The points are randomly generated within the bounds specified by the user.\n")

# set number of points
while True:
    try:
        n = int(input("Enter an integer for how many points to generate: "))
        lowerx = int(input("Enter an integer to serve as lower x bound: "))
        upperx = int(input("Enter an integer to serve as upper x bound: "))
        lowery = int(input("Enter an integer to serve as lower y bound: "))
        uppery = int(input("Enter an integer to serve as upper y bound: "))
        m = int(input("Enter the number of distances and pairs to return: "))
        break  # exit loop if input is valid
    except ValueError:
        print("Invalid input. Please enter integers.")

# generates random points
P = [(random.uniform(lowerx, upperx), random.uniform( lowery, uppery)) for _ in range(n)]

# initialize counter
comparison_counter = {"count": 0}

print("\n**************************************")
print(f"INPUT FOR n = {len(P)} and m = {m}")
print("**************************************\n")
print("Points generated:")
for point in P:
    print(f"({point[0]:.4f}, {point[1]:.4f})")
print("\n")

# sort the points by x-value
merge_sort(P, 0, len(P) - 1)
print("The points sorted by x-value are:")
for point in P:
    print(f"({point[0]:.4f}, {point[1]:.4f})")
print("\n")

num_points = len(P)
max_pairs = (num_points * (num_points-1))/2

# new red-black tree
rbt = RBT()

# if asking for no pairs or no points in set
if m == 0 or len(P) == 0:
    print("Error: Please specify a valid value for m and make sure there are points in the input set.")
    sys.exit()

# if asking for more than n choose 2 pairs
if m > max_pairs:
    if len(P) == 1:
        print("Error: There is only one point in the input set.")
        sys.exit()
    else:
        print("Error: m exceeds the maximum number of unique pairs in the set.")
        sys.exit()
else:
    # execute to find pairs
    if len(P) < 4:
        three_or_less(P, m, rbt, comparison_counter)
    else:
        pairs(P, m, rbt, comparison_counter)

print("\n**************************************")
print("OUTPUT")
print("**************************************")
print(f"\nThe closest {m} pairs and their distances are:")
rbt.print_tree(rbt.root)
print(f"Comparisons: {comparison_counter['count']}\n")



