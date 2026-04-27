from Builders.MainMenuBuilder import MainMenuBuilder
from Globals import settings, states
from Globals.settings import pygame
from Systems import ClickingSystem, HoverSystem, InputSystem, RenderingSystem, UISystem

game_started_prev_frame = False


class Main:
    def __init__(self) -> None:
        self.window = pygame.display.set_mode(settings.WINDOW.SIZE)
        self.clock = pygame.Clock()
        MainMenuBuilder.build(states.UI)

    def update(self):
        global game_started_prev_frame
        self.clock.tick(settings.UPDATE.FPS)
        events = []

        if not game_started_prev_frame and states.CURRENT_STATE == "GAME":
            events.append({"type": "start_game"})
        game_started_prev_frame = states.CURRENT_STATE == "GAME"

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
