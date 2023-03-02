n = int(input())
parking = []

for _ in range(n):
    command, plate = input().split(', ')

    if command == "IN":
        if plate not in parking:
            parking.append(plate)
    elif command == "OUT":
        if plate in parking:
            parking.remove(plate)

if len(parking) > 0:
    for x in parking:
        print(x)
else:
    print(f"Parking Lot is Empty")