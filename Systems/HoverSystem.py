import pygame
from Globals.Components import BackgroundComponent, HoverComponent, SpatialComponent


def process(ui: dict):
    for element in ui.values():
        if SpatialComponent not in element:
            continue

        if HoverComponent in element:
            mouse_pos = pygame.mouse.get_pos()

            if element[SpatialComponent].rect.collidepoint(mouse_pos):
                element[BackgroundComponent].color = element[
                    HoverComponent
                ].hovered_color
            else:
                element[BackgroundComponent].color = element[
                    HoverComponent
                ].normal_color
