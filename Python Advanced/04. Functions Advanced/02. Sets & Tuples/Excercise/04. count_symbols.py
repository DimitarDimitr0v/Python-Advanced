name = input()
total_chars = []

for ch in name:
    total_chars.append(ch)

one_time_mentioned = []
for el in total_chars:
    if el not in one_time_mentioned:
        one_time_mentioned.append(el)

sorted_chars = sorted(one_time_mentioned)

for elmnt in sorted_chars:
    print(f"{elmnt}: {total_chars.count(elmnt)} time/s")