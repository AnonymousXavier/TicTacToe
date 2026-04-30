import json
from threading import Thread

from Globals import settings, states
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

        states.is_hosting = True

    @classmethod
    def join_game(cls, ip: str):
        if cls.client_created:
            return

        print("Client Socket Created")

        cls.client = ClientNetworkSystem.create_client(ip, settings.UPDATE.PORT)
        Thread(
            target=ClientNetworkSystem.connect_to_server,
            args=(cls.client,),
            daemon=True,
        ).start()

        cls.client_created = True

    @classmethod
    def sync_played_move(cls, coord: tuple, char: str):
        data = {"type": "play", "coord": coord, "char": char}
        packet = json.dumps(data).encode()

        cls.client.sendall(packet)

        # Force them to be unable to play After
        ClientNetworkSystem.can_play = False

    @classmethod
    def process(cls):
        pass
