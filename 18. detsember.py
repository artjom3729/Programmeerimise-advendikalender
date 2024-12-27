from collections import defaultdict

input_str = """|==| |==| |==| |==| |==| 
| =| |  | |  | |  | |  |
|==| |==| |==| |==| |==|

|==| |==| |==| |==| |==|
|  | |  | |  | |  | |  |
|==| |==| |==| |==| |==|

|==| |==| |==| |==| |==|
|  | | =| |  | |  | |  |
|==| |==| |==| |==| |==|

|==| |==| |==| |==| |==|
|  | |  | |  | |  | |  |
|==| |==| |==| |==| |==|

|==| |==| |==| |==| |==|
|  | |  | |  | || | |  |
|==| |==| |==| |==|  ==|"""

correct_upper_part = "|==|"
correct_middle_part = "|  |"
correct_bottom_part = "|==|"

input_str = input_str.strip().splitlines()


def find_broken_cans(input_str):
    incorrect_columns = defaultdict(list)

    for x in range(0, len(input_str[0]), 5):
        for y in range(0, len(input_str), 4):
            upper_part = (
                input_str[y][x]
                + input_str[y][x + 1]
                + input_str[y][x + 2]
                + input_str[y][x + 3]
            )
            middle_part = (
                input_str[y + 1][x]
                + input_str[y + 1][x + 1]
                + input_str[y + 1][x + 2]
                + input_str[y + 1][x + 3]
            )
            bottom_part = (
                input_str[y + 2][x]
                + input_str[y + 2][x + 1]
                + input_str[y + 2][x + 2]
                + input_str[y + 2][x + 3]
            )
            if (
                upper_part != correct_upper_part
                or middle_part != correct_middle_part
                or bottom_part != correct_bottom_part
            ):
                row_number = int(y / 4) + 1
                column_number = int(x / 5) + 1
                incorrect_columns[row_number].append(column_number)

    output_rows = []

    for row in range(1, max(incorrect_columns.keys()) + 1):
        if row in incorrect_columns:
            output_rows.append(", ".join(map(str, incorrect_columns[row])))
        else:
            output_rows.append("")

    return "|" + "||".join(output_rows) + "|"


print(find_broken_cans(input_str)) # Expected output: |1||||2||||4, 5|
