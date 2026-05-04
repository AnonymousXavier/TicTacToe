from Builders.GameBoardBuilder import BoardBuilder
from Builders.GameHUD import GameHUDBuilder
from Globals import settings
from Globals.Components import TextComponent
from Systems import ClientNetworkSystem
from Systems.NetworkManagingSystem import NetworkManagingSystem


def update_text_colors(ui: dict):
    for cell_id in BoardBuilder.board_cells_ids.values():
        cell = ui[cell_id]

        if cell[TextComponent].text == "X":
            cell[TextComponent].color = settings.BOARD.X_TEXT_COLOR
        elif cell[TextComponent].text == "O":
            cell[TextComponent].color = settings.BOARD.O_TEXT_COLOR


def update_turn_label(ui: dict):
    turn_label = ui.get(GameHUDBuilder.turn_label_id)
    if turn_label:
        _id = ClientNetworkSystem.currently_playing_player_id
        turn_label[TextComponent].text = settings.BOARD.CHARS[_id] + "'s Turn"
        turn_label[TextComponent].color = settings.BOARD.CHAR_COLOR[_id]


def update_board(ui: dict):
    update_text_colors(ui)
    update_turn_label(ui)


def get_cell_id_at(target_coord: tuple):
    return BoardBuilder.board_cells_ids[target_coord]


def get_coord_of(target_cell_id: int):
    for coord, cell_id in BoardBuilder.board_cells_ids.items():
        if cell_id == target_cell_id:
            return coord


def play_move_at(ui: dict, char: str, cell_id: int):
    if ui[cell_id][TextComponent].text == " ":
        ui[cell_id][TextComponent].text = char


def has_drawn(ui):
    for cell_id in BoardBuilder.board_cells_ids.values():
        if ui[cell_id][TextComponent].text == " ":
            return False

    return True


def won_horizontally(ui: dict, char: str):
    for y in range(settings.BOARD.ROWS):
        char_count = 0  # For this row
        for x in range(settings.BOARD.COLS):
            cell_id = BoardBuilder.board_cells_ids[(x, y)]
            if ui[cell_id][TextComponent].text == char:
                char_count += 1

        if char_count == settings.BOARD.COLS:
            return True
    return False


def won_vertically(ui: dict, char: str):
    for x in range(settings.BOARD.COLS):
        chars_count = 0
        for y in range(settings.BOARD.ROWS):
            cell_id = BoardBuilder.board_cells_ids[(x, y)]
            if ui[cell_id][TextComponent].text == char:
                chars_count += 1

        if chars_count == settings.BOARD.ROWS:
            return True
    return False


def won_diagonally(ui: dict, char: str):
    left_diag_count = 0
    right_diag_count = 0

    for y in range(settings.BOARD.ROWS):
        inv_y = settings.BOARD.ROWS - y - 1

        right_diag_cell_id = BoardBuilder.board_cells_ids[(y, y)]
        left_diag_cell_id = BoardBuilder.board_cells_ids[(inv_y, inv_y)]

        if ui[right_diag_cell_id][TextComponent].text == char:
            right_diag_count += 1
        elif ui[left_diag_cell_id][TextComponent].text == char:
            left_diag_count += 1

    return settings.BOARD.ROWS in (right_diag_count, left_diag_count)


def get_board_state_with(ui: dict, char: str):
    if (
        won_diagonally(ui, char)
        or won_horizontally(ui, char)
        or won_vertically(ui, char)
    ):
        return "won"
    elif has_drawn(ui):
        return "drawn"
    return ""


def process(ui: dict, char: str):
    current_state = get_board_state_with(ui, char)
    match current_state:
        case "won":
            ClientNetworkSystem.prompt_i_won(NetworkManagingSystem.client)
        case "":
            pass
        case "drawn":
            ClientNetworkSystem.prompt_draw(NetworkManagingSystem.client)
