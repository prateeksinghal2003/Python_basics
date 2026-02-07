import socket

clientsocket = socket.socket()

host = "127.0.0.1"
port = 1233

print("waiting for connection")
try:
    clientsocket.connect((host, port))


    while True:
      Input = input("Say something: ")
      clientsocket.send(str.encode(Input))

      response = clientsocket.recv(1024)
      print(response.decode("utf-8"))

      more = input("Want to send more data to the server? (y/n): ").strip().lower()

      if more != 'y':
          break


except socket.error as e:
    print(str(e))

clientsocket.close()

#     What
#     socket.error
#     Is
#
#     socket.error is an exception
#
#
#     class from Python’s socket module.
#
#
#     It
#     represents
#     errors
#     related
#     to
#     networking, such as:
#
#     Server is not running
#
#     Connection
#     refused
#
#     Server
#     closed
#     the
#     connection
#
#     Network
#     cable / Wi - Fi
#     disconnected
#
#     Timeout
#
#     Your
#     Code
#     except socket.error as e:
#     print(str(e))
#
# Break
# It
# Down
# socket.error
#
# This
# means:
#
# Catch
# only
# errors
# that
# come
# from socket operations
#
# Examples
# of
# socket
# operations:
#
# connect()
#
# send()
#
# recv()
#
# bind()
#
# listen()
#
# accept()
#
# as e
#
# This
# means:
#
# Store
# the
# actual
# error
# message in variable
# e
#
# So if the
# OS
# says:
#
# Connection
# reset
# by
# peer
#
# It
# gets
# stored in e
#
# str(e)
#
# This
# converts
# the
# error
# object
# into
# a
# readable
# string
#
# Then:
#
# print(str(e))
#
# Shows
# the
# real
# network
# problem
# on
# screen





# 1. Purpose of This Code
#
# This is a TCP client.
# It:
#
# Connects to a TCP server
#
# Receives a welcome message
#
# Sends messages to the server
#
# Receives and prints server responses
#
# Repeats until stopped
#
# 2. Import and Socket Creation
# import socket
# clientsocket = socket.socket()
#
# What happens:
#
# Imports Python’s socket library
#
# Creates a TCP socket
#
# This socket will be used to communicate with the server
#
# Default:
#
# IPv4
#
# TCP protocol
#
# 3. Server Address
# host = "127.0.0.1"
# port = 1233
#
#
# This defines:
#
# Server IP
#
# Server Port
#
# The client will try to connect to a server running on this address.
#
# 4. Connect to Server
# print("waiting for connection")
# try:
#     clientsocket.connect((host, port))
# except socket.error as e:
#     print(str(e))
#
# What connect() does:
#
# Initiates a TCP connection to the server
#
# If server is running and listening:
#
# Connection is established
#
# If not:
#
# Raises an error
#
# 5. Receive Welcome Message
# Response = clientsocket.recv(1024)
# print(Response.decode("utf-8"))
#
# What happens:
#
# Client waits for data from server
#
# Server sends:
#
# "welcome to the server"
#
#
# Client receives it as bytes
#
# .decode() converts bytes to readable text
#
# 6. Send and Receive Loop
# while True:
#
#
# Client stays connected and continues communication.
#
# Send Data to Server
# Input = input("Say something: ")
# clientsocket.send(str.encode(Input))
#
# What happens:
#
# Takes user input
#
# Converts it to bytes
#
# Sends it to the server using the same TCP connection
#
# Receive Server Reply
# response = clientsocket.recv(1024)
# print(response.decode("utf-8"))
#
# What happens:
#
# Client waits for server’s response
#
# Server replies with:
#
# "Hello I am server <your_message>"
#
#
# Client prints it
#
# 7. Close Connection
# clientsocket.close()
#
#
# This:
#
# Terminates the TCP connection
#
# Frees network resources
#
# Note:
# This line will only run if you exit the loop (e.g., using Ctrl+C or adding a break condition).
#
# 8. Client–Server Flow
# Client Side
#
# Create socket
#
# Connect to server
#
# Receive welcome message
#
# Send message
#
# Receive reply
#
# Repeat
#
# Close connection
#
# Server Side (Reference)
#
# Server accepts connection
#
# Sends welcome message
#
# Receives client message
#
# Sends response
#
# Repeats for same client
#
# 9. Key Functions Summary
# Function	Role
# socket()	Creates TCP socket
# connect()	Connects to server
# send()	Sends data to server
# recv()	Receives data from server
# close()	Closes connection