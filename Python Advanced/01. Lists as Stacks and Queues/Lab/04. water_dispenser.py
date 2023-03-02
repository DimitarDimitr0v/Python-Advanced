from collections import deque

START_COMMAND = "Start"
END_COMMAND = "End"

names_deque = deque()
total_water = int(input())

command_started = False


def refill(f_total_water, f_liters):
    return f_total_water + f_liters


def give_water(f_total_water, f_liters_needed, f_names_deque):
    if f_total_water - f_liters_needed >= 0:
        print(f"{f_names_deque.popleft()} got water")
        f_total_water -= f_liters_needed
    else:
        print(f"{f_names_deque.popleft()} must wait")

    return f_total_water


while True:
    name = input()

    if name == START_COMMAND:
        command_started = True
        continue

    if name == END_COMMAND:
        break

    if not command_started:
        names_deque.append(name)

    if command_started:
        if "refill" in name:
            command_info = name.split()
            liters = int(command_info[1])
            total_water = refill(total_water, liters)
        else:
            liters_needed = int(name)
            total_water = give_water(total_water, liters_needed, names_deque)

print(f"{total_water} liters left")
