class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []
command = input()

while command != "Stop":
    splitted_command = command.split()
    email_sender = splitted_command[0]
    email_receiver = splitted_command[1]
    email_content = splitted_command[2]
    current_email = Email(email_sender, email_receiver, email_content)
    emails.append(current_email)
    command = input()

indices = [int(x) for x in input().split(", ")]

for indx in indices:
    emails[indx].send()

for curr_email in emails:
    print(curr_email.get_info())
