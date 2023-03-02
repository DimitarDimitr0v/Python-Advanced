def fill_the_box(height, length, width, *args):
    static_volume = height * width * length

    args = list(args)
    volume = static_volume
    space_taken = 0
    indexes_to_pop = 0

    for i in range(len(args)):
        el = args[i]

        if el == "Finish":
            break

        else:
            current_cube = int(el)

            if (volume - current_cube) >= 0:
                space_taken += current_cube
                volume -= current_cube
                indexes_to_pop += 1
            else:
                args[i] = (current_cube - volume)
                volume = 0
                space_taken = static_volume
                break


    if static_volume > space_taken:
        return f"There is free space in the box. You could put {static_volume - space_taken} more cubes."
    else:
        [args.pop(0) for _ in range(indexes_to_pop)]
        return f"No more free space! You have {sum([int(x) for x in args if not x == 'Finish'])} more cubes."



print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))