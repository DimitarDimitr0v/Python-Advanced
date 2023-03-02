import sys
n = int(input())

total_intersections = []

for _ in range(n):
    first_set = set()
    second_set = set()
    total_section_data = input().split('-')

    first_section_data = total_section_data[0].split(',')
    first_section_start = int(first_section_data[0])
    first_section_end = int(first_section_data[1])

    second_section_data = total_section_data[1].split(',')
    second_section_start = int(second_section_data[0])
    second_section_end = int(second_section_data[1])

    for fs in range(first_section_start, first_section_end + 1):
        first_set.add(fs)

    for ss in range(second_section_start, second_section_end + 1):
        second_set.add(ss)

    intersection = first_set.intersection(second_set)
    total_intersections.append(intersection)

min_number = -sys.maxsize
index_with_biggest_length = 0

for i in range(len(total_intersections)):
    if len(total_intersections[i]) > min_number:
        min_number = len(total_intersections[i])
        index_with_biggest_length = i

print(f"Longest intersection is {list(total_intersections[index_with_biggest_length])} "
      f"with length {len(total_intersections[index_with_biggest_length])}")