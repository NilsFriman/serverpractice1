import socket
import pickle
import threading




server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 1234
server_socket.bind((host, port))
server_socket.listen()


def connection():
    while True:
        conn, addr = server_socket.accept()
