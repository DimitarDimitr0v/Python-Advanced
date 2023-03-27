class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.count = 0
        self.total = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.total != self.number:

            if self.count < len(self.sequence):
                self.count += 1
                self.total += 1
                return self.sequence[self.count - 1]
            else:
                self.count = 0

        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')