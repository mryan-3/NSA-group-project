# Client 

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))
while True:
    message = input("Enter Message: ")
    client_socket.send(message.encode())
    message = client_socket.recv(1024).decode()
    print(f"Received {message}")
    if message == "Spam Message, disconneting from server":
      break
client_socket.close()

