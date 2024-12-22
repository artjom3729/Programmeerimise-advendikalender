numbrid = "55"
sisend = """1123255
1415640
6415634
6414248
5513154
5412641
6412652
2412054"""

numbrid = [int(digit) for digit in numbrid]

sisend = sisend.strip().splitlines()

uus_sisend = []

for n in sisend:
    n = [int(char) for char in n]
    uus_sisend.append(n)

telefoninumbrid = []

for n in uus_sisend:
    if n[0] == numbrid[0] and n[1] == numbrid[1]:
        telefoninumbrid.append(int("".join(map(str, n)))) 

for y in range(len(uus_sisend) - 6):
    for x in range(len(uus_sisend[y])):
        if (uus_sisend[y][x] == numbrid[0] and 
            uus_sisend[y+1][x] == numbrid[1]):
            telefoninumber = int("".join(str(uus_sisend[y+i][x]) for i in range(7)))
            telefoninumbrid.append(telefoninumber)

print(telefoninumbrid)