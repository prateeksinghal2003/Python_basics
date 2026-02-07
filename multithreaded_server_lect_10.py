import socket
from _thread import *
# send for sendall and listen at last.


serversocket = socket.socket()

host = "127.0.0.1"
port = 1233

ThreadCount = 0

try:
    serversocket.bind((host, port))
except socket.error as e:
    print(str(e))

print("waiting for connection")
serversocket.listen(5)

def client_thread(connection):
    connection.send(str.encode("welcome to the server"))
    while True:
        data = connection.recv(2048)
        reply = "Hello I am server " + data.decode("utf-8")

        if not data:
            break

        connection.sendall(str.encode(reply))

    connection.close()

while True:
    client, address = serversocket.accept()

    # both sides of '+' should have string
    print("connected to: " + address[0] + ":" + str(address[1]))

    start_new_thread(client_thread, (client,))
    ThreadCount += 1
    print("Thread Number: " + str(ThreadCount))

server_socket.close()



#  Big Picture First
#
# This is a multi-threaded TCP server.
# That means:
#
# One server, many clients at the same time — each client gets its own “helper” (thread).
#
# 🖥️ Server’s Mindset
#
# “I open my door.
# When someone comes, I assign them a personal assistant (thread).
# That assistant talks to them while I stay free to welcome new people.”
#
#  Code Flow — Step by Step
#  Import tools
# import socket
# from _thread import *
#
#
#  “I need networking power and threading power.”
#
# socket → for TCP communication
#
# _thread → to handle multiple clients at once
#
#  Create server socket
# serversocket = socket.socket()
#
#
# 💭 “I open a TCP phone.”
# (Default = IPv4 + TCP)
#
# 3️⃣ Define my address
# host = "127.0.0.1"
# port = 1233
#
#
# 💭 “This is where people can find me.”
#
# 4️⃣ Track connections
# ThreadCount = 0

#
#  “I’ll count how many clients I’ve served.”
#
# 5️⃣ Bind to address
# serversocket.bind((host, port))
#
#
# 💭 “I stand at this IP and port and wait.”
#
# 6️⃣ Start listening
# serversocket.listen(5)
#
#
# 💭 “I can keep 5 people waiting in line while I help others.”
#
# 7️⃣ Define client handler
# def client_thread(connection):
#
#
# 💭 “This is the personal assistant for one client.”
#
# Welcome message

# str is an inbuilt class
# connection.send(str.encode("welcome to the server"))
#
#
# 💭 “First, I greet them.”
#
# Talk loop
# while True:
#
#
# 💭 “I keep listening until they leave.”
#
# Receive data
# data = connection.recv(2048)
#
#
# 💭 “Tell me what you want.”
#
# Prepare reply
# reply = "Hello I am server " + data.decode("utf-8")
#
#
# 💭 “Let me respond politely.”
#
# Check disconnect
# if not data:
#     break
#
#
# 💭 “If they stop talking, I stop too.”
#
# Send back
# connection.sendall(str.encode(reply))
#
#
# 💭 “Here’s my reply.”
#
# Close connection
# connection.close()
#
#
# 💭 “Conversation is over. Goodbye.”
#
# 8️⃣ Accept clients forever
# while True:
#     client, address = serversocket.accept()
#
#
# 💭 “Someone new is at the door!”
#
# Show who connected
# print("connected to: " + address[0] + ":" + str(address[1]))
#
#
#  “Let me write their name in my log.”
#
# Start new thread
# start_new_thread(client_thread, (client,))
#
#
# 💭 “Here’s your personal assistant.”
#
# Count them
# ThreadCount += 1
# print("Thread Number: " + str(ThreadCount))
#
#
# 💭 “Another client served!”
#
# 🔄 Flow Summary (Super Simple)
# Server Main Loop:
#
# Wait → Accept client → Create thread → Go back to waiting
#
# Client Thread:
#
# Welcome → Receive → Reply → Repeat → Close
#
#
# 1. What def means (Python basics)
# def client_thread(connection):
#
# What def does:
#
# def is used to define a function
#
# A function is a block of code you can run whenever you call it
#
# So this creates a function named:
#
# client_thread
#
#
# That will run when a new client connects
#
# 2. What connection contains (argument)
#
# This line:
#
# client, address = serversocket.accept()
#
#
# Then later:
#
# start_new_thread(client_thread, (client,))
#
#
# So:
#
# connection = client
# What connection actually is:
#
# It is a socket object for that specific client
#
# You use it to:
#
# Receive data:
#
# connection.recv(2048)
#
#
# Send data:
#
# connection.sendall(...)
#
#
# Close client:
#
# connection.close()
#
#
# So each connected client gets its own socket
#
# 3. What start_new_thread does
# start_new_thread(client_thread, (client,))
#
# Meaning:
#
# It starts a new thread
#
# That thread runs this function:
#
# client_thread(client)
#
# Why needed:
#
# Without threads:
#
# Server can handle only one client at a time
#
# With threads:
#
# Server can handle multiple clients at the same time
#
# Each client runs in its own execution path
#
# 4. What address contains
#
# From this line:
#
# client, address = serversocket.accept()
#
# address is a tuple:
# (address[0], address[1])
#
# It contains:
# Part	Meaning
# address[0]	Client IP address
# address[1]	Client port number
# Example:
# ('127.0.0.1', 54321)
#
# 5. What serversocket.accept() does
# client, address = serversocket.accept()
#
# This line:
#
# Waits until a client connects
#
# Then returns:
#
# Two things:
#
# client
# → A new socket for that client only
#
# address
# → The IP and port of that client
#
# Important:
#
# This is a blocking call
# The program pauses here until a client connects
#
# 6. Full Flow (Client–Server Reference Only)
# Server side:
#
# Server starts
#
# Server listens:
#
# serversocket.listen(5)
#
#
# Server waits:
#
# client, address = serversocket.accept()
#
#
# When client connects:
#
# Server creates a new thread
#
# Passes the client socket to:
#
# client_thread(client)
#
# Inside client_thread
#
# This part handles only one client:
#
# data = connection.recv(2048)
# connection.sendall(...)
#
#
# It continues until client disconnects.
#
# 7. Key Concept Summary
# Term	Meaning
# def	Defines a function
# connection	Client-specific socket
# start_new_thread	Runs a function in parallel
# address	Client IP + Port
# accept()	Waits for client and creates new socket


# 1. What start_new_thread is
# from _thread import *
#
#
# This line imports a function named:
#
# start_new_thread
#
# So:
#
# start_new_thread is a built-in Python function from the _thread module.
#
# Its job is:
#
# Run a function in a new thread (parallel execution)
#
# 2. Its general format (syntax)
# start_new_thread(function_name, arguments_tuple)
#
#
# It always takes two things:
#
# The function you want to run
#
# A tuple of arguments to pass to that function
#
# 3. What this means in your code
# start_new_thread(client_thread, (client,))
#
#
# Break it down:
#
# First part
# client_thread
#
#
# This is the function name
# You are NOT calling it here (no ()).
#
# You are passing the function itself.
#
# Second part
# (client,)
#
#
# This is a tuple
#
# Why the comma?
#
# In Python:
#
# (client)   # NOT a tuple, just client
# (client,)  # This IS a tuple with one item
#
#
# So you are creating:
#
# (client,)
#
#
# Which means:
#
# Pass client as the first argument to the function
#
# 4. What Python actually does internally
#
# This line:
#
# start_new_thread(client_thread, (client,))
#
#
# Is basically telling Python:
#
# Start a new thread and run this:
#
# client_thread(client)
#
#
# But run it in parallel, not in the main program.
#
# 5. How the argument reaches def
#
# Your function is defined as:
#
# def client_thread(connection):
#
#
# So when the thread starts, Python does:
#
# connection = client
#
#
# Now inside the function:
#
# connection is the same socket object as client
#
# You use it to send and receive data
#
# 6. Why function name has no ()
# This would be wrong:
# start_new_thread(client_thread(), (client,))
#
#
# Because:
#
# client_thread() runs the function immediately
#
# Then passes its return value (None) to the thread
#
# That breaks threading
#
# Correct:
# start_new_thread(client_thread, (client,))
#
#
# This passes the function itself, so the thread can run it.
#
# 7. Execution Flow (Step-by-Step)
# Server reaches:
# client, address = serversocket.accept()
#
#
# Then:
#
# start_new_thread(client_thread, (client,))
#
# What happens:
#
# Python creates a new thread
#
# That thread runs:
#
# client_thread(client)
#
#
# Main program does not wait
#
# Main program goes back to:
#
# serversocket.accept()
#
#
# and waits for another client
#
# 8. Very Short Summary
# Part	Meaning
# start_new_thread	Function that starts a new thread
# client_thread	Function to run in thread
# (client,)	Tuple of arguments
# Result	Runs client_thread(client) in parallel

#------------------------------------------------------
# send() vs sendall()
# 1️⃣ send()
# What It Does
# connection.send(data)
#
#
# Tries to send data once
#
# May send only part of the bytes
#
# Returns how many bytes were actually sent
#
# Example
# bytes_sent = connection.send(b"Hello Server")
# print(bytes_sent)
#
# What Can Happen
#
# If your message is large or the network buffer is full:
#
# Only part of the message is sent
#
# So the receiver might get:
#
# "Hello"
#
#
# Instead of:
#
# "Hello Server"
#
# 2️⃣ sendall()
# What It Does
# connection.sendall(data)
#
#
# Keeps sending until all bytes are sent
#
# Does not return number of bytes
#
# Blocks (waits) until complete or error
#
# Key Difference Table
# Feature	send()	sendall()
# Sends full message	❌ Not guaranteed	✅ Guaranteed
# Returns value	✅ Bytes sent	❌ None
# Needs loop for full send	✅ Yes	❌ No
# Best for	Low-level control	Normal client-server apps
# Why This Matters in Client–Server Code
# Using send() Safely
#
# You must do this:
#
# total_sent = 0
# while total_sent < len(data):
#     sent = connection.send(data[total_sent:])
#     total_sent += sent
#
# Using sendall() Safely
#
# Just:
#
# connection.sendall(data)
#
# What Professionals Use
#
# In most client-server programs, people use:
#
# sendall()
#
#
# Because:
#
# It guarantees the full message reaches the other side
#
# One-Line Summary (Interview Ready)
#
# send() may transmit only part of the data and returns how many bytes were sent, while sendall() keeps sending until the entire message is delivered or an error occurs.
#
# Example in Your Server Context
# connection.sendall("welcome to the server".encode("utf-8"))
#
#
# This ensures the client always receives the full welcome message.
#
# If you want, I can explain why partial sends happen at OS buffer and TCP level — that’s a strong networking interview topic.


#---------------------------------listen
# It means 5 clients can wait in line to be accepted.
#
# What listen(5) Actually Means
# serversocket.listen(5)
#
# 5 = Backlog
#
# It is the maximum number of incoming client connections that can sit in the waiting queue
# before your server calls accept().
#
# Client–Server Flow
# 1. Client calls connect()
#
# The OS puts the client into the pending connection queue
#
# 2. Server calls accept()
#
# The server takes one client from the queue and starts talking to it
#
# What the Number 5 Controls
# Waiting Queue (Backlog)
# [ Client1 ][ Client2 ][ Client3 ][ Client4 ][ Client5 ]
#
#
# These clients are not being served yet
#
# They are just waiting for the server to call accept()
#
# What Happens to the 6th Client?
#
# If the queue is full:
#
# The OS may reject the connection
#
# Or the client will hang / timeout