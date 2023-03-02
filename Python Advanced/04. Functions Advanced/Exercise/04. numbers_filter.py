def even_odd_filter(**kwargs):
    for key, value in kwargs.items():

        if key == "odd":
            kwargs[key] = [x for x in kwargs[key] if not x % 2 == 0]
        if key == "even":
            kwargs[key] = [y for y in kwargs[key] if y % 2 == 0]

    result = dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))
    return result



print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

