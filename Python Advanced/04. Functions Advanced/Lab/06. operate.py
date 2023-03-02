import functools


def operate(operator, *numbers):
    result = 0

    if operator == '+':
        result += functools.reduce(lambda a, b: a + b, numbers)
    elif operator == '-':
        result += functools.reduce(lambda a, b: a - b, numbers)
    elif operator == '*':
        result += functools.reduce(lambda a, b: a * b, numbers)
    elif operator == '/':
        result += functools.reduce(lambda a, b: a / b, numbers)

    return result

print(operate("*", 3, 4))