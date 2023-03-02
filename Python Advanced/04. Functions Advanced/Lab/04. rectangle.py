def rectangle(length, width):

    def area(side_length, side_width):
        return side_length * side_width

    def perimeter(side_length, side_width):
        return (side_length + side_width) * 2

    result = ''
    if not isinstance(length, int) or not isinstance(width, int):
        return f"Enter valid values!"

    else:
        rect_area = area(length, width)
        rect_perimeter = perimeter(length, width)

    result += f'Rectangle area: {rect_area}' + '\n'
    result += f'Rectangle perimeter: {rect_perimeter}'

    return result


print(rectangle(10, 10))

