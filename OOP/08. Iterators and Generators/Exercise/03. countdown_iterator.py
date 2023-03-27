class countdown_iterator:
    def __init__(self, start_time):
        self.start_time = start_time
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.count <= self.start_time:
            self.start_time -= 1
            return self.start_time + 1

        raise StopIteration


iterator = countdown_iterator(30)
for item in iterator:
    print(item, end=" ")