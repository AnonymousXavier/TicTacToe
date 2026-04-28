from Builders.MainMenuBuilder import MainMenuBuilder
from Globals import settings, states
from Globals.settings import pygame
from Systems import (
    ClickingSystem,
    GameStateManager,
    HoverSystem,
    InputSystem,
    RenderingSystem,
    UISystem,
)


class Main:
    def __init__(self) -> None:
        self.window = pygame.display.set_mode(settings.WINDOW.SIZE)
        self.clock = pygame.Clock()
        MainMenuBuilder.build(states.UI)

    def update(self):
        self.clock.tick(settings.UPDATE.FPS)
        events = []

        GameStateManager.process()
        InputSystem.process()

        HoverSystem.process(states.UI)
        ClickingSystem.process(states.UI, events)

        UISystem.process(states.UI, events)
        pygame.display.update()

    def draw(self):
        self.window.fill(settings.COLOURS.BLACK)

        RenderingSystem.process(states.UI, self.window)

    def run(self):
        while states.RUNNING:
            self.update()
            self.draw()


Main().run()
