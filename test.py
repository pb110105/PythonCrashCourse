msg = ['Hello', 'Phambao', 'I will become a King of Pirate']
def show_messages(msg):
    for m in msg:
        print(m)
show_messages(msg)
#8-10. Sending Messages
sent_messages = []
def send_messages(msg, sent_messages):
    while msg:
        current_message = msg.pop(0)
        print(f"\nMessage: {current_message}")
        sent_messages.append(current_message)
    for s in sent_messages:
        print(s)
send_messages(msg, sent_messages)
print("----")
print(msg)
print(sent_messages)
#8-11. Archived Messages
print("--")
archive = send_messages(msg[:], sent_messages)
print(sent_messages)