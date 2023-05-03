import socket
import pickle
import threading
import customtkinter


host = socket.gethostbyname(socket.gethostname())
port = 52000



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()

clients = []
names = []



def messages(msg):
    for client in clients:
        client.send(msg)


def client_handler(client):
    while True:
        try:
            message = client.recv(1024)
            messages(message)

        except Exception:
            index_of_client = clients.index(client)
            clients.remove(index_of_client)
            client.close()
            messages(f"{names[index_of_client]} Has left the chat".encode("utf-8"))
            names.remove(clients[index_of_client])
            break

            
            