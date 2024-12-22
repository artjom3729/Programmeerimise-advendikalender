sisend = """60x60x10
50x50x40
10x10x5"""

def parse_dimensions(sisend):
    blocks = []
    for line in sisend.strip().splitlines():
        l, w, h = map(int, line.split('x'))
        blocks.append((l, w, h))
    return blocks

def generate_orientations(blocks):
    orientations = []
    for l, w, h in blocks:
        orientations.append((l, w, h))
        orientations.append((l, h, w))
        orientations.append((w, l, h))
        orientations.append((w, h, l))
        orientations.append((h, l, w))
        orientations.append((h, w, l))
    return orientations

def base_area(block):
    return block[0] * block[1]

def tallest_tree_height(sisend):
    blocks = parse_dimensions(sisend)
    orientations = generate_orientations(blocks)
    orientations.sort(key=base_area, reverse=True)
    
    n = len(orientations)
    dp = [0] * n
    
    for i in range(n):
        dp[i] = orientations[i][2]
    
    for i in range(1, n):
        for j in range(i):
            if (orientations[i][0] < orientations[j][0] and
                orientations[i][1] < orientations[j][1]):
                dp[i] = max(dp[i], dp[j] + orientations[i][2])
    
    return max(dp)

result = tallest_tree_height(sisend)
print(result)