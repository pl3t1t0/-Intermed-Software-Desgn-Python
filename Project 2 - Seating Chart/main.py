# Seating Chart Project
# This program manages a classroom seating chart, allows students to be assigned seats,
# displays the seating chart, and organizes students into teams based on their seating arrangement.

# Create a jagged 2D list representing the seating chart with varying row sizes
seats = [
    [None, None, None, None],  # First row with 4 seats
    [None, None, None, None],  # Second row with 4 seats
    [None, None, None, None, None]  # Third row with 5 seats
]

def addStudent(name, row, col):
    """
    Adds a student to the seating chart at the specified row and column.
    Ensures that the seat is within bounds and not already occupied.
    """
    if 0 <= row < len(seats) and 0 <= col < len(seats[row]):
        if seats[row][col] is None:
            seats[row][col] = name  # Assign student to the seat
        else:
            print("Seat is already occupied!")  # Prevent overwriting an occupied seat
    else:
        print("Invalid seat position!")  # Prevent invalid seat assignments

def displaySeatingChart():
    """
    Displays the seating chart in a grid format.
    Empty seats are labeled as '[Empty]'.
    """
    for row in seats:
        print("\t".join([name if name else "[Empty]" for name in row]))  # Print each row with tab spacing

def assignTeams():
    """
    Assigns students to teams based on their seat position.
    Students in the same column of seats are assigned to the same team.
    """
    max_cols = max(len(row) for row in seats)  # Find the maximum number of columns
    teams = [[] for _ in range(max_cols)]  # Create a list for each team
    
    for col in range(max_cols):  # Iterate through columns
        for row in range(len(seats)):  # Iterate through rows
            if col < len(seats[row]) and seats[row][col]:  # Ensure seat exists and is occupied
                teams[col].append(seats[row][col])  # Assign student to respective team
    
    return teams  # Return the teams list

def displayTeams():
    """
    Displays the teams and their members.
    Each team corresponds to students sitting in the same column.
    """
    teams = assignTeams()  # Get the teams list
    for i, team in enumerate(teams):  # Iterate through teams
        print(f"Team {i}: {', '.join(team) if team else '[No Members]'}")  # Print each team's members

# Example usage - Adding students to specific seats
addStudent("Alice", 0, 0)
addStudent("Bob", 0, 1)
addStudent("Charlie", 0, 2)
addStudent("David", 0, 3)
addStudent("Eve", 1, 0)
addStudent("Frank", 1, 1)
addStudent("Grace", 1, 2)
addStudent("Hannah", 1, 3)
addStudent("Ian", 2, 0)
addStudent("Jack", 2, 1)
addStudent("Kim", 2, 2)
addStudent("Liam", 2, 3)
addStudent("Mia", 2, 4)

# Display the seating chart
print("Seating Chart:")
displaySeatingChart()

# Display the assigned teams
print("\nTeams:")
displayTeams()
