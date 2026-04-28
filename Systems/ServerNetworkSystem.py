import socket
from threading import Thread

from Systems import GameStateManager

clients: list[socket.socket] = []


def create_server(port: int, host: str = ""):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    return server_socket


def start_server(server_socket: socket.socket):
    while True:
        server_socket.listen()

        connection, _ = server_socket.accept()

        print("Connected to client")
        clients.append(connection)

        # A thread per client
        Thread(target=handle_connection, args=(connection,), daemon=True).start()


def handle_connection(connection: socket.socket):
    GameStateManager.change_state_to("GAME")
    while True:
        packet = connection.recv(1024)

        if not packet:
            break

        send_recieved_packet_to_everyone(packet)


def send_recieved_packet_to_everyone(packet: bytes):
    for client in clients:
        client.send(packet)
