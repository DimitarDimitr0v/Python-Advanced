import math
n = int(input())

even_numbers_set = set()
odd_numbers_set = set()
result = 0

for row in range(1, n + 1):
    name = input()
    sum_of_letters = 0

    for l in name:
        current_ascii_value = ord(l)
        sum_of_letters += current_ascii_value

    result = math.floor((sum_of_letters / row))

    if result % 2 == 0:
        even_numbers_set.add(result)
    else:
        odd_numbers_set.add(result)

even = sum(even_numbers_set)
odd = sum(odd_numbers_set)

if even == odd:
    united = [str(x) for x in even_numbers_set.union(odd_numbers_set)]
    print(', '.join(united))

elif odd > even:
    difference = sorted(odd_numbers_set.difference(), reverse=True)
    difference_str = [str(x) for x in difference]
    print(', '.join(difference_str))

elif even > odd:
    symmetrical_difference = [str(x) for x in even_numbers_set.symmetric_difference(odd_numbers_set)]
    print(', '.join(symmetrical_difference))