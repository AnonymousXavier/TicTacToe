import json
import socket
from threading import Thread

clients: list[socket.socket] = []
ready_players = []


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

        manage_sent_packets(packet)
        send_to_everyone(packet)


def manage_sent_packets(packet: byte):
    global ready_players
    data = json.loads(packet)

    match data["type"]:
        case "prompt":
            if data["prompt"] == "ready":
                ready_players.append(data["id"])
                ready_players = list(
                    set(ready_players)
                )  # In case we recieve duplicates
                send_ready_players_to_everyone()


def send_ready_players_to_everyone():
    ready_players_data = {"type": "ready", "all": ready_players}

    send_to_everyone(ready_players_data)


def send_join_data_to_everyone():
    for i, client in enumerate(clients):
        roster_data = {
            "players": len(clients),
            "id": i,
            "type": "roster",
            "ready_players": ready_players,
        }
        roster_packet = json.dumps(roster_data).encode()

        client.send(roster_packet)


def tell_everyone_start_game():
    data = {"type": "start_game"}
    send_to_everyone(data)


def send_to_everyone(data: dict | bytes):
    if type(data) == dict:
        packet = json.dumps(data).encode()
    else:
        packet = data

    for client in clients:
        client.send(packet)
