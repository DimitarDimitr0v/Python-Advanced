from collections import deque
default_green_light_duration = int(input())
default_free_window_duration = int(input())

current_car_queue = deque()

safe_passed_cars = 0
crash = False

current_green_light_duration = default_green_light_duration  # value that we use
current_free_window_duration = default_free_window_duration  # value that we use

command = input()
while not command == "END":

    if not command == "green":  # add the car model
        current_car_queue.append(command)

    else:                       # we are in cycle
        current_green_light_duration = default_green_light_duration  # reset the light

        while len(current_car_queue) > 0:  # if we still have cars waiting
            if current_green_light_duration > 0:    # check if we are in green cycle
                current_car = current_car_queue.popleft()   # identify the car
                for i in range(len(current_car)):
                    if current_green_light_duration <= 0:  # we have entered the free window duration
                        free_window = True
                        car_char = current_car[i]
                        if current_free_window_duration - 1 >= 0:
                            current_free_window_duration -= 1
                        else:
                            crash = True
                            print(f"A crash happened!")
                            print(f"{current_car} was hit at {car_char}.")
                            exit()
                    else:                                  # we are in green cycle
                        car_char = current_car[i]
                        current_green_light_duration -= 1

                safe_passed_cars += 1

            else:
                break

    command = input()

if not crash:
    print(f"Everyone is safe.")
    print(f"{safe_passed_cars} total cars passed the crossroads.")