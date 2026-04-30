import json
import socket

from Globals import states
from Systems import BoardManager, GameStateManager

# Data Managed by server
id_on_server = -1
can_play = False  # Is the Clients turn

connected_players = 0
ready_players = []  # Store ID of players that are ready


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
    global id_on_server, connected_players, ready_players, can_play

    data = json.loads(packet)

    match data["type"]:
        case "play":
            cell_id = BoardManager.get_cell_id_at(tuple(data["coord"]))
            BoardManager.play_move_at(states.UI, data["char"], cell_id)
            BoardManager.update_text_colors(states.UI)
        case "roster":
            id_on_server = data["id"]
            connected_players = data["players"]
            ready_players = data["ready_players"]

            states.id_on_server = id_on_server
        case "ready":
            ready_players = data["all"]
        case "start_game":
            GameStateManager.change_state_to("GAME")
        case "turn":
            can_play = data["current"] == id_on_server


def prompt_ready(client: socket.socket):
    data = {"type": "prompt", "prompt": "ready", "id": id_on_server}
    packet = json.dumps(data).encode()
    client.sendall(packet)
