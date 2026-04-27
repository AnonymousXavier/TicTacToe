import json
import socket
from threading import Thread

from Globals import states
from Systems import BoardManager, GameStateManager

clients = []


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
        else:
            data = json.loads(packet)
            if data["type"] == "play":
                cell_id = BoardManager.get_cell_id_at(tuple(data["coord"]))
                BoardManager.play_move_at(states.UI, data["char"], cell_id)
