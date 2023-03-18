class custom_range:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.counter = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > self.stop:
            raise StopIteration

        result = self.counter
        self.counter += 1

        return result


# one = custom_range(1, 10)
# for x in one:
#     print(x)
