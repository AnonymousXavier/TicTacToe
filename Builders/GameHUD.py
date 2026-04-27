import pygame

from Globals import Factories, Misc, settings


class GameHUDBuilder:
    @classmethod
    def build(cls, ui: dict):
        ww, wh = settings.WINDOW.SIZE
        ulw, slw = (
            settings.GAME_UI.USERNAME_LABEL_WIDTH,
            settings.GAME_UI.SCORE_LABEL_WIDTH,
        )
        lh = settings.GAME_UI.LABEL_HEIGHT
        m = settings.GAME_UI.MARGIN

        username_label_rect = pygame.Rect((ww - ulw) // 2 + m, m, ulw, lh)
        username = Misc.get_username()
        font_color = (
            settings.COLOURS.RED if Misc.is_the_host() else settings.COLOURS.BLUE
        )

        cls.username_label_id = Factories.create_label(
            ui=ui,
            rect=username_label_rect,
            text=username,
            text_color=font_color,
            font_size=settings.GAME_UI.FONT_SIZE,
        )
