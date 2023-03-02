def check_colors(first, last, total):
    first_combination = first + last
    second_combination = last + first

    if first_combination in total:
        return first_combination
    elif second_combination in total:
        return second_combination
    else:
        return None


def remove_empty_strings(original_list):
    new_list = []
    for item in original_list:
        if item != "":
            new_list.append(item)
    return new_list


string = input().split()
colors_acquired = []

total_colors = [
    'red',
    'yellow',
    'blue',
    'purple',
    'orange',
    'green'
]

while string:
    if len(string) == 1:
        if string[0] in total_colors:
            colors_acquired.append(string.pop())
            break
        else:
            break

    first_substring = string[0]
    last_substring = string[-1]
    color = check_colors(first_substring, last_substring, total_colors)

    if color in total_colors:
        colors_acquired.append(color)
        string.remove(first_substring)
        string.remove(last_substring)
    else:

        first_substring = first_substring[:len(first_substring) - 1]
        last_substring = last_substring[:len(last_substring) - 1]

        index = len(string) // 2

        if len(string) % 2 == 0:
            string.insert(index, first_substring)
            string.insert(index, last_substring)
        else:
            string.insert(index + 1, first_substring)
            string.insert(index + 1, last_substring)

        string.pop(0)
        string.pop(-1)
        string = remove_empty_strings(string)

if 'orange' in colors_acquired:
    if 'red' and 'yellow' not in colors_acquired:
        colors_acquired.remove('orange')

if 'purple' in colors_acquired:
    if 'red' and 'blue' not in colors_acquired:
        colors_acquired.remove('purple')

if 'green' in colors_acquired:
    if 'blue' and 'yellow' not in colors_acquired:
        colors_acquired.remove('green')

print(colors_acquired)