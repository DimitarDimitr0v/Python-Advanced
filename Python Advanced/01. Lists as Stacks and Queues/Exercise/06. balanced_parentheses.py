import collections


def check_balanced_parentheses(sequence):
    stack = collections.deque()
    for char in sequence:
        if char in ("[", "{", "("):
            stack.append(char)
        elif char in ("]", "}", ")"):
            if not stack:
                return False
            top = stack.pop()

            if char == "]" and top != "[":
                return False
            if char == "}" and top != "{":
                return False
            if char == ")" and top != "(":
                return False
    return not stack


sequence = input()
if check_balanced_parentheses(sequence):
    print("YES")
else:
    print("NO")
