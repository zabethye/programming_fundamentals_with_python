def lenght_validation(password):
    if len(password) < 6 or len(password) > 10:
        return False
    return True


def alphanum_validation(password):
    if not password.isalnum():
        return False
    return True


def digit_validation(password):
    digit_counter = 0
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for digit in password:
        if digit in digits:
            digit_counter += 1
    if digit_counter < 2:
        return False
    return True




def final_validation(password):
    lenght = lenght_validation(password)
    alphanum = alphanum_validation(password)
    digit = digit_validation(password)
    if lenght is True and alphanum is True and digit is True:
        print("Password is valid")
        return
    if not lenght:
        print("Password must be between 6 and 10 characters")
    if not alphanum:
        print("Password must consist only of letters and digits")
    if not digit:
        print("Password must have at least 2 digits")


passwrd = input()
final_validation(passwrd)
