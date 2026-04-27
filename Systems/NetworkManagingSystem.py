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

        Thread(
            target=ClientNetworkSystem.connect_to_server,
            args=(cls.client,),
            daemon=True,
        ).start()
        cls.client_created = True
