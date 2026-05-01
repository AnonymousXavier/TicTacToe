from Builders.MainMenuBuilder import MainMenuBuilder
from Globals import Misc, settings, states
from Globals.Components import EditTextComponent, TextComponent
from Systems import (
    BoardManager,
    ClientNetworkSystem,
    GameStateManager,
    ServerNetworkSystem,
)
from Systems.NetworkManagingSystem import NetworkManagingSystem

delay_frames_left_for_event = {}  # dont process an event if the time here isnt 0


def process(ui: dict, events: list):
    for event in events:
        if event["type"] == "click":
            handle_click_events(ui, event)

        if event["type"] == "start_game":
            GameStateManager.change_state_to("GAME")

    event_delays_completed = []
    for event_name, frames_left in delay_frames_left_for_event.items():
        if frames_left <= 0:
            event_delays_completed.append(event_name)
        else:
            delay_frames_left_for_event[event_name] -= 1

    for event_name in event_delays_completed:
        del delay_frames_left_for_event[event_name]


def handle_click_events(ui: dict, event: dict):
    match event["action"]:
        case "host":
            NetworkManagingSystem.host_game(Misc.get_ip_address())
            NetworkManagingSystem.join_game(Misc.get_ip_address())
            GameStateManager.change_state_to("MENU")
        case "join":
            GameStateManager.change_state_to("MENU")
        case "edit_text":
            ui[event["id"]][EditTextComponent].editing = True

        case "join_lobby":
            if states.CURRENT_STATE == "LOBBY":
                return

            # Fetch IP from textbox
            text_box = ui[MainMenuBuilder.server_ip_textbox_id]
            server_ip = text_box[TextComponent].text
            # Dont forget to remove the | in case it has it
            server_ip = (  # Itll always be the last character if it exists
                Misc.remove_last_character_of(server_ip)
                if "|" in server_ip
                else server_ip
            )

            NetworkManagingSystem.join_game(server_ip)
            GameStateManager.change_state_to("LOBBY")

        case "play_move":
            # Only Play if its your turn
            if not states.can_play:
                return

            # To avoid spamming the server
            if "play_move" in delay_frames_left_for_event:
                return

            char = Misc.get_move_char()
            BoardManager.play_move_at(ui, char, event["id"])

            coord = BoardManager.get_coord_of(event["id"])
            NetworkManagingSystem.sync_played_move(coord, char)

            BoardManager.update_board(ui)

            delay_frames_left_for_event["play_move"] = int(
                settings.UPDATE.FPS * 0.5
            )  # 1/2 sec

            BoardManager.process(ui, char)

        case "toggle_ready":
            ClientNetworkSystem.prompt_ready(NetworkManagingSystem.client)

        case "start_game":
            ServerNetworkSystem.tell_everyone_start_game()  # Then each client sends the event

        case "retry":
            GameStateManager.change_state_to("GAME")
