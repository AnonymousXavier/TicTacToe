from Builders.GameBoardBuilder import BoardBuilder
from Builders.GameHUD import GameHUDBuilder
from Builders.LobbyBuilder import LobbyBuilder
from Builders.MainMenuBuilder import MainMenuBuilder
from Globals import Misc, settings, states
from Systems import ClientNetworkSystem, ServerNetworkSystem

has_joined_lobby = False
last_number_of_players = 0
ready_players = 0


def process():
    global has_joined_lobby, last_number_of_players, ready_players

    if not has_joined_lobby and len(
        ServerNetworkSystem.clients
    ):  # Atleast, the server has joined the game
        change_state_to("LOBBY")
        has_joined_lobby = True

    if states.CURRENT_STATE == "LOBBY":
        if (
            ClientNetworkSystem.connected_players != last_number_of_players
            or len(ClientNetworkSystem.ready_players) != ready_players
        ):
            LobbyBuilder.update_joined_player(states.UI)

            last_number_of_players = ClientNetworkSystem.connected_players
            ready_players = len(ClientNetworkSystem.ready_players)


def change_state_to(new_state: states.STATES_LITERAL):
    transition_to_next_state(states.UI, states.CURRENT_STATE, new_state)

    states.CURRENT_STATE = new_state


def transition_to_next_state(
    ui: dict, _from: states.STATES_LITERAL, _to: states.STATES_LITERAL
):
    # Destroy Old UI's elements
    if _from != _to:  # For Menu Changes, we dont want to delete it unnecesaryily
        match _from:
            case "MENU":
                if Misc.is_the_host():
                    MainMenuBuilder.destroy_host_menu(ui)
                else:
                    MainMenuBuilder.destroy_join_menu(ui)
            case "LOBBY":
                LobbyBuilder.destroy(ui)
            case "OVER":
                GameHUDBuilder.destroy(ui)
                states.reset()

    # Add New UI based on the target state
    init(ui, _to)


def init(ui: dict, _state: states.STATES_LITERAL):
    match _state:
        case "GAME":
            GameHUDBuilder.build(ui)
            BoardBuilder.build(ui)

        case "LOBBY":
            LobbyBuilder.build(ui)

        case "MENU":
            if Misc.is_the_host():
                MainMenuBuilder.build_host_menu(ui)
            else:
                MainMenuBuilder.build_join_menu(ui)
        case "OVER":
            if states.draw:
                message = "DRAW"
                color = settings.COLOURS.BLUE
            elif states.won:
                message = "YOU WON"
                color = settings.COLOURS.GREEN
            else:
                message = "YOU LOST"
                color = settings.COLOURS.RED

            GameHUDBuilder.draw_overlay(ui, message, color, 64)
