from Globals import states
from Globals.settings import pygame
from Systems import TextEditingSystem


def process():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            states.RUNNING = False

        TextEditingSystem.process(states.UI, event)
