import json
import socket


def create_client(host: str, port: int):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print(f"Connected to {host} on {port}")

    return client_socket


def send_packet(client: socket.socket, packet: dict):
    data = json.dumps(packet).encode()
    client.send(data)


def connect_to_server(client_socket: socket.socket):
    while True:
        packet = {"message": "Hello World"}

        send_packet(client_socket, packet)

        recieve_packet(client_socket)


def recieve_packet(client):
    data = client.recv(1024)

    return data
