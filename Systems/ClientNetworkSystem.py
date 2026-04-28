import json
import socket

from Globals import states
from Systems import BoardManager

id_on_server = -1
connected_players = 0


def create_client(host: str, port: int):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print(f"Connected to {host} on {port}")

    return client_socket


def connect_to_server(client: socket.socket):
    while True:
        packet = client.recv(1024)

        if not packet:
            break

        recieve_packet(packet)


def recieve_packet(packet: bytes):
    global id_on_server, connected_players

    data = json.loads(packet)

    match data["type"]:
        case "play":
            cell_id = BoardManager.get_cell_id_at(tuple(data["coord"]))
            BoardManager.play_move_at(states.UI, data["char"], cell_id)
            BoardManager.update_text_colors(states.UI)
        case "roster":
            print(packet)
            id_on_server = data["id"]
            connected_players = data["players"]

            print(
                f"My ID is {id_on_server} and there are {connected_players} ppl connected"
            )
