# Server
import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9999))
server_socket.listen(4) 

print("""<<<GLOBAL CHAT>>>>>""")
blcked_users = []
def handle_client(client_socket,addr):
    while True:
        message = client_socket.recv(1024).decode()
        print(f"Received {message} from client")
        if message.lower() == 'spam':
          message = "Spam Message, disconneting from server"
          blcked_users.append(addr)
        else:
          message = input("Enter message to send: ")
        client_socket.send(message.encode())

while True:
    client_socket, address = server_socket.accept()
    if address in blcked_users:
      client_socket.send('Connection abort: Reason banned'.encode())
      break
    print(f'Got connection from {address}')
    client_handler = threading.Thread(
        target=handle_client, args=(client_socket,address))
    client_handler.start()

