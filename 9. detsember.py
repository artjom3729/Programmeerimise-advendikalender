sisend = """00011
10011
11001
10101
11010"""

def count_2x2_squares_of_zeros(sisend):
    grid = [list(map(int, line)) for line in sisend.strip().splitlines()]
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    for r in range(rows - 1):
        for c in range(cols - 1):
            if (grid[r][c] == 0 and grid[r][c+1] == 0 and
                grid[r+1][c] == 0 and grid[r+1][c+1] == 0):
                count += 1
    
    return count

result = count_2x2_squares_of_zeros(sisend)
print(result)