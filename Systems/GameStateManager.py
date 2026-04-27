from Globals import states


def change_state_to(new_state: states.STATES_LITERAL):
    states.CURRENT_STATE = new_state
