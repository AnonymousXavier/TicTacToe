from typing import Literal

RUNNING = True
NEXT_ENTITY_ID = 1


UI = {}
STATES_LITERAL = Literal["MENU", "LOBBY", "GAME", "OVER"]

CURRENT_STATE: STATES_LITERAL = "MENU"

is_hosting: bool = False
id_on_server: int = -1  # Avoids circular imports


draw = False
current_turn = 0
won = False
can_play = False


def reset():
    global draw, won, current_turn, can_play

    draw = False
    won = False
    can_play = False
    current_turn = 0

    # Buf if youre the host, play first
    if is_hosting:
        can_play = True
