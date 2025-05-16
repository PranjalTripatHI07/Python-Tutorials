#DATE - 10/2/2025

# message
def show_message(messages):
    for message in messages:
        print(f"\n {message}")
msg = ["Hello How are you", "Welcome to our first tutorial", "Today we are learning about", "Passing list in a function", "Hope you all are ready to begin", "Lets start today's session "]

show_message(messages = msg )

# sending message

def send_messages(messages, sent_messages):
    while messages:
        current_status = messages.pop()

        print(f"\n List of messages:- {current_status}")

        sent_messages.append(current_status)


def show_message(messages):
    for message in messages:
        print(f"\n {message}")


msg = ["Hello How are you", "Welcome to our first tutorial", "Today we are learning about", "Passing list in a function", "Hope you all are ready to begin", "Lets start today's session "]
messages_sent = []

send_messages(messages=msg, sent_messages=messages_sent)
show_message(messages=messages_sent)


#Archived Messages

def send_messages(messages, sent_messages):
    while messages:
        current_state = messages.pop()
        print(f"\n list of messages :- {current_state}")

        sent_messages.append(current_state)

def show_messages(sent_messages):
    for message in sent_messages:
        print(f"\n {message}")

msg = ["Hello How are you", "Welcome to our first tutorial", "Today we are learning about", "Passing list in a function", "Hope you all are ready to begin", "Lets start today's session "]
messages_sent = []

send_messages(messages=msg[:], sent_messages=messages_sent)
show_messages(sent_messages=messages_sent)
print("-----------------------------------next---------------------------")
send_messages(messages=msg, sent_messages=messages_sent)
show_messages(sent_messages=messages_sent)