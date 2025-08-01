"""
map_color.py

Starter for the Map Coloring CSP (Assignment 2).

Students must complete the `solveCSP` function using backtracking search
to assign colors to regions such that no adjacent regions share the same color.

Refer to Chapter 6 (Section 6.1.1) of *Artificial Intelligence: A Modern Approach* (3rd Edition)
for background on constraint satisfaction and the map coloring problem.

Optional enhancements:
- MRV (Minimum Remaining Values)
- LCV (Least Constraining Value)
- Forward Checking / AC-3 (constraint propagation)
"""

def solveCSP(map_data):
    """
    Solves the map-coloring CSP via backtracking search.

    Args:
        map_data (dict): Contains:
            - 'regions': list of region names (variables)
            - 'neighbors': dict mapping each region to its adjacent regions
            - 'colors': list of color names (domains)
    Returns:
        dict or None: Mapping region->color if solution found; otherwise None.
    """
    regions = map_data['regions']
    neighbors = map_data['neighbors']
    colors = map_data['colors']

    # Initialize assignment as an empty dictionary
    assignment = {}

    def is_consistent(region, color):
        """
        Return True if assigning `color` to `region` doesn't violate constraints
        (i.e., none of its neighbors have the same color).
        """
        for neighbor in neighbors.get(region, []):
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True

    def backtrack():
        """
        Performs recursive backtracking search.

        TODO:
        1. If all regions are assigned, return the assignment.
        2. Select an unassigned region (Optionally implement MRV here).
        3. For each color in the color list (Optionally use LCV ordering):
            a. Check if the color is consistent using `is_consistent`.
            b. If valid, assign it and recursively backtrack.
            c. If recursion succeeds, return the assignment.
            d. Otherwise, backtrack (undo assignment).
        4. If no color leads to a solution, return None.

        Optional:
        - Implement MRV for smarter region selection.
        - Use forward checking or AC-3 to reduce domains after assignment.
        """
        # TODO 1: Check if assignment is complete
        # if assignment contains all regions
        if len(assignment) == len(regions):
            return assignment

        # TODO 2: Select the next unassigned region (MRV heuristic optional)

        # initialize
        next_unassigned = None

        # go through the regions and see if it is assigned
        for region in regions:
            if region not in assignment:
                next_unassigned = region
                break

        # TODO 3: Iterate over colors (LCV ordering optional)
        # go through colors and test consistency
        for color in colors:
            if is_consistent(next_unassigned, color):
                assignment[next_unassigned] = color
                answer = backtrack()

                if answer is not None:
                    return answer
                
                # if branch led to dead end
                del assignment[next_unassigned]

        # TODO 4: Return None if no valid assignment is found
        return None

    return backtrack()


if __name__ == "__main__":
    # Example map_data (Australia map from AIMA)
    sample_map = {
        'regions': ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T'],
        'neighbors': {
            'WA': ['NT', 'SA'],
            'NT': ['WA', 'SA', 'Q'],
            'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
            'Q': ['NT', 'SA', 'NSW'],
            'NSW': ['SA', 'Q', 'V'],
            'V': ['SA', 'NSW'],
            'T': []
        },
        'colors': ['Red', 'Green', 'Blue']
    }

    # This is just for testing; you can remove or modify as needed
    solution = solveCSP(sample_map)
    if solution:
        print("Solution found:")
        for region, color in solution.items():
            print(f"{region} -> {color}")
    else:
        print("No solution found.")
