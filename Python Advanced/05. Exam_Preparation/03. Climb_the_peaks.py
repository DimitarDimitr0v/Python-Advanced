food_portions = [int(x) for x in input().split(", ")]
stamina = [int(x) for x in input().split(", ")]

difficulty = [80, 90, 100, 60, 70]
peaks = ["Vihren", "Kutelo", "Banski Suhodol", "Polezhan", "Kamenitza"]

conquered_peaks = []
current_peak_number = 0
days = 0

while True:

    if len(conquered_peaks) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break

    if days > 7 or not food_portions or not stamina:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break

    daily_food = food_portions.pop()
    daily_stamina = stamina.pop(0)

    daily_capability = daily_food + daily_stamina

    if daily_capability >= difficulty[current_peak_number]:
        conquered_peaks.append(peaks[current_peak_number])
        current_peak_number += 1

    days += 1

if conquered_peaks:
    print("Conquered peaks:")
    print("\n".join(conquered_peaks))