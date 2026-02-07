import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12345))
server_socket.listen(5)

while True:
    print("Server waiting for connection")


    try:
        client_socket, addr = server_socket.accept()
        print("Client connected from", addr)

        while True:
          data = client_socket.recv(1024)
          if not data or data.decode("utf-8") == "END":
           break

           print("received from  client is", data.decode("utf-8"))


        client_socket.send(bytes("Hey client", "utf-8"))

    except:
       print("Exited by the user")
       client_socket.close()

server_socket.close()


#
# 1️⃣ Import Power
# import socket
#
# Feel:
#
# You’re saying:
#
# “Python, give me networking powers.”
#
# Python Basic:
#
# socket is a module (a file full of functions and tools)
#
# import loads it into your program
#
# 2️⃣ Create the Shop (Socket)
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# Feel:
#
# You’re building a telephone system for your shop.
#
# Breakdown:
#
# server_socket → a variable that stores the socket
#
# socket.socket() → creates a new socket
#
# AF_INET → use IPv4
#
# SOCK_STREAM → use TCP (reliable connection)
#
# 3️⃣ Give Your Shop an Address
# server_socket.bind(("127.0.0.1", 12345))
#
# Feel:
#
# You’re telling the world:
# “My shop is at THIS address.”
#
# Breakdown:
#
# "127.0.0.1" → your own computer (localhost)
#
# 12345 → your door number (port)
#
# bind() → attach socket to that address
#
# 4️⃣ Start Listening for Customers
# server_socket.listen(5)
#
# Feel:
#
# You open your door and say:
# “I can handle up to 5 people waiting in line.”
#
# Python + Network:
#
# 5 = backlog (waiting queue size)
#
# 5️⃣ Infinite Server Loop
# while True:
#
# Feel:
#
# “My shop never closes.”
#
# Python Basic:
#
# while = loop
#
# True = always true
# So this runs forever.
#
# 6️⃣ Tell Yourself You’re Waiting
# print("Server waiting for connection")
#
# Feel:
#
# The shopkeeper says:
# “I’m waiting for someone to walk in…”
#
# Python Basic:
#
# print() displays text on screen
#
# 7️⃣ Accept a Client
# client_socket, addr = server_socket.accept()
#
# Feel:
#
# A customer walks in — you greet them.
#
# Breakdown:
#
# accept() → blocks (waits) until someone connects
#
# client_socket → new phone just for this client
#
# addr → client’s address (IP + port)

#  The Line
# client_socket, addr = server_socket.accept()
#
# What accept() Returns
#
# accept() does not return one thing.
# It returns TWO things packed together:
#
# (client_socket, addr)
#
#
# Think of it like a bundle.
#
#  Real-Life Analogy
#
# You ask:
#
# “Who came to my shop?”
#
# And you get:
#
# The person’s phone (socket to talk to them)
#
# The person’s address (IP + port)
#
# Both come together.
#
#  Python Concept: Tuple Unpacking
#
# This is called tuple unpacking.
#
# What’s a Tuple?
#
# A tuple is a group of values:
#
# result = (10, 20)
#
#
# Now you can split it like this:
#
# a, b = result
#
#
# So:
#
# a = 10
#
# b = 20
#
#  Apply It to Your Code
#
# server_socket.accept() returns:
#
# (client_socket, addr)
#
#
# So Python does:
#
# client_socket = first value
# addr = second value
#
#  What Each One Is
# ️ client_socket
#
# This is a new socket
#
# Used to talk to this specific client
#
# You use it for:
#
# client_socket.recv()
# client_socket.send()
# client_socket.close()
#
# addr
#
# This is the client’s address
# Example:
#
# ('127.0.0.1', 54321)
#
#
# Which means:
#
# IP address
#
# Port number
#
#  Why Comma Is Used
#
# The comma means:
#
# “Split what comes back into two variables.”
#
# It’s Python shorthand for:
#
# result = server_socket.accept()
# client_socket = result[0]
# addr = result[1]
#
# 8️⃣ Show Who Connected
# print("Client connected from", addr)
#
# Feel:
#
# You say:
# “This person came from this address.”
#
# 🧠 Inner Loop = Talking to the Client
# 9️⃣ Keep Talking Until They Leave
# while True:
#
# Feel:
#
# “I’ll keep listening to this customer.”
#
# 🔟 Receive Data
# data = client_socket.recv(1024)
#
# Feel:
#
# You listen to what the client says.
#
# Python + Network:
#
# recv(1024) → receive up to 1024 bytes
#
# Data comes in as bytes, not text
#
# 1️⃣1️⃣ Check If Client Left
# if not data or data.decode("utf-8") == "END":
# break

# Why decode() Exists
#
# When data travels over a network, it does NOT travel as text.
# It travels as bytes (0s and 1s).
#
# So:
#
# client_socket.recv(1024)
#
#
# gives you:
#
# b'Hello'
# Not:
# "Hello"
#
# That b means bytes, not string.
#
# 🔄 What decode() Does
# data.decode("utf-8")
#
# Meaning:
#
# “Convert these bytes into readable text.”
#
# So:
#
# b'Hello'  →  "Hello"
#
# 🌍 What is UTF-8?
#
# UTF-8 is a rulebook for converting:
#
# Text ↔ Bytes
#
# Think of it like a language dictionary.
#
# Example:
#
# The letter A:
#
# In text → "A"
#
# In bytes → 01000001
#
# UTF-8 defines:
#
# How every character (English, Hindi, emojis, symbols) is turned into bytes.
#
# 🧩 Full Meaning of This Line
# data.decode("utf-8") == "END"
#
# Step-by-step:
#
# data → bytes from network
# Example: b'END'
#
# .decode("utf-8") → turn into string
# "END"
#
# == "END" → check if client sent the word "END"
#
# 🛑 Why We Check for "END"
#
# This is your exit signal.
#
# It means:
#
# “Client is done talking. Close the connection.”
#
# 🔁 Opposite Process (Encoding)
#
# When you send data:
#
# client_socket.send(bytes("Hey client", "utf-8"))
#
#
# That does the reverse:
#
# "Hey client" → b'Hey client'
#
# 🧠 Mental Picture
# CLIENT SIDE
# "Hello"
#    ↓ encode (utf-8)
# b'Hello'
#    ↓ network
# SERVER SIDE
# b'Hello'
#    ↓ decode (utf-8)
# "Hello"
#
# 🧪 Tiny Python Demo
#
# Try this in Python:

text = "Hello 😊"
b = text.encode("utf-8")
print(b)
print(b.decode("utf-8"))
#
# Feel:
#
# If the customer says “END” or stays silent — they’re leaving.
#
# Python Basic:
#
# if = decision
#
# not data → nothing received
#
# .decode("utf-8") → bytes → text
#
# break → exit the loop
#
# 1️⃣2️⃣ Print Message
# print("received from client client is", data.decode("utf-8"))
#
# Feel:
#
# You repeat what the customer said out loud.
#
# 1️⃣3️⃣ Reply to Client
# try:
#     client_socket.send(bytes("Hey client", "utf-8"))
#
# Feel:
#
# You talk back to the customer.
#
# Python Basic:
#
# try → “This might fail, be careful”
#
# send() → send data
#
# bytes(..., "utf-8") → convert text → bytes
#
# 1️⃣4️⃣ Handle Errors
# except:
#     print("Exited by the user")
#     break
#
# Feel:
#
# If the client suddenly hangs up — you notice and stop talking.
#
# 1️⃣5️⃣ Close Client Connection
# client_socket.close()
#
# Feel:
#
# You hang up the phone for this customer.
#
# 🏁 Server Never Stops
# server_socket.close()
#
#
# This line technically:
#
# Would close the shop — but since while True never ends, it only runs if you force-stop the program.
#
# 🔄 Full Flow (Mental Picture)
# Start Server
#    ↓
# Create socket
#    ↓
# Bind address
#    ↓
# Listen
#    ↓
# WAIT FOR CLIENT
#    ↓
# Client connects
#    ↓
# Talk to client
#    ↓
# Client leaves
#    ↓
# WAIT FOR NEXT CLIENT
#    ↓
# Repeat forever

# ---------------------------------------------------------------------------------

# Your first code(tcpsocket_lect_6) = CLIENT
# This new code = SERVER
#
# Let’s compare them clearly.
#
# 🧩 Big Difference (One Line)
#
# First program connects to someone.
# This program waits for someone to connect.
#
# 🧱 Role Difference
# Feature	First Code (Client)	This Code (Server)
# Purpose	Makes a connection	Accepts connections
# Who starts	You	Client
# Waits for	Server	Client
# Address	Goes TO an IP+port	BINDS to IP+port
# Talks	Sends request	Receives request
# 🔄 Flow Difference (Feel It)
# CLIENT FLOW
# Create socket
#    ↓
# Ask user for host + port
#    ↓
# Resolve DNS
#    ↓
# CONNECT to server
#    ↓
# Send/Receive (optional)
#    ↓
# Close
#
# SERVER FLOW
# Create socket
#    ↓
# BIND to address
#    ↓
# LISTEN
#    ↓
# WAIT for client
#    ↓
# ACCEPT client
#    ↓
# Receive/Send in loop
#    ↓
# Close client
#    ↓
# WAIT for next client
#
# 🔍 Line-by-Line Key Differences
# 1️⃣ Address Handling
# Client:
# sock.connect((target_host, target_port))
#
#
# 👉 Goes to someone else
#
# Server:
# server_socket.bind(("127.0.0.1", 12345))
#
#
# 👉 Stays at one place and waits
#
# 2️⃣ Listening vs Connecting
# Client:
#
# No listen — it just connects
#
# Server:
# server_socket.listen(5)
#
#
# 👉 Opens the door for clients
#
# 3️⃣ Accepting Connections
# Client:
#
# Doesn’t accept anyone
#
# Server:
# client_socket, addr = server_socket.accept()
#
#
# 👉 Creates a new socket per client
#
# 4️⃣ Data Direction
# Client:
#
# Mostly sends:
#
# sock.connect(...)
#
# Server:
#
# Mostly receives:
#
# data = client_socket.recv(1024)
#
# 5️⃣ Looping Behavior
# Client:
#
# Runs once and exits
#
# Server:
#
# Runs forever
#
# while True:
#
#
# Keeps serving clients
#
# 6️⃣ Socket Usage
# Client:
#
# One socket:
#
# sock
#
# Server:
#
# Two sockets:
#
# server_socket  # main door
# client_socket  # private phone for each client
