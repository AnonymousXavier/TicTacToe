import pygame

from Globals import states
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

        if element[ClickComponent].action == "retry":
            if rect.collidepoint(mouse_pos) and clicked:
                add_action_to_event(element_id, "retry", events)

        if states.CURRENT_STATE == "OVER":
            continue

        if rect.collidepoint(mouse_pos) and clicked:
            add_action_to_event(element_id, element[ClickComponent].action, events)


def add_action_to_event(element_id: int, action: str, events: list):
    click_event = {
        "type": "click",
        "action": action,
        "id": element_id,
    }
    events.append(click_event)
