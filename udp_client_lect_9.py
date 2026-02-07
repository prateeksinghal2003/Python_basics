import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Enter message: ")
    client_socket.sendto(msg.encode("utf-8"), ("127.0.0.1", 12345))

    data, addr = client_socket.recvfrom(4096)
    print("Server Says:", data.decode())

    more = input("Send more? (y/n): ")
    if more.lower() != 'y':
        break

client_socket.close()





#  Client Code — “The Messenger”
# Flow of the Client
#
# “I write a message.
# I throw it to the server.
# I wait for reply.
# I go home.”
#
# Step-by-step Feel
#  Create client
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
#
# 💭 “I have a UDP phone now.”
#
# 2️⃣ Write message
# msg = "Hello UDP Server"
#
#
# 💭 “This is what I want to say.”
#
# 3️⃣ Send message
# client_socket.sendto(msg.encode("utf-8"), ('127.0.0.1', 12345))
#
#
# 💭 “Throw this note to the server’s door.”
#
# Encoded → computer understands bytes
#
# IP + Port → where server is
#
# 4️⃣ Wait for reply
# data, addr = client_socket.recvfrom(4096)
#
#
# 💭 “I’m waiting… okay, server replied!”
#
# 5️⃣ Show reply
# print("Server Says")
# print(str(data))
#
#
# 💭 “Let me read what server said.”
#
# 6️⃣ Close
# client_socket.close()
#
#
# 💭 “My job is done. I’m leaving.”
#
# 🔁 Flow Summary (Interview Style)
# Client
#
# Send → Wait → Read → Exit
#
# Server
#
# Wait → Receive → Print → Reply → Repeat
#
#
# data, addr = client_socket.recvfrom(4096)
#
# Perfect — let’s feel this line instead of memorizing it
#
# 🧠 This Line:
# data, addr = client_socket.recvfrom(4096)
#
# 💭 What it feels like
#
# “I’ve sent my message.
# Now I’m standing and waiting at my door.
# When someone replies, I’ll take the message and note who sent it.”
#
# 🔍 Break it Simply
# recvfrom
#
# Means:
#
# Receive data from someone
#
# Since UDP has no connection, it always tells you:
#
# What message came
#
# Who sent it
#
# 📦 4096
#
# This means:
#
# “I can receive up to 4096 bytes in one message”
#
# Think of it as:
# 🧺 Size of the basket I use to catch the message
#
# 🧾 What you get back
# data
#
# 👉 The actual message (in bytes)
# Example:
#
# b'Hello I am UDP Server'
#
# addr
#
# 👉 Sender’s address (IP + port)
# Example:
#
# ('127.0.0.1', 12345)
#
# 🎯 Why client also gets addr
#
# Even though the client already knows the server, UDP still says:
