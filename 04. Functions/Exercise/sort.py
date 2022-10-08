def sorted_numbers(nums):
    nums_as_digits = []
    for num in nums:
        nums_as_digits.append(int(num))
    return sorted(nums_as_digits)


numbers = input().split()
print(sorted_numbers(numbers))
