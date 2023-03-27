def division_with_others(number):
    for test_number in range(10):
        if test_number > 0 and test_number != 1 and test_number != number:

            if number % test_number == 0:
                return False

    return True


def get_primes(sequence_of_integers):
    for num in sequence_of_integers:
        if num > 1:
            if division_with_others(num):
                yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0,
                       2, 3, 5, 7, 11, 13, 17, 19,
                       23, 29, 31, 37])))
