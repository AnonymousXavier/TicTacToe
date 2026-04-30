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

        cls.ip_label = Factories.create_label(
            ui,
            pygame.Rect((ww - tw) / 2, th, tw, th // 2),
            f"IP: {Misc.get_ip_address()}",
            settings.LOBBY_UI.TEXT_COLOR,
            20,
        )

        cls.add_joined_players(ui)

    @classmethod
    def delete_joined_players(cls, ui: dict):
        for label_id in cls.connected_players_labels:
            if label_id in ui:
                del ui[label_id]

    @classmethod
    def update_joined_player(cls, ui: dict):
        cls.delete_joined_players(ui)
        cls.add_joined_players(ui)

    @classmethod
    def add_joined_players(cls, ui: dict):
        ww = settings.WINDOW.WIDTH
        pw, ph = (
            settings.LOBBY_UI.CONNECTED_PLAYERS_LABEL_WIDTH,
            settings.LOBBY_UI.CONNECTED_PLAYERS_LABEL_HEIGHT,
        )
        th = settings.LOBBY_UI.TITLE_LABEL_HEIGHT

        y = th * 1.4
        for i in range(ClientNetworkSystem.connected_players):
            rect = pygame.Rect((ww - pw) / 2, y, pw, ph)

            if i == ClientNetworkSystem.id_on_server:
                text = " (YOU) "  # Just sm personalization
            else:
                text = "       "  # For Consistency in layout

            border_color = (
                settings.COLOURS.GREEN
                if i in ClientNetworkSystem.ready_players
                else settings.COLOURS.RED
            )

            text += settings.BOARD.CHARS[i]
            label_id = Factories.create_label(
                ui,
                rect,
                text,
                settings.LOBBY_UI.TEXT_COLOR,
                settings.LOBBY_UI.TITLE_FONT_SIZE,
                border_color,
                border_size=1,
            )

            cls.connected_players_labels.append(label_id)

            y += ph

    @classmethod
    def destroy(cls, ui: dict):
        del ui[cls.title_label]
        del ui[cls.ip_label]
        del ui[cls.start_game_btn]

        cls.delete_joined_players(ui)
