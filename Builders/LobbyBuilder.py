import pygame

from Globals import Factories, Misc, settings
from Systems import ClientNetworkSystem


class LobbyBuilder:
    connected_players_labels = []

    @classmethod
    def build(cls, ui: dict):
        ww, wh = settings.WINDOW.SIZE
        tw, th = (
            settings.LOBBY_UI.TITLE_LABEL_WIDTH,
            settings.LOBBY_UI.TITLE_LABEL_HEIGHT,
        )
        bw, bh = settings.LOBBY_UI.START_GAME_BUTTON_WIDTH, th

        # TITLE LABEL
        title_label_rect = pygame.Rect((ww - tw) / 2, 0, tw, th)
        cls.title_label = Factories.create_label(
            ui,
            title_label_rect,
            "LOBBY",
            settings.LOBBY_UI.TEXT_COLOR,
            settings.LOBBY_UI.TITLE_FONT_SIZE,
            settings.LOBBY_UI.BORDER_COLOR,
        )

        # START GAME BUTTON
        start_btn_text = "Start Game" if Misc.is_the_host() else "Ready"
        start_btn_action = "start_game" if Misc.is_the_host() else "toggle_ready"
        button_rect = pygame.Rect((ww - bw) / 2, (wh - bh), bw, bh)
        cls.start_game_btn = Factories.create_button(
            ui=ui,
            rect=button_rect,
            text=start_btn_text,
            text_color=settings.LOBBY_UI.TEXT_COLOR,
            bg_color=settings.MAINMENU_UI.BUTTON_NORMAL_COLOR,
            hovered_color=settings.MAINMENU_UI.BUTTON_HOVERED_COLOR,
            border_color=settings.LOBBY_UI.BORDER_COLOR,
            action=start_btn_action,
            font_size=settings.LOBBY_UI.BUTTON_FONT_SIZE,
        )

        cls.add_joined_players(ui)

    @classmethod
    def delete_joined_players(cls, ui: dict):
        for label_id in cls.connected_players_labels:
            del ui[label_id]

    @classmethod
    def update_joined_player(cls, ui: dict):
        try:
            cls.delete_joined_players(ui)
        except Exception as err:
            print(err)
        cls.add_joined_players(ui)

    @classmethod
    def add_joined_players(cls, ui: dict):
        ww = settings.WINDOW.WIDTH
        pw, ph = (
            settings.LOBBY_UI.CONNECTED_PLAYERS_LABEL_WIDTH,
            settings.LOBBY_UI.CONNECTED_PLAYERS_LABEL_HEIGHT,
        )
        th = settings.LOBBY_UI.TITLE_LABEL_HEIGHT

        y = th
        for i in range(ClientNetworkSystem.connected_players):
            text = settings.BOARD.CHARS[ClientNetworkSystem.id_on_server]
            rect = pygame.Rect((ww - pw) / 2, y, pw, ph)

            print(
                ClientNetworkSystem.connected_players, ClientNetworkSystem.id_on_server
            )

            if i == ClientNetworkSystem.id_on_server:
                text += " (YOU)"  # Just sm personalization

            label_id = Factories.create_label(
                ui,
                rect,
                text,
                settings.LOBBY_UI.TEXT_COLOR,
                settings.LOBBY_UI.TITLE_FONT_SIZE,
                settings.LOBBY_UI.BORDER_COLOR,
            )

            cls.connected_players_labels.append(label_id)

            y += ph

    @classmethod
    def destroy(cls, ui: dict):
        pass
