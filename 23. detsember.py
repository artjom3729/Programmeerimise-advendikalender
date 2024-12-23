sisend = """(()(()))
)())()((
()(()()(()))
(()()())
)(())))()"""

def is_properly_packed(gift):
    stack = []
    for char in gift:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

def check_gifts(sisend):
    gifts = sisend.strip().split('\n')
    results = []
    for idx, gift in enumerate(gifts):
        if is_properly_packed(gift):
            results.append(idx + 1)
    return results

print(", ".join(map(str, check_gifts(sisend))))
print(len(check_gifts(sisend)))