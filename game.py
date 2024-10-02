from entities import Bottle, Board, Color as c, Move
from pprint import pprint
from actions import pour, get_all_moves
from copy import deepcopy
from typing import Optional, Any
from collections import defaultdict


bottle_colors = [
    [c.BROWN,   c.ORANGE,  c.GREEN,   c.GREEN],
    [c.PURPLE,  c.YELLOW,  c.CYAN,    c.BEIGE],
    [c.BROWN,   c.PINK,    c.CYAN,    c.PINK],
    [c.MAGENTA, c.PURPLE,  c.RED,     c.PINK],
    [c.MAGENTA, c.BROWN,   c.MAGENTA, c.CYAN],
    [c.BEIGE, c.MAGENTA, c.BLUE,    c.YELLOW],
    [c.YELLOW, c.BROWN,   c.PURPLE,  c.ORANGE],

    [c.GREEN,   c.BLUE,    c.BEIGE,   c.FOREST],
    [c.PINK,    c.RED,     c.BLUE,    c.PURPLE],
    [c.FOREST,  c.YELLOW,  c.CYAN,    c.GREEN],
    [c.RED,     c.RED,     c.FOREST,  c.BLUE],
    [c.ORANGE,  c.ORANGE,  c.BEIGE,   c.FOREST],

    [],
    [],
]

board = Board(Bottle(colors) for colors in bottle_colors)

node_tree = defaultdict(dict)


visited_boards = set()


def play(board: Board, solution_tree_node: dict, last_move: Optional[Move] = None):

    board_state = board.as_hashable

    if board_state in visited_boards:
        return

    visited_boards.add(board_state)

    moves = get_all_moves(board)
    # pprint(board)
    pprint(moves)


    for move in moves:
        # Skip back-and-forths
        if last_move and set(move) == set(last_move):
            continue

        new_board = deepcopy(board)
        pour(new_board[move.source], new_board[move.target])

        solution_tree_node[move] = defaultdict(dict)

        if new_board.is_complete:
            solution_tree_node[move] = True
            raise RuntimeError('Done')

        play(new_board, solution_tree_node[move], move)

try:
    play(board, node_tree)
except Exception:
    print('Done')

def find_winning_path(solution_tree_node: dict) -> Optional[list[Move]]:
    # Base case: If the current node is `True`, we have found a winning path.
    if solution_tree_node is True:
        return []

    # Recursively search for the winning path
    for move, subtree in solution_tree_node.items():
        result = find_winning_path(subtree)
        if result is not None:  # Found a winning path in the subtree
            return [move] + result

    # If no winning path is found in this subtree
    return None

# Example usage to find the path
winning_path = find_winning_path(node_tree)

if winning_path:
    print("Winning path found!")
    for step, move in enumerate(winning_path):
        if step % 5 == 0:
            print('')
        print(f"Step {step + 1}: {board[move.source].top_color.name} from {move.source} to {move.target}")
        pour(board[move.source], board[move.target])


else:
    print("No winning path found.")


# pprint(board)
