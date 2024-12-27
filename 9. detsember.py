input_str = """10001
11001
11110
11100
11110"""

def count_2x2_squares_of_ones(input_str):
    grid = [list(map(int, line)) for line in input_str.strip().splitlines()]
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    for r in range(rows - 1):
        for c in range(cols - 1):
            if (grid[r][c] == 1 and grid[r][c+1] == 1 and
                grid[r+1][c] == 1 and grid[r+1][c+1] == 1):
                count += 1
    
    return count


result = count_2x2_squares_of_ones(input_str)
print(result) # Expected output: 5
