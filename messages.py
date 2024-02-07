messages = ['why', 'this syntax is so annoying', 'blah blah', 'stuff']
sent_messages = []
def print_messages(messages):
    for message in messages:
        print(message)

print_messages(messages)

def send_messages(messages):
    for message in messages:
        print("Sending")
        sent_messages.append(message)

send_messages(messages)
print(sent_messages)