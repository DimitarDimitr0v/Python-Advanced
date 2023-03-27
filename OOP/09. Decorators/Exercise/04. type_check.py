import functools


def type_check(type_info):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            if isinstance(*args, type_info):
                return func(*args, **kwargs)
            else:
                return f"Bad Type"

        return wrapper

    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
