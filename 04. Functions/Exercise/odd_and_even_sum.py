def sum_of_even_and_odd_digits(num):
    sum_even = 0
    sum_odd = 0
    for current_num in num:
        if int(current_num) % 2 == 0:
            sum_even += int(current_num)
        else:
            sum_odd += int(current_num)
    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"


number = input()
print(sum_of_even_and_odd_digits(number))
