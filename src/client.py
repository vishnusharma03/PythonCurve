import socket
import threading


nick = input("Enter your Nickname!").encode()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 61562))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == "Send me your Nickname!":
                client.send(nick)
            else:
                print(message)

        except:
            print("Closing the connection due to an error!")
            client.close()
            break

def write():
    while True:
        message = f"{nick} : {input("what do you want to send?")}".encode()
        client.send(message)


rThread = threading.Thread(target=receive)
rThread.start()

wThread = threading.Thread(target=write)
wThread.start()

