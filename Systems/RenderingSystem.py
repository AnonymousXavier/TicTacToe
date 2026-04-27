from Globals import Misc, settings
from Globals.Components import (
    BackgroundComponent,
    BorderComponent,
    EditTextComponent,
    SpatialComponent,
    TextComponent,
)
from Globals.settings import pygame

cursor_flash_frame_duration = 60

frame = 1


def process(ui: dict, surface: pygame.Surface):
    global frame

    for element in ui.values():
        if SpatialComponent not in element:
            continue

        # Render Backgrounds First
        if BackgroundComponent in element:
            pygame.draw.rect(
                surface,
                element[BackgroundComponent].color,
                element[SpatialComponent].rect,
            )

        # Render Text
        if TextComponent in element:
            font = pygame.font.SysFont(
                settings.UI.FONT_NAME, element[TextComponent].size, True
            )

            text_surface = font.render(
                element[TextComponent].text, True, element[TextComponent].color
            )

            text_rect = text_surface.get_rect(
                center=element[SpatialComponent].rect.center
            )

            surface.blit(text_surface, text_rect)

        # Render Backgrounds First
        if BorderComponent in element:
            pygame.draw.rect(
                surface,
                element[BorderComponent].color,
                element[SpatialComponent].rect,
                width=element[BorderComponent].size,
                border_radius=element[BorderComponent].radius,
            )

        # Add Flashes to Editable TextComponents
        if EditTextComponent in element:
            # Add a | at the end that flashes
            if (
                cursor_flash_frame_duration - frame <= cursor_flash_frame_duration / 2
            ):  # The last X frames, show the |
                if element[TextComponent].text[-1] != "|":
                    element[TextComponent].text += "|"

            else:
                if element[TextComponent].text[-1] == "|":
                    element[TextComponent].text = Misc.remove_last_character_of(
                        element[TextComponent].text
                    )

    frame += 1

    if frame > cursor_flash_frame_duration:
        frame = 0
