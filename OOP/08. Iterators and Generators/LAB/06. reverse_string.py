def reverse_text(string: str):
    index = -1
    for letter in string:
        yield string[index]
        index -= 1


for char in reverse_text("step"):
    print(char, end='')
