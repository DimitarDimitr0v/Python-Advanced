import functools


def validation(args):
    for el in args:
        if not isinstance(el, int):
            return False
        if not el % 2 == 0:
            return False

    return True


def even_parameters(function):
    @functools.wraps(function)
    def wrapper(*args):
        is_valid = validation(args)

        if is_valid:
            return function(*args)
        else:
            return f"Please use only even numbers!"

    return wrapper


@even_parameters
def func(*args):
    return sum(args)


result = func(4, 4, 4)
print(result) # 12
