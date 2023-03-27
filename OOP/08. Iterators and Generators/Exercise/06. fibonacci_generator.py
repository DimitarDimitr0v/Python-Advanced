def fibonacci():
    starting_zero_and_one = 0

    for _ in range(2):
        yield starting_zero_and_one
        starting_zero_and_one += 1

    previous = 0
    current = 1

    while True:
        fibonacci_result = previous + current
        yield fibonacci_result
        previous = current
        current = fibonacci_result


generator = fibonacci()
for i in range(10):
    print(next(generator))