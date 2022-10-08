operator = input()
num1 = int(input())
num2 = int(input())


def calculate(operation, first_number, second_number):
    result = None
    if operation == "multiply":
        result = first_number * second_number
    elif operation == "divide":
        result = int(first_number / second_number)
    elif operation == "add":
        result = first_number + second_number
    elif operation == "subtract":
        result = first_number - second_number
    return result


print(calculate(operator, num1, num2))
