from itertools import permutations


def possible_permutations(sequence):

    perms = permutations(sequence)

    for el in perms:
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]
