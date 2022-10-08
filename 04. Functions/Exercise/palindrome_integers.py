def palindrome_searcher(nums):
    for num in nums:
        backword_num = num[::-1]
        if backword_num == num:
            print(True)
        else:
            print(False)


numbers = input().split(", ")
palindrome_searcher(numbers)
