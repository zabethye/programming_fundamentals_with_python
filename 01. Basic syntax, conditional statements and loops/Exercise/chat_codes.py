messages_count = int(input())

for message in range(messages_count):
    curr_message = int(input())
    if curr_message == 88:
        print("Hello")
    elif curr_message == 86:
        print("How are you?")
    elif curr_message < 88:
        print("GREAT!")
    elif curr_message > 88:
        print("Bye.")
