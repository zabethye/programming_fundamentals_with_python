def positive(number):
    result = [num for num in number if int(num) >= 0]
    return result


def negative(number):
    result = [num for num in number if int(num) < 0]
    return result


def even(number):
    result = [num for num in number if int(num) % 2 == 0]
    return result


def odd(number):
    result = [num for num in number if int(num) % 2 != 0]
    return result


numbers = input().split(", ")
print(f"Positive:", ", ".join(positive(numbers)))
print(f"Negative:", ", ".join(negative(numbers)))
print(f"Even:", ", ".join(even(numbers)))
print(f"Odd:", ", ".join(odd(numbers)))
