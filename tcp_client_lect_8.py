import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345))

payload = "Hey Server"

try:
    while True:
        client_socket.send(payload.encode("utf-8"))

        data = client_socket.recv(1024)
        print("Server says:", data.decode("utf-8"))

        more = input("Want to send more data to the server? (y/n): ").strip().lower()

        if more == 'y':
            payload = input("Enter Payload: ")
        else:
            break

except:
    print("Exited by user")

client_socket.close()

# -------------------------------------------------------------------------------------------
#
# Big Picture (Feel the Program)
#
# This program is a TCP Client.
#
# Think of it like:
#
# You pick up a phone 📞, dial a shop’s number, talk, listen to the reply, and decide whether to keep talking or hang up.
#
# Your client:
#
# Picks up the phone (creates socket)
#
# Dials the server’s address (connects)
#
# Sends a message
#
# Listens to the reply
#
# Asks you if you want to keep talking
#
# Hangs up when done
#
# 🧱 Python Basics You’ll See
# Concept	Meaning
# import	Bring a library into your program
# variable	Store values
# function()	Perform an action
# while True:	Loop forever
# if	Decision making
# try / except	Error handling
# .method()	Call function on object
# indentation	Defines code blocks
# 🧩 Line-by-Line (With Feel)
# 1️⃣ Import Networking Power
# import socket
#
# Feel:
#
# “Python, give me the ability to talk over the network.”
#
# Basic:
#
# socket is a module
#
# import loads it
#
# 2️⃣ Create the Phone
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# Feel:
#
# You pick up a TCP phone.
#
# Breakdown:
#
# client_socket → variable storing socket
#
# AF_INET → IPv4
#
# SOCK_STREAM → TCP
#
# 3️⃣ Dial the Server
# client_socket.connect(('127.0.0.1', 12345))
#
# Feel:
#
# You dial the shop’s number.
#
# Breakdown:
#
# '127.0.0.1' → same computer (localhost)
#
# 12345 → server’s door number (port)
#
# connect() → start TCP handshake
#
# 4️⃣ First Message
# payload = 'Hey Server'
#
# Feel:
#
# You prepare what you’ll say first.
#
# Python:
#
# payload is a string variable
#
# 🧠 Safe Zone
# try:
#
#
# “Everything inside here might fail — be ready.”
#
# 🔄 Talking Loop
# 5️⃣ Loop Forever
# while True:
#
# Feel:
#
# “I’ll keep talking until I choose to stop.”
#
# 6️⃣ Send Message
# client_socket.send(payload.encode('utf-8'))
#
# Feel:
#
# You speak into the phone.
#
# Breakdown:
#
# .encode('utf-8') → text → bytes
#
# send() → send bytes over network
#
# 7️⃣ Listen for Reply
# data = client_socket.recv(1024)
#
# Feel:
#
# You listen to what the server says.
#
# Basic:
#
# Receives up to 1024 bytes
#
# Comes as bytes
#
# 8️⃣ Show Reply
# print("Server says:", data.decode('utf-8'))
#
# Feel:
#
# You read the reply out loud.
#
# Basic:
#
# .decode() → bytes → text
#
# 9️⃣ Ask the User
# more = input("Want to send more data to the server? (y/n): ").strip().lower()
#
# Feel:
#
# You ask yourself:
# “Do I want to keep talking?”
#
# Breakdown:
#
# input() → take user input
#
# .strip() → remove spaces
#
# .lower() → convert to lowercase
#
# 🔟 Decision
# if more == 'y':
#     payload = input("Enter Payload: ")
# else:
#     break
#
# Feel:
#
# If you say yes → prepare new message
#
# If you say no → hang up
#
# Python:
#
# if → condition
#
# break → exit loop
#
# 🛑 Emergency Exit
# except KeyboardInterrupt:
#     print("Exited by user")
#
# Feel:
#
# If you press Ctrl+C, exit politely instead of crashing.
#
# 📴 Hang Up
# client_socket.close()
#
# Feel:
#
# You put the phone down.
#
# 🔄 Full Flow (Mental Map)
# Start client
#    ↓
# Create socket
#    ↓
# Connect to server
#    ↓
# Send message
#    ↓
# Receive reply
#    ↓
# Ask user
#    ↓
# If yes → repeat
# If no → close socket
#    ↓
# End
