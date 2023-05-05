import socket
import pickle
import threading 


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = socket.gethostbyname(socket.gethostname())
server_port = 1234

server_socket.bind(("", server_port))
server_socket.listen()


clients = []
users = []
ipaddresses = []
names = []


def message_sender(nickname):
    for client in clients:
        client.send()

def connection():
    while True:
        conn, addr = server_socket.accept()
        conn.send(b"Your mom")
        print(f"connection frmo {addr}{conn}")

connection()