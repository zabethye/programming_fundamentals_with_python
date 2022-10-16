nums = list(map(int, input().split(", ")))
boundary = 10

while len(nums) > 0:
    new_list = []
    for num in nums:
        if boundary - 10 < num <= boundary:
            new_list.append(num)
    for numb in new_list:
        for number in nums:
            if numb == number:
                nums.remove(number)
    print(f"Group of {boundary}'s: {new_list}")
    boundary += 10

