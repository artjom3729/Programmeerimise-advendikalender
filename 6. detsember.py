numbers = "55"
input_str = """1123255
1415640
6415634
6414248
5513154
5412641
6412652
2412054"""

def find_phone_numbers(numbers, input_str):
    numbers = [int(digit) for digit in numbers]

    input_str = input_str.strip().splitlines()

    uus_input_str = []

    for n in input_str:
        n = [int(char) for char in n]
        uus_input_str.append(n)

    telephone_numbers = []

    for n in uus_input_str:
        if n[0] == numbers[0] and n[1] == numbers[1]:
            telephone_numbers.append(int("".join(map(str, n)))) 

    for y in range(len(uus_input_str) - 6):
        for x in range(len(uus_input_str[y])):
            if (uus_input_str[y][x] == numbers[0] and 
                uus_input_str[y+1][x] == numbers[1]):
                telephone_number = int("".join(str(uus_input_str[y+i][x]) for i in range(7)))
                telephone_numbers.append(telephone_number)
    
    return ", ".join(map(str, telephone_numbers))


print(find_phone_numbers(numbers, input_str)) # Expected output: 5513154, 5543222
