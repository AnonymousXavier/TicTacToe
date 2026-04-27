import json
from threading import Thread

from Globals import settings
from Systems import ClientNetworkSystem, ServerNetworkSystem


class NetworkManagingSystem:
    server_created = False
    client_created = False

    @classmethod
    def host_game(cls, ip: str = ""):
        if cls.server_created:
            return

        cls.server = ServerNetworkSystem.create_server(settings.UPDATE.PORT, ip)
        Thread(
            target=ServerNetworkSystem.start_server, args=(cls.server,), daemon=True
        ).start()

        cls.server_created = True

    @classmethod
    def join_game(cls, ip: str):
        if cls.client_created:
            return

        cls.client = ClientNetworkSystem.create_client(ip, settings.UPDATE.PORT)
        cls.client_created = True

    @classmethod
    def sync_played_move(cls, coord: tuple, char: str):
        data = {"type": "play", "coord": coord, "char": char}
        packet = json.dumps(data).encode()

        if cls.server_created:
            cls.server.sendall(packet)

        elif cls.client_created:
            cls.client.sendall(packet)
