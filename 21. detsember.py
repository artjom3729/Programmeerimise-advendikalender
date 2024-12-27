from copy import deepcopy

# Original input grid as a multi-line string
input_str = """*4011
*4444
*4242
*4444
*4011"""


# Function to add boundaries to the grid
def add_boundaries(grid, boundary_char="#"):
    """
    Adds a boundary around the original grid to simplify neighbor checks.

    Parameters:
    - grid (list of list of str): The original grid without boundaries.
    - boundary_char (str): The character to use for the boundary.

    Returns:
    - list of list of str: The grid with added boundaries.
    """
    # Determine the width of the grid
    width = len(grid[0])

    # Create the top and bottom boundary rows
    boundary_row = [boundary_char] * (width + 2)

    # Add boundaries to each row
    bounded_grid = [boundary_row]
    for row in grid:
        bounded_grid.append([boundary_char] + row + [boundary_char])
    bounded_grid.append(boundary_row)

    return bounded_grid


# Function to parse the input grid and add boundaries
def parse_and_add_boundaries(input_str):
    """
    Parses the input string into a grid and adds boundaries.

    Parameters:
    - input_str (str): Multi-line string representing the grid.

    Returns:
    - list of list of str: The bounded grid.
    """
    # Split the input into lines and strip any leading/trailing whitespace
    lines = input_str.strip().splitlines()

    # Convert each line into a list of characters
    grid = [[char for char in line.strip()] for line in lines]

    # Add boundaries to the grid
    bounded_grid = add_boundaries(grid)

    return bounded_grid


# Function to calculate the Rose (Pink) Scenario
def rose_scenario(grid):
    """
    Calculates the minimal number of damaged rooms (Rose Scenario).

    Parameters:
    - grid (list of list of str): The bounded grid.

    Returns:
    - int: Count of damaged rooms in the Rose Scenario.
    """
    # Create a deep copy of the grid to avoid modifying the original
    rose_grid = deepcopy(grid)

    changed = True  # Flag to track if any changes occurred in an iteration

    while changed:
        changed = False  # Reset the flag at the start of each iteration
        # Iterate through the grid excluding the boundaries
        for y in range(1, len(rose_grid) - 1):
            for x in range(1, len(rose_grid[0]) - 1):
                current = rose_grid[y][x]

                if current == "*":
                    continue  # Already damaged, no action needed

                open_doors = int(current)

                # Count the number of adjacent flooded rooms
                adjacent_flooded = 0
                if rose_grid[y - 1][x] == "*":
                    adjacent_flooded += 1
                if rose_grid[y + 1][x] == "*":
                    adjacent_flooded += 1
                if rose_grid[y][x - 1] == "*":
                    adjacent_flooded += 1
                if rose_grid[y][x + 1] == "*":
                    adjacent_flooded += 1

                # Determine if the room should be flooded based on Rose Scenario rules
                # Flood the room only if the number of open doors exceeds the number of undamaged neighbors
                if open_doors > (4 - adjacent_flooded):
                    rose_grid[y][x] = "*"  # Flood the room
                    changed = True  # A change has occurred

    # Count the total number of damaged rooms
    damaged_count = sum(row.count("*") for row in rose_grid)

    return damaged_count


# Function to calculate the Black Scenario
def black_scenario(grid):
    """
    Calculates the maximal number of damaged rooms (Black Scenario).

    Parameters:
    - grid (list of list of str): The bounded grid.

    Returns:
    - int: Count of damaged rooms in the Black Scenario.
    """
    # Create a deep copy of the grid to avoid modifying the original
    black_grid = deepcopy(grid)

    changed = True  # Flag to track if any changes occurred in an iteration

    while changed:
        changed = False  # Reset the flag at the start of each iteration
        # Iterate through the grid excluding the boundaries
        for y in range(1, len(black_grid) - 1):
            for x in range(1, len(black_grid[0]) - 1):
                current = black_grid[y][x]

                if current == "*":
                    continue  # Already damaged, no action needed

                open_doors = int(current)

                # Check if there's at least one adjacent flooded room
                adjacent_flooded = False
                if black_grid[y - 1][x] == "*":
                    adjacent_flooded = True
                if black_grid[y + 1][x] == "*":
                    adjacent_flooded = True
                if black_grid[y][x - 1] == "*":
                    adjacent_flooded = True
                if black_grid[y][x + 1] == "*":
                    adjacent_flooded = True

                # Determine if the room should be flooded based on Black Scenario rules
                # Flood the room if it has at least one open door leading to a flooded room
                if adjacent_flooded and open_doors >= 1:
                    black_grid[y][x] = "*"  # Flood the room
                    changed = True  # A change has occurred

    damaged_count = sum(row.count("*") for row in black_grid)

    return damaged_count


bounded_input_str = parse_and_add_boundaries(input_str)

rose = rose_scenario(bounded_input_str)
black = black_scenario(bounded_input_str)


print(f"{rose}, {black}")  # Expected output: 19, 23
