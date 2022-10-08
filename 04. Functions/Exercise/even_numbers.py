def even_return(nums):
    nums_as_digits = []
    for num in nums:
        nums_as_digits.append(int(num))
    even_numbers = list(filter(lambda x: x % 2 == 0, nums_as_digits))
    return even_numbers


numbers = input().split()
print(even_return(numbers))
