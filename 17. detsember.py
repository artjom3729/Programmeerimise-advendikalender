from collections import deque

input_str = """##########
#L#.......
#.#.###.##
#.#...#...
#.###.###.
#.#...#.K.
#.#.###.#.
#.#.#...#.
#.###.###.
#.....#..."""

input_str = [list(line) for line in input_str.splitlines()]

lennart = None
kodu = None
for y in range(len(input_str)):
    for x in range(len(input_str[y])):
        if input_str[y][x] == 'L':
            lennart = (x, y)
        elif input_str[y][x] == 'K':
            kodu = (x, y)

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(lennart, kodu):
    queue = deque([lennart])
    visited = set()
    visited.add(lennart)
    parent = {lennart: None}
    direction_taken = {lennart: None}

    while queue:
        current = queue.popleft()
        if current == kodu:
            break

        for i, direction in enumerate(directions):
            next_x, next_y = current[0] + direction[0], current[1] + direction[1]
            if 0 <= next_x < len(input_str[0]) and 0 <= next_y < len(input_str):
                if input_str[next_y][next_x] != '#' and (next_x, next_y) not in visited:
                    queue.append((next_x, next_y))
                    visited.add((next_x, next_y))
                    parent[(next_x, next_y)] = current
                    direction_taken[(next_x, next_y)] = i

    path = []
    directions_path = []
    step = kodu
    while step is not None:
        path.append(step)
        step = parent[step]
    path.reverse()

    for i in range(1, len(path)):
        current_direction = direction_taken[path[i]]
        previous_direction = direction_taken[path[i - 1]]
        if previous_direction is not None:
            turn = (current_direction - previous_direction) % 4
            if turn == 1:
                directions_path.append('P')
            elif turn == 3:
                directions_path.append('V')

    return path, directions_path

path, directions_path = bfs(lennart, kodu)

print("".join(directions_path))