import threading
import socket

host = '127.0.0.1'
port = 61562

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))

server.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat.".encode())
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected to server {address}")

        client.send("Send me your Nickname!".encode())
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Connected to {nickname}")
        broadcast(f"{nickname} joined the chat".encode())
        client.send("Connected to serverX!".encode())

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("ServerX is online!")
receive()
