numbers = "55"
input_str = """1123255
1415640
6415634
6414248
5513154
5412641
6412652
2412054"""

numbers = [int(digit) for digit in numbers]

input_str = input_str.strip().splitlines()

uus_input_str = []

for n in input_str:
    n = [int(char) for char in n]
    uus_input_str.append(n)

telefoninumbers = []

for n in uus_input_str:
    if n[0] == numbers[0] and n[1] == numbers[1]:
        telefoninumbers.append(int("".join(map(str, n)))) 

for y in range(len(uus_input_str) - 6):
    for x in range(len(uus_input_str[y])):
        if (uus_input_str[y][x] == numbers[0] and 
            uus_input_str[y+1][x] == numbers[1]):
            telefoninumber = int("".join(str(uus_input_str[y+i][x]) for i in range(7)))
            telefoninumbers.append(telefoninumber)

print(telefoninumbers)