from collections import deque

# read input
textiles = deque(map(int, input().split()))
medicaments = deque(map(int, input().split()))

# initialize variables
items = {"Patch": 30, "Bandage": 40, "MedKit": 100}
acquired_items = {"Patch": 0, "Bandage": 0, "MedKit": 0}


# process the collections
while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()

    # check if the sum is in the items table
    if textile + medicament in items.values():
        for item, value in items.items():
            if value == textile + medicament:
                acquired_items[item] += 1
                break

    # check if the sum is bigger than the MedKit
    elif textile + medicament > items["MedKit"]:
        acquired_items["MedKit"] += 1
        remaining = textile + medicament - items["MedKit"]
        medicaments[-1] += remaining

    else:
        medicaments.append(medicament + 10)


if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

sorted_items = sorted(acquired_items.items(), key=lambda x: (-x[1], x[0]))

for item in sorted_items:
    if item[1] > 0:
        print(f"{item[0]} - {item[1]}")

if medicaments:
    print(f"Medicaments left: {', '.join(str(x) for x in sorted(medicaments, reverse=True))}")

if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")
