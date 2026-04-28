import pygame

from Globals import Factories, Misc, settings


class LobbyBuilder:
    @classmethod
    def build(cls, ui: dict):
        ww, wh = settings.WINDOW.SIZE
        tw, th = (
            settings.LOBBY_UI.TITLE_LABEL_WIDTH,
            settings.LOBBY_UI.TITLE_LABEL_HEIGHT,
        )
        pw, ph = (
            settings.LOBBY_UI.CONNECTED_PLAYERS_LABEL_WIDTH,
            settings.LOBBY_UI.CONNECTED_PLAYERS_LABEL_HEIGHT,
        )

        bw, bh = settings.LOBBY_UI.START_GAME_BUTTON_WIDTH, lh

        title_label_rect = pygame.Rect((ww - tw) / 2, 0, tw, th)
        button_rect = pygame.Rect((ww - bw) / 2, (wh - bh), bw, bh)

        cls.title_label = Factories.create_label(
            ui,
            title_label_rect,
            "LOBBY",
            settings.LOBBY_UI.TEXT_COLOR,
            settings.LOBBY_UI.TITLE_FONT_SIZE,
            settings.LOBBY_UI.BORDER_COLOR,
        )

        start_btn_text = "Start Game" if Misc.is_the_host() else "Ready"
        start_btn_action = "start_game" if Misc.is_the_host() else "ready"
        cls.start_game_btn = Factories.create_button(
            ui,
            button_rect,
            start_btn_text,
            settings.MAINMENU_UI.BUTTON_NORMAL_COLOR,
            settings.MAINMENU_UI.BUTTON_HOVERED_COLOR,
            settings.LOBBY_UI.BORDER_COLOR,
            start_game_action,
            settings.LOBBY_UI.BUTTON_FONT_SIZE,
        )
