import socket
from threading import Thread

from Globals import states

clients = []


def create_server(port: int, host: str = ""):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    return server_socket


def start_server(server_socket: socket.socket):
    while True:
        server_socket.listen()

        connection, _ = server_socket.accept()

        print(f"Connected to client {connection}")
        clients.append(connection)

        # A thread per client
        Thread(target=handle_connection, args=(connection,), daemon=True).start()


def handle_connection(connection: socket.socket):
    states.GAME_STARTED = True
    while True:
        data = connection.recv(1024)
        if not data:
            break

        connection.sendall(data)
