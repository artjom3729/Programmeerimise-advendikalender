from collections import deque

path = "KÜLMAV"
sisend = """-xxxA
xxxL+
KÜxxx
xxxVx
xxxxM"""

def find_position(grid, char):
    positions = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == char:
                positions.append((row, col))
    return positions

def bfs(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, 0)])  # (position, distance)
    visited = set([start])
    
    while queue:
        (r, c), dist = queue.popleft()
        
        if (r, c) == end:
            return dist
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] in 'x' + path + '+-':
                visited.add((nr, nc))
                queue.append(((nr, nc), dist + 1))
    
    return float('inf')  # If no path is found

def find_shortest_path_length(sisend, path):
    grid = [list(line) for line in sisend.strip().split('\n')]
    total_length = 0
    
    # Find the starting point (-)
    start = find_position(grid, '-')[0]
    
    # Traverse through the letters in the path
    for char in path:
        end_positions = find_position(grid, char)
        min_length = float('inf')
        best_end = None
        for end in end_positions:
            length = bfs(grid, start, end)
            if length < min_length:
                min_length = length
                best_end = end
        if min_length == float('inf'):
            return -1  # No path found
        total_length += min_length
        start = best_end
    
    # Finally, go to the end point (+)
    end_positions = find_position(grid, '+')
    min_length = float('inf')
    best_end = None
    for end in end_positions:
        length = bfs(grid, start, end)
        if length < min_length:
            min_length = length
            best_end = end
    if min_length == float('inf'):
        return -1  # No path found
    total_length += min_length
    
    return total_length

total_length = find_shortest_path_length(sisend, path)
print(f"Total path length: {total_length}")