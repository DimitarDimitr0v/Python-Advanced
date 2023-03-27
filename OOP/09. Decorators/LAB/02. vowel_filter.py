import functools


def vowel_filter(function):
    @functools.wraps(function)
    def wrapper():
        sequence = function()
        vowels = ["a", "e", "o", "u", "i"]

        return [x for x in sequence if x in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
