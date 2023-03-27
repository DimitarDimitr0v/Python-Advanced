def number_increment(numbers):

    def increase():
        result = []

        for el in numbers:
            result.append(el + 1)
        return result

    return increase()


print(number_increment([1, 2, 3]))