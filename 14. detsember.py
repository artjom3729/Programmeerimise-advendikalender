sisend = """###############UU#  
#______LLO____LL_#  
#______LL_____LL_#  
#_____#_______LL_#  
#####_#__O_##OLL_#  
#__LL_#OLL_______#  
#__LL_#_LL_______#  
#_____#_LL_O_____#  
#_O___#__________#  
###########__#####  
      #__________#  
      #_______OO_#
      #__LLL_____#
      U__LLL_____#
      #######O___#
            U__O_#
            #__O_#
            U____#
            #____#
            ######"""

def can_place_chair(grid, row, col):
    if grid[row][col] != '_':
        return False
    
    # Check adjacent tiles
    adjacent_positions = [
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1)
    ]
    
    has_L = False
    for r, c in adjacent_positions:
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            continue
        if grid[r][c] == 'U' or grid[r][c] == 'O':
            return False
        if grid[r][c] == 'L':
            has_L = True
    
    return has_L

def count_chairs(sisend):
    grid = [list(line) for line in sisend.strip().split('\n')]
    chair_count = 0
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if can_place_chair(grid, row, col):
                chair_count += 1
    
    return chair_count

chair_count = count_chairs(sisend)
print(chair_count)