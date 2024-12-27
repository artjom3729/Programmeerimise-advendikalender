input_str = "v v p p p p p v p v"


def find_tree_number(input_str):
    input_str = input_str.strip().split()
    input_str = [letter for letter in input_str if letter != " "]

    number = 1

    for letter in input_str:
        if letter == "p":
            number *= 2
        if letter == "v":
            number = number * 2 - 1

    return number


print(find_tree_number(input_str))  # Expected output: 251
