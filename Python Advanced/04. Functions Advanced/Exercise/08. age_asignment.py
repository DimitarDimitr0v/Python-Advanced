def age_assignment(*names, **years):
    result = []
    for k, v in years.items():
        for el in names:
            if k in el[0]:
                result.append(f"{el} is {v} years old.")

    return '\n'.join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))