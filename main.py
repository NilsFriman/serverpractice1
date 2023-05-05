import socket
import threading


host = socket.gethostbyname(socket.gethostname())
port = 52000



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()

