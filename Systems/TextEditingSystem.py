import pygame

from Globals import Misc
from Globals.Components import EditTextComponent, TextComponent


def process(ui: dict, event: pygame.Event):
    for element in ui.values():
        if EditTextComponent not in element:
            continue

        if not element[EditTextComponent].editing:
            continue

        if event.type != pygame.KEYDOWN:
            continue

        # Text Editing
        if event.key == pygame.K_BACKSPACE:
            text = element[TextComponent].text
            element[TextComponent].text = Misc.remove_last_character_of(text)
        else:
            char = event.unicode
            if char in "0123456789.":
                element[TextComponent].text += char
