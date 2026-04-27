from Builders.GameHUD import GameHUDBuilder
from Builders.MainMenuBuilder import MainMenuBuilder
from Globals import Misc, states
from Globals.Components import EditTextComponent, TextComponent
from Systems.NetworkManagingSystem import NetworkManagingSystem


def process(ui: dict, events: list):
    for event in events:
        if event["type"] == "click":
            handle_click_events(ui, event)

        if event["type"] == "start_game":
            print("Started Game")

            if Misc.is_the_host():
                MainMenuBuilder.destroy_host_menu(ui)
            else:
                MainMenuBuilder.destroy_join_menu(ui)

            GameHUDBuilder.build(ui)


def handle_click_events(ui: dict, event: dict):
    match event["action"]:
        case "host":
            NetworkManagingSystem.host_game(Misc.get_ip_address())
            MainMenuBuilder.build_host_menu(states.UI)
        case "join":
            MainMenuBuilder.build_join_menu(states.UI)
        case "edit_text":
            ui[event["id"]][EditTextComponent].editing = True
        case "join_game":
            if states.GAME_STARTED:
                return

            # Fetch IP from textbox
            text_box = ui[MainMenuBuilder.server_ip_textbox_id]
            server_ip = text_box[TextComponent].text
            # Dont forget to remove the | in case it has it
            server_ip = (
                Misc.remove_last_character_of(server_ip)
                if "|" in server_ip
                else server_ip
            )

            NetworkManagingSystem.join_game(server_ip)
            states.GAME_STARTED = True
