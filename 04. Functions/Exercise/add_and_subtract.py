def sum_numbers(number_one, number_two):
    return number_one + number_two


def subtract(first_num, third_num):
    return first_num - third_num


def add_and_subtract(first_num, second_num, third_num):
    sum_result = sum_numbers(first_num, second_num)
    subtract_result = subtract(sum_result, third_num)
    return subtract_result


num_one = int(input())
num_two = int(input())
num_three = int(input())
print(add_and_subtract(num_one, num_two, num_three))
