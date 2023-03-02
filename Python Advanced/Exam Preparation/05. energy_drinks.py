caffeine = [int(x) for x in input().split(", ")]
energy_drinks = [int(x) for x in input().split(", ")]

max_caffeine = 300
initial_caffeine = 0

while caffeine and energy_drinks:
    daily_caffeine_dose = caffeine.pop(-1)
    daily_energy_drinks = energy_drinks.pop(0)

    energy_and_caffeine = daily_energy_drinks * daily_caffeine_dose

    if initial_caffeine + energy_and_caffeine > max_caffeine:

        energy_drinks.append(daily_energy_drinks)

        if not initial_caffeine - 30 < 0:
            initial_caffeine -= 30
    else:
        initial_caffeine += energy_and_caffeine


if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")

else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {initial_caffeine} mg caffeine.")


