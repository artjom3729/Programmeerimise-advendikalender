input_str = """(()(()))
)())()((
()(()()(()))
(()()())
)(())))()"""


def is_properly_packed(gift):
    stack = []
    for char in gift:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


def check_gifts(input_str):
    gifts = input_str.strip().splitlines()
    results = []
    for idx, gift in enumerate(gifts):
        if is_properly_packed(gift):
            results.append(idx + 1)
    return results


print(", ".join(map(str, check_gifts(input_str))))


print(len(check_gifts(input_str))) # Expected output: 3
