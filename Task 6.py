# University Campus Map Coloring using CSP

# Available colors
colors = ["Red", "Green", "Blue", "Yellow"]

# Variables (zones)
zones = ["A", "B", "C", "D", "E"]

# Constraints represented using adjacency list
neighbors = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E"],
    "E": ["C", "D"]
}


# Check whether assigning a color is valid
def is_valid(zone, color, assignment):

    for neighbor in neighbors[zone]:

        if neighbor in assignment:
            if assignment[neighbor] == color:
                return False

    return True


# Backtracking CSP algorithm
def backtracking(assignment):

    # If all zones are assigned
    if len(assignment) == len(zones):
        return assignment

    # Select the next unassigned zone
    for zone in zones:
        if zone not in assignment:
            break

    # Try every available color
    for color in colors:

        # Check constraints
        if is_valid(zone, color, assignment):

            # Assign color
            assignment[zone] = color

            # Recursively solve remaining zones
            result = backtracking(assignment)

            if result is not None:
                return result

            # Backtrack
            del assignment[zone]

    return None


# Solve the CSP
solution = backtracking({})


# Display solution
if solution:
    print("Valid Campus Map Coloring:")
    
    for zone in zones:
        print(zone, "->", solution[zone])

else:
    print("No valid coloring found.")



OUTPUT

Valid Campus Map Coloring:
A -> Red
B -> Green
C -> Blue
D -> Red
E -> Green
