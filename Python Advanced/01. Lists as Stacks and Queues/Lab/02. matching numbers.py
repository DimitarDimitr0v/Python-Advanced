algebraic_expression = input()

open_brackets = []

for i in range(len(algebraic_expression)):
    if algebraic_expression[i] == "(":
        open_brackets.append(i)
    elif algebraic_expression[i] == ")":
        print(algebraic_expression[open_brackets.pop():i + 1])
