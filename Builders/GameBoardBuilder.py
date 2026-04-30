import pygame

from Globals import Factories, settings


class BoardBuilder:
    @classmethod
    def build(cls, ui: dict):
        cls.board_cells_ids = {}

        cw, ch, s = (
            settings.BOARD.CELL_WIDTH,
            settings.BOARD.CELL_HEIGHT,
            settings.BOARD.SPACING,
        )

        ox, oy = (
            settings.BOARD.SPACING / 2 + settings.BOARD.LEFT_PADDING,
            settings.GAME_UI.LABEL_HEIGHT + settings.BOARD.SPACING / 2,
        )

        for yi in range(settings.BOARD.ROWS):
            for xi in range(settings.BOARD.COLS):
                x, y = ox + xi * (cw + s), yi * (ch + s) + oy

                rect = pygame.Rect(x, y, cw, ch)

                cell_id = Factories.create_button(
                    ui,
                    rect,
                    " ",
                    settings.BOARD.CELL_NORMAL_COLOR,
                    settings.BOARD.CELL_HOVERED_COLOR,
                    settings.BOARD.CELL_TEXT_COLOR,
                    settings.BOARD.CELL_FONT_SIZE,
                    "play_move",
                    settings.BOARD.CELL_BORDER_COLOR,
                )

                cls.board_cells_ids[(xi, yi)] = cell_id
