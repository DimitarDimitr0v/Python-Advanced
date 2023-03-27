class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary_as_list = [(k, v) for k, v in dictionary.items()]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.dictionary_as_list):
            self.index += 1
            return self.dictionary_as_list[self.index - 1]


        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
