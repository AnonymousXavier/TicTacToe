from typing import Literal

RUNNING = True
NEXT_ENTITY_ID = 1


UI = {}
STATES_LITERAL = Literal["MENU", "GAME"]

CURRENT_STATE: STATES_LITERAL = "MENU"
is_hosting: bool = False
