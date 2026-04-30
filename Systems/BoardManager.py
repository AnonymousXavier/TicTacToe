from Builders.GameBoardBuilder import BoardBuilder
from Globals import settings
from Globals.Components import TextComponent


def update_text_colors(ui: dict):
    for cell_id in BoardBuilder.board_cells_ids.values():
        cell = ui[cell_id]

        if cell[TextComponent].text == "X":
            cell[TextComponent].color = settings.BOARD.X_TEXT_COLOR
        elif cell[TextComponent].text == "O":
            cell[TextComponent].color = settings.BOARD.O_TEXT_COLOR


def get_cell_id_at(target_coord: tuple):
    return BoardBuilder.board_cells_ids[target_coord]


def get_coord_of(target_cell_id: int):
    for coord, cell_id in BoardBuilder.board_cells_ids.items():
        if cell_id == target_cell_id:
            return coord


def play_move_at(ui: dict, char: str, cell_id: int):
    if ui[cell_id][TextComponent].text == " ":
        ui[cell_id][TextComponent].text = char
