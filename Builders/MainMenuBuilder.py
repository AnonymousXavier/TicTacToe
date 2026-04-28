import pygame

from Globals import Factories, Misc, settings


class MainMenuBuilder:
    @classmethod
    def build(cls, ui: dict):
        ww, wh = settings.WINDOW.SIZE
        bw, bh = settings.MAINMENU_UI.BUTTON_SIZE

        # ------------------- ADD ELEMENTS
        # LABEL
        tw, th = settings.MAINMENU_UI.LABEL_SIZE
        title_label_rect = pygame.Rect((ww - tw) // 2, 0, tw, th)
        ip_label_rect = pygame.Rect((ww - bw) // 2, wh * 0.5, bw, bh)

        cls.title_label_id = Factories.create_label(
            ui,
            title_label_rect,
            "Tic Tac Toe".upper(),
            settings.MAINMENU_UI.TEXT_COLOR,
            settings.MAINMENU_UI.TITLE_LABEL_FONT_SIZE,
        )

        cls.ip_label_id = Factories.create_label(
            ui,
            ip_label_rect,
            str(Misc.get_ip_address()),
            settings.MAINMENU_UI.TEXT_COLOR,
            settings.MAINMENU_UI.BUTTONS_FONT_SIZE,
        )

        # BUTTONS

        text_rect = Misc.get_position_rect_of(  # Position it exactly at beloe the ip address label
            str(Misc.get_ip_address()),
            settings.MAINMENU_UI.BUTTONS_FONT_SIZE,
            ip_label_rect,
        )
        bottom = text_rect.bottom
        remaining_h = wh - bottom

        spacing = remaining_h // 3

        host_btn_rect = pygame.Rect((ww - bw) // 2, bottom, bw, bh)
        join_btn_rect = pygame.Rect((ww - bw) // 2, bottom + spacing, bw, bh)

        cls.host_btn_id = Factories.create_button(
            ui,
            host_btn_rect,
            "HOST",
            settings.MAINMENU_UI.BUTTON_NORMAL_COLOR,
            settings.MAINMENU_UI.BUTTON_HOVERED_COLOR,
            settings.MAINMENU_UI.TEXT_COLOR,
            settings.MAINMENU_UI.BUTTONS_FONT_SIZE,
            action="host",
        )

        cls.join_btn_id = Factories.create_button(
            ui,
            join_btn_rect,
            "JOIN",
            settings.MAINMENU_UI.BUTTON_NORMAL_COLOR,
            settings.MAINMENU_UI.BUTTON_HOVERED_COLOR,
            settings.MAINMENU_UI.TEXT_COLOR,
            settings.MAINMENU_UI.BUTTONS_FONT_SIZE,
            action="join",
        )

    @classmethod
    def destroy_main_maneu(cls, ui: dict):
        del ui[cls.join_btn_id]
        del ui[cls.host_btn_id]
        del ui[cls.title_label_id]
        del ui[cls.ip_label_id]

    @classmethod
    def destroy_host_menu(cls, ui: dict):
        del ui[cls.host_hint_id]

    @classmethod
    def destroy_join_menu(cls, ui: dict):
        del ui[cls.join_hint_id]
        del ui[cls.server_ip_textbox_id]
        del ui[cls.join_game_btn_id]

    @classmethod
    def build_host_menu(cls, ui: dict):
        ww, wh = settings.WINDOW.SIZE
        tw, th = settings.MAINMENU_UI.LABEL_SIZE
        hint_label_rect = pygame.Rect((ww - tw) // 2, (wh - th) // 2, tw, th)

        cls.destroy_main_maneu(ui)
        cls.host_hint_id = Factories.create_label(
            ui,
            hint_label_rect,
            f"   Waiting for a \n player to join on \n    {Misc.get_ip_address()}".upper(),
            settings.MAINMENU_UI.TEXT_COLOR,
            settings.MAINMENU_UI.TITLE_LABEL_FONT_SIZE,
        )

    @classmethod
    def build_join_menu(cls, ui: dict):
        ww, wh = settings.WINDOW.SIZE
        tw, th = settings.MAINMENU_UI.LABEL_SIZE
        bw, bh = settings.MAINMENU_UI.BUTTON_SIZE

        title_label_rect = pygame.Rect(
            (ww - tw) // 2, (wh - th) // 2 - (th + bh // 2), tw, th
        )
        server_ip_textbox_rect = pygame.Rect(
            (ww - tw) // 2, title_label_rect.bottom + th // 2, tw, bh
        )
        join_btn_rect = pygame.Rect(
            (ww - bw) // 2, server_ip_textbox_rect.bottom + bh // 2, bw, bh
        )

        cls.destroy_main_maneu(ui)

        cls.join_hint_id = Factories.create_label(
            ui,
            title_label_rect,
            "Connect to Host with IP".upper(),
            settings.MAINMENU_UI.TEXT_COLOR,
            settings.MAINMENU_UI.TITLE_LABEL_FONT_SIZE,
        )
        cls.server_ip_textbox_id = Factories.create_textbox(
            ui,
            server_ip_textbox_rect,
            text=f"{Misc.get_ip_address()}",
            bg_color=settings.COLOURS.BLACK,
            hovered_color=settings.COLOURS.GREY,
            text_color=settings.COLOURS.WHITE,
            font_size=settings.MAINMENU_UI.BUTTONS_FONT_SIZE,
            action="edit_text",
        )
        cls.join_game_btn_id = Factories.create_button(
            ui,
            join_btn_rect,
            "JOIN",
            settings.MAINMENU_UI.BUTTON_NORMAL_COLOR,
            settings.MAINMENU_UI.BUTTON_HOVERED_COLOR,
            settings.MAINMENU_UI.TEXT_COLOR,
            settings.MAINMENU_UI.BUTTONS_FONT_SIZE,
            action="join_lobby",
        )
