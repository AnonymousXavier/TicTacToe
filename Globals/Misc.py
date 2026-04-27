import socket

import pygame

from Globals import settings
from Systems.NetworkManagingSystem import NetworkManagingSystem


def get_ip_address():
    return socket.gethostbyname(socket.gethostname())


def get_position_rect_of(text: str, font_size, ref_rect: pygame.Rect):
    font = pygame.font.SysFont(settings.UI.FONT_NAME, font_size, True)
    text_surface = font.render(text, True, (0, 0, 0))

    return text_surface.get_rect(center=ref_rect.center)


def remove_last_character_of(text: str):
    return "".join([text[i] for i in range(len(text) - 1)])


def get_username():
    return "Player 1" if is_the_host() else "Player 2"


def is_the_host():
    return NetworkManagingSystem.server_created
