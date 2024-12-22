sisend = """__________
__________
_____X____
_____X____
_____X____
_______X__
______X___
_____X____
__________
__________"""

sisend = sisend.strip().splitlines()

ulemine_x = (float("inf"), float("inf"))
alumine_x = (0, 0)
vasak_x = (float("inf"), float("inf"))
parem_x = (0, 0)

for y in range(len(sisend)):
    for x in range(len(sisend[y])):
        if sisend[y][x] == "X":
            if y < ulemine_x[1]:
                ulemine_x = (x, y)
            if y > alumine_x[1]:
                alumine_x = (x, y)
            if x < vasak_x[0]:
                vasak_x = (x, y)
            if x > parem_x[0]:
                parem_x = (x, y)

kaugus = 2 * (alumine_x[1] - ulemine_x[1] + parem_x[0] - vasak_x[0] + 4)

print(kaugus)