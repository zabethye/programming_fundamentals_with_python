command = input()
chat_list = []
while command != "end":
    splitted_command = command.split()
    current_command = splitted_command[0]
    if current_command == "Chat":
        chat_list.append(splitted_command[1])
    elif current_command == "Delete":
        if splitted_command[1] in chat_list:
            chat_list.remove(splitted_command[1])
    elif current_command == "Edit":
        if splitted_command[1] in chat_list:
            for word in range(len(chat_list)):
                if chat_list[word] == splitted_command[1]:
                    chat_list.pop(word)
                    chat_list.insert(word, splitted_command[2])
                    break
    elif current_command == "Pin":
        if splitted_command[1] in chat_list:
            for word in range(len(chat_list)):
                if chat_list[word] == splitted_command[1]:
                    chat_list.pop(word)
                    chat_list.append(splitted_command[1])
    elif current_command == "Spam":
        for word in splitted_command:
            if word == "Spam":
                continue
            chat_list.append(word)
    command = input()

print("\n".join(chat_list))
