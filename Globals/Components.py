from dataclasses import dataclass

import pygame


@dataclass(kw_only=True)
class TextComponent:
    text: str
    color: tuple
    size: int = 16


@dataclass(kw_only=True)
class ClickComponent:
    action: str


@dataclass(kw_only=True)
class HoverComponent:
    normal_color: tuple
    hovered_color: tuple


@dataclass(kw_only=True)
class SpatialComponent:
    rect: pygame.Rect


@dataclass(kw_only=True)
class BackgroundComponent:
    color: tuple


@dataclass(kw_only=True)
class BorderComponent:
    color: tuple
    size: int
    radius: int = 10


@dataclass(kw_only=True)
class EditTextComponent:
    editing: bool = False
