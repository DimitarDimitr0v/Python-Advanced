from functools import reduce
from math import floor
expression = input().split()

operators = ["*", "+", "-", "/"]
temporary_numbers = []
result = ''

for value in expression:
    if value not in operators:
        temporary_numbers.append(value)
    else:
        if value == '+':
            summed = sum(int(x) for x in temporary_numbers)
            temporary_numbers = [str(summed)]
            result = summed
        elif value == '/':
            divided = reduce(lambda x, y: x // y, (int(x) for x in temporary_numbers))
            temporary_numbers = [str(divided)]
            result = divided
        elif value == '-':
            subtracted = reduce(lambda x, y: x - y, (int(x) for x in temporary_numbers))
            temporary_numbers = [str(floor(subtracted))]
            result = subtracted
        elif value == '*':
            multiplied = reduce(lambda x, y: x * y, (int(x) for x in temporary_numbers))
            temporary_numbers = [str(multiplied)]
            result = multiplied
print(result)