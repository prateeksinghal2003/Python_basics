import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 12345))

while True:
    data, addr = sock.recvfrom(4096)
    print(str(data))

    message = bytes("Hello I am UDP Server", "utf-8")
    sock.sendto(message, addr)

#
# Big Picture First
#
# Think of UDP like throwing paper notes 📄
# You throw a note to the server.
# The server reads it and throws a note back.
# No connection, no guarantee — just send and receive.
#
# 🖥️ Server Code — “The Listener”
# Flow of the Server
#
# “I’m here. I’m waiting.
# Whenever someone sends me a message, I’ll read it and reply.”
#
# Step-by-step Feel
# 1️⃣ Create the server
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
#
# 💭 “I am opening a UDP phone.”
#
# AF_INET → Internet (IP address)
#
# SOCK_DGRAM → UDP (datagram / message-based)
#
# 2️⃣ Fix my address
# sock.bind(('127.0.0.1', 12345))
#
#
# 💭 “I will stand at this location and listen.”
#
# IP → localhost (your own machine)
#
# Port → 12345 (my door number)
#
# 3️⃣ Wait forever
# while True:
#
#
# 💭 “I’m always available. I never sleep.”
#
# 4️⃣ Receive message
# data, addr = sock.recvfrom(4096)
#
#
# 💭 “Someone sent me a note!”
#
# data → message content
#
# addr → who sent it (client address)
#
# 5️⃣ Show message
# print(str(data))
#
#
# 💭 “Let me read it on my screen.”
#
# 6️⃣ Reply back
# message = bytes("Hello I am UDP Server", "utf-8")
# sock.sendto(message, addr)
#
#
# 💭 “Let me send a reply to the same person.”
#
