#nandhini sri V(192521344)
"""
EXAM TIMETABLING USING GRAPH COLORING


Problem:

Schedule exams so that:
1. No student has two exams at the same time.
2. Adjacent subjects (conflicting subjects) must
   receive different time slots.
3. Rooms and slots are efficiently utilized.

Technique Used:
Graph Coloring + Backtracking

Complexity:

Let:
n = Number of subjects
m = Number of available time slots (colors)

Worst Case Time Complexity:
O(m^n)

Reason:
Each subject may try all m colors.

Space Complexity:
O(n)

Reason:
Recursion depth is equal to number of vertices.

"""

# --------------------------------------------------
# Graph Representation
# --------------------------------------------------
# Subjects are vertices
# Edges represent conflicts

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# Available time slots (colors)
colors = ["T1", "T2", "T3"]

# Stores assigned colors
color_assignment = {}


# ---------------------------------------------------
# Check whether assigning a color is safe
# ---------------------------------------------------
def is_safe(subject, color):

    # Check all neighboring subjects
    for neighbour in graph[subject]:

        # If neighbor already has same color,
        # then conflict occurs
        if neighbour in color_assignment and color_assignment[neighbour] == color:
            return False

    return True


# ---------------------------------------------------
# Backtracking Function
# ---------------------------------------------------
def graph_coloring(subjects, index):

    # Base Case
    if index == len(subjects):
        return True

    # Current subject
    current_subject = subjects[index]

    # Try every time slot
    for color in colors:

        # ------------------------------------------------
        # PRUNING CONDITION
        # ------------------------------------------------
        # Assign only if no neighboring subject
        # has same color
        if is_safe(current_subject, color):

            # Assign color
            color_assignment[current_subject] = color

            # Recursive call for next subject
            if graph_coloring(subjects, index + 1):
                return True

            # ------------------------------------------
            # BACKTRACKING
            # ------------------------------------------
            # Remove color if future assignment fails
            del color_assignment[current_subject]

    return False


# ---------------------------------------------------
# Main Program
# ---------------------------------------------------
subjects = list(graph.keys())

if graph_coloring(subjects, 0):

    print("Conflict-Free Exam Schedule\n")

    for subject in color_assignment:
        print(subject, "->", color_assignment[subject])

else:
    print("No valid timetable exists.")
