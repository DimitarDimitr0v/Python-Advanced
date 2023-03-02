def honey_calculator(worker_bee, operation, nectar_collected):
    if operation == '+':
        return abs(worker_bee + nectar_collected)
    elif operation == '-':
        return abs(worker_bee - nectar_collected)
    elif operation == '*':
        return abs(worker_bee * nectar_collected)
    elif operation == '/' and nectar_collected > 0:
        return abs(worker_bee / nectar_collected)
    else:
        return 0


working_bees = [int(x) for x in input().split()]
total_nectar = [int(x) for x in input().split()]
symbols = input().split()

collected_nectar = 0
collected_honey = 0

while working_bees and total_nectar:
    bee = working_bees[0]
    nectar = total_nectar[-1]

    if nectar >= bee:
        collected_nectar = nectar

    elif nectar < bee:
        total_nectar.pop()
        continue

    collected_honey += honey_calculator(bee, symbols[0], collected_nectar)
    working_bees.pop(0)
    total_nectar.pop()
    symbols.pop(0)

print(f"Total honey made: {collected_honey}")

if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if total_nectar:
    print(f"Nectar left: {', '.join([str(x) for x in total_nectar])}")