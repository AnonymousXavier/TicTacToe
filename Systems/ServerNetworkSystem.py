import json
import socket
from threading import Thread

clients: list[socket.socket] = []


def create_server(port: int, host: str = ""):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    return server_socket


def start_server(server_socket: socket.socket):
    while True:
        server_socket.listen()
        connection, _ = server_socket.accept()

        print(f"Connected to client {len(clients)}")
        clients.append(connection)
        send_join_data_to_everyone()

        # A thread per client
        Thread(target=handle_connection, args=(connection,), daemon=True).start()


def handle_connection(connection: socket.socket):
    while True:
        packet = connection.recv(1024)

        if not packet:
            break

        send_packet_to_everyone(packet)


def send_join_data_to_everyone():
    for i, client in enumerate(clients):
        roster_data = {"players": len(clients), "id": i, "type": "roster"}
        roster_packet = json.dumps(roster_data).encode()

        client.send(roster_packet)


def send_packet_to_everyone(packet: bytes):
    for client in clients:
        client.send(packet)
