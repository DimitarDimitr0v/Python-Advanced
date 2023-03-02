def negative_positive(sequence):
    negative = sum([x for x in sequence if x < 0])
    positive = sum([x for x in sequence if x > 0])
    return positive, negative


numbers = [int(x) for x in input().split()]

positives, negatives = negative_positive(numbers)

print(negatives)
print(positives)

if abs(positives) < abs(negatives):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")