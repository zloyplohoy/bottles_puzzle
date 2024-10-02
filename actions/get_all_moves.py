from entities import Board, Bottle, Move
from .pour import pour

def get_all_moves(board: Board) -> list[Move]:
    moves = []

    single_color_size_3_colors = [bottle.top_color for bottle in board if bottle.source_capacity == 3 and bottle.is_single_color]

    for source_bottle_index, source_bottle in enumerate(board):
        for target_bottle_index, target_bottle in enumerate(board):
            # Skip the source bottle
            if source_bottle_index == target_bottle_index:
                continue

            # Check if pouring is possible
            if source_bottle.top_color in single_color_size_3_colors and target_bottle.is_empty:
                continue

            if pour(source_bottle, target_bottle, test=True):
                moves.append(Move(source_bottle_index, target_bottle_index))

    return moves
