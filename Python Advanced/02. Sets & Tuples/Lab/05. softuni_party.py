number_of_guests = int(input())

total_guests = []

vip_guests = []
regular_guests = []

reservation_number = input()
while not reservation_number == "END":
    total_guests.append(reservation_number)
    reservation_number = input()

for i in range(len(total_guests)):
    if not total_guests.count(total_guests[i]) > 1:
        if total_guests[i][0].isdigit():
            vip_guests.append(total_guests[i])
        else:
            regular_guests.append(total_guests[i])

print(len(vip_guests + regular_guests))
sorted_vip = vip_guests.sort()
sorted_reg = regular_guests.sort()

for x in vip_guests:
    print(x)

for y in regular_guests:
    print(y)