import pygame

from Globals import Factories, Misc, settings


class GameHUDBuilder:
    @classmethod
    def build(cls, ui: dict):
        ww, wh = settings.WINDOW.SIZE
        ulw, slw, tlw = (
            settings.GAME_UI.USERNAME_LABEL_WIDTH,
            settings.GAME_UI.SCORE_LABEL_WIDTH,
            settings.GAME_UI.TURN_LABEL_WIDTH,
        )
        lh = settings.GAME_UI.LABEL_HEIGHT

        username_label_rect = pygame.Rect(0, 0, ulw, lh)
        turn_label_rect = pygame.Rect((ww - tlw) / 2, wh - lh, tlw, lh)
        score_label_rect = pygame.Rect(ulw, 0, slw, lh)

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

        cls.score_label_id = Factories.create_label(
            ui=ui,
            text="0:0",
            rect=score_label_rect,
            text_color=font_color,
            font_size=settings.GAME_UI.FONT_SIZE,
        )

        cls.turn_label_id = Factories.create_label(
            ui=ui,
            rect=turn_label_rect,
            text="X's Turn",
            text_color=font_color,
            font_size=settings.GAME_UI.FONT_SIZE,
        )

    @classmethod
    def draw_overlay(cls, ui: dict, message: str, color: tuple, font_size: int):
        ww, wh = settings.WINDOW.SIZE
        bw, bh = ww * 0.2, wh * 0.1
        cls.overlap_id = Factories.create_label(
            ui, pygame.Rect(0, 0, ww, wh), message, color, font_size
        )
        cls.retry_btn = Factories.create_button(
            ui,
            pygame.Rect((ww - bw) / 2, (wh - bh) / 2 + bh, bw, bh),
            "RETRY",
            settings.MAINMENU_UI.BUTTON_NORMAL_COLOR,
            settings.MAINMENU_UI.BUTTON_HOVERED_COLOR,
            settings.MAINMENU_UI.TEXT_COLOR,
            settings.MAINMENU_UI.BUTTONS_FONT_SIZE,
            "retry",
        )

    @classmethod
    def destroy(cls, ui: dict):
        del ui[cls.overlap_id]
        del ui[cls.score_label_id]
        del ui[cls.turn_label_id]
        del ui[cls.username_label_id]
        del ui[cls.retry_btn]
