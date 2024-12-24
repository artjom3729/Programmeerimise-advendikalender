input_str = """__________
__________
_____X____
_____X____
_____X____
_______X__
______X___
_____X____
__________
__________"""

def find_perimeter(input_str: str) -> int:
    input_str = input_str.strip().splitlines()

    top_x = (float("inf"), float("inf"))
    bottom_x = (0, 0)
    left_x = (float("inf"), float("inf"))
    right_x = (0, 0)

    for y in range(len(input_str)):
        for x in range(len(input_str[y])):
            if input_str[y][x] == "X":
                if y < top_x[1]:
                    top_x = (x, y)
                if y > bottom_x[1]:
                    bottom_x = (x, y)
                if x < left_x[0]:
                    left_x = (x, y)
                if x > right_x[0]:
                    right_x = (x, y)

    return 2 * (bottom_x[1] - top_x[1] + right_x[0] - left_x[0] + 4)

print(find_perimeter(input_str)) # Oodatav väljund: 22