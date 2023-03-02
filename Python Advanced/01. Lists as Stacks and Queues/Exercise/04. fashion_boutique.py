total_clothes = input().split()
capacity = int(input())

summed_clothes_value = 0
racks = 0

while total_clothes:

    if summed_clothes_value < capacity:
        if int(total_clothes[-1]) + summed_clothes_value > capacity:
            racks += 1
            summed_clothes_value = 0
        else:
            summed_clothes_value += int(total_clothes.pop())
    else:
        racks += 1
        summed_clothes_value = 0

if summed_clothes_value != 0:
    racks += 1

print(racks)