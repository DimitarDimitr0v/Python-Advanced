sequence = [float(x) for x in tuple(input().split())]

printed_numbers = []

for el in sequence:
    if el not in printed_numbers:
        print(f"{el} - {sequence.count(el)} times")
        printed_numbers.append(el)
