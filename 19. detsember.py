input_str = "1, 3, 4, 5, 5, 3, 3, 3, 4, 5, 6, 6, 4, 5, 6"

input_str = [int(n.strip()) for n in input_str.split(", ")]


def longest_increasing_subsequence(argument):
    if not argument:
        return 0

    list = [1] * len(argument)

    for i in range(1, len(argument)):
        for j in range(0, i):
            if argument[i] > argument[j] and list[i] < list[j] + 1:
                list[i] = list[j] + 1

    return max(list)


longest_subsequence = longest_increasing_subsequence(input_str)

print(longest_subsequence)
