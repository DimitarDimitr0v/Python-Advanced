def read_next(*args):
    tuple_index = 0

    for el in args:
        if isinstance(el, str) or \
                isinstance(el, tuple) or \
                isinstance(el, dict) or \
                isinstance(el, list):

            for key in el:
                yield key


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
