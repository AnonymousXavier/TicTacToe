from typing import Literal

RUNNING = True
NEXT_ENTITY_ID = 1


UI = {}
STATES_LITERAL = Literal["MENU", "LOBBY", "GAME"]

CURRENT_STATE: STATES_LITERAL = "MENU"

is_hosting: bool = False
id_on_server: int = -1  # Avoids circular imports
