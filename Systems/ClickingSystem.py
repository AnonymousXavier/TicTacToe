import pygame

from Globals.Components import ClickComponent, EditTextComponent, SpatialComponent


def process(ui: dict, events: list):
    for element_id, element in ui.items():
        if ClickComponent not in element or SpatialComponent not in element:
            continue

        if EditTextComponent in element:
            element[EditTextComponent].editing = False

        mouse_pos = pygame.mouse.get_pos()
        rect: pygame.Rect = element[SpatialComponent].rect
        clicked = pygame.mouse.get_pressed()[0]

        if rect.collidepoint(mouse_pos) and clicked:
            click_event = {
                "type": "click",
                "action": element[ClickComponent].action,
                "id": element_id,
            }
            events.append(click_event)
