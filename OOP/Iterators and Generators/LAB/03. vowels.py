class vowels:
    def __init__(self, string):
        self.string = string
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U']
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.counter < len(self.string):

            if self.string[self.counter] in self.vowels:
                result = self.string[self.counter]
                self.counter += 1
                return result
            else:
                self.counter += 1

        raise StopIteration


# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)