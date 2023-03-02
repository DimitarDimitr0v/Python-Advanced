petrol_pumps = int(input())

x = []

current_fuel_capacity = 0

for stations in range(petrol_pumps):
    pumps_info = [int(x) for x in input().split()]
    x.append(pumps_info)

tested_index = 0

i = 0
while i < len(x):
    fuel = x[i][0]
    distance = x[i][1]

    current_fuel_capacity += fuel

    if current_fuel_capacity - distance >= 0:
        current_fuel_capacity -= distance
        i += 1
        continue
    else:
        x.append(x[0])
        x.remove(x[0])
        tested_index += 1
        current_fuel_capacity = 0
        i = 0

print(tested_index)