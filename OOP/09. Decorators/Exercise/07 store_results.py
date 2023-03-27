import functools


def store_results(func):
    @functools.wraps(func)
    def wrapper(*args):
        result = func(*args)
        print(f"Function {func.__name__} was add called. Result: {result}")

    return wrapper


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
