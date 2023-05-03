import socket
import threading
import customtkinter


host = socket.gethostbyname(socket.gethostname())
port = 52000



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()

clients = []
names = []



def send_message(msg):
    for client in clients:
        client.send(msg)


def client_handler(client):
    while True:
        try:
            message = client.recv(1024)
            send_message(message)

        except Exception:
            index_of_client = clients.index(client)
            clients.remove(index_of_client)
            client.close()
            send_message(f"{names[index_of_client]} Has left the chat".encode("utf-8"))
            names.remove(clients[index_of_client])
            break



def reciever():
    while True:
        print("Looking for connections ....")

        client, addr = s.accept()
        print(f"connecting to {str(addr)}")

        client.send(b"Welcome to the chat, what would you want your name to be?")
        name = client.recv(1024)

        names.append(name)
        clients.append(client)

        print(f"The name of this client is {name}")

        send_message(f"{name} has connected to the chat room".encode("utf-8"))
        client.send("You are now connected!".encode("utf-8"))

        thread = threading.Thread(target=client_handler, args=(client,))
        thread.start()
            
reciever()