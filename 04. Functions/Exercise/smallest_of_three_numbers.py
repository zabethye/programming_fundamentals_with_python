def return_min_of_numbers(number_one, number_two, number_three):
    numbers = [number_one, number_two, number_three]
    return min(numbers)


num_one = int(input())
num_two = int(input())
num_three = int(input())
print(return_min_of_numbers(num_one, num_two, num_three))
