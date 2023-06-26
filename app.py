# Comment in Python

def mean(numbers):
    total = 0
    count = 0

    for num in numbers:
        total += num
        count += 1

    if count == 0:
        return 0  # To handle empty list input

    mean_value = total / count
    return mean_value
