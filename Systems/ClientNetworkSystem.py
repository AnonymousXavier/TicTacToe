import socket


def create_client(host: str, port: int):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print(f"Connected to {host} on {port}")

    return client_socket
