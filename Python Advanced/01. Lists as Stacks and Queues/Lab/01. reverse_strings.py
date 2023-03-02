text = input()

s = []

for el in text:
    s.append(el)

while s:
    print(s.pop(), end="")
