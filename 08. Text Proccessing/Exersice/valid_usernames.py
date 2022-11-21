usernames = input().split(", ")
valid_usernames = []
is_valid = False

for username in usernames:
    if 3 <= len(username) <= 16:
        for char in username:
            if char == " ":
                is_valid = False
                break
            if not (char.isalnum() or char == "-" or char == "_"):
                is_valid = False
                break
            is_valid = True
        if is_valid:
            valid_usernames.append(username)

print("\n".join(valid_usernames))
