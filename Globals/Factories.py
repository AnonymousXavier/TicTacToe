import pygame

from Globals import states
from Globals.Components import (
    BackgroundComponent,
    BorderComponent,
    ClickComponent,
    EditTextComponent,
    HoverComponent,
    SpatialComponent,
    TextComponent,
)


def create_label(
    ui: dict,
    rect: pygame.Rect,
    text: str,
    text_color: tuple,
    font_size: int,
    border_color=None,
    border_size=3,
):
    label_id = states.NEXT_ENTITY_ID

    label = {
        SpatialComponent: SpatialComponent(rect=rect),
        TextComponent: TextComponent(text=text, color=text_color, size=font_size),
    }
    if border_color:
        label[BorderComponent] = BorderComponent(color=border_color, size=border_size)

    ui[label_id] = label

    states.NEXT_ENTITY_ID += 1

    return label_id


def create_button(
    ui: dict,
    rect: pygame.Rect,
    text: str,
    bg_color: tuple,
    hovered_color: tuple,
    text_color: tuple,
    font_size: int,
    action: str,
    border_color: tuple = (255, 255, 0),
):
    btn_id = states.NEXT_ENTITY_ID

    btn = {
        SpatialComponent: SpatialComponent(rect=rect),
        BackgroundComponent: BackgroundComponent(color=bg_color),
        ClickComponent: ClickComponent(action=action),
        TextComponent: TextComponent(text=text, color=text_color, size=font_size),
        BorderComponent: BorderComponent(size=2, color=border_color),
        HoverComponent: HoverComponent(
            hovered_color=hovered_color, normal_color=bg_color
        ),
    }

    ui[btn_id] = btn

    states.NEXT_ENTITY_ID += 1

    return btn_id


def create_textbox(
    ui: dict,
    rect: pygame.Rect,
    text: str,
    bg_color: tuple,
    hovered_color: tuple,
    text_color: tuple,
    font_size: int,
    action: str,
    border_color: tuple = (255, 255, 0),
):
    textComp_id = states.NEXT_ENTITY_ID

    textComp = {
        SpatialComponent: SpatialComponent(rect=rect),
        BackgroundComponent: BackgroundComponent(color=bg_color),
        ClickComponent: ClickComponent(action=action),
        TextComponent: TextComponent(text=text, color=text_color, size=font_size),
        BorderComponent: BorderComponent(size=2, color=border_color),
        HoverComponent: HoverComponent(
            hovered_color=hovered_color, normal_color=bg_color
        ),
        EditTextComponent: EditTextComponent(),
    }

    ui[textComp_id] = textComp

    states.NEXT_ENTITY_ID += 1

    return textComp_id
