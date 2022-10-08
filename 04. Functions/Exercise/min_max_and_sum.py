def min_number(nums):
    nums_as_digits = []
    for num in nums:
        nums_as_digits.append(int(num))
    return min(nums_as_digits)


def max_number(nums):
    nums_as_digits = []
    for num in nums:
        nums_as_digits.append(int(num))
    return max(nums_as_digits)


def sum_numbers(nums):
    nums_as_digits = []
    for num in nums:
        nums_as_digits.append(int(num))
    return sum(nums_as_digits)


def min_max_sum(nums):
    min_num = min_number(nums)
    max_num = max_number(nums)
    sum_nums = sum_numbers(nums)
    return f"The minimum number is {min_num}\n" \
           f"The maximum number is {max_num}\n" \
           f"The sum number is: {sum_nums}"


numbers = input().split()
print(min_max_sum(numbers))
