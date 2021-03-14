"""
COMP30024 Artificial Intelligence, Semester 1, 2021
Project Part A: Searching

This script contains the entry point to the program (the code in
`__main__.py` calls `main()`). Your solution starts here!
"""
import copy
import json
import sys
import time

from classes.BoardNode import BoardNode
from classes.BoardState import BoardState
from search.AStar import AStar, heuristic
from search.util import *


def main():
    try:
        with open(sys.argv[1]) as file:
            data = json.load(file)
    except IndexError:
        print("usage: python3 -m search path/to/input.json", file=sys.stderr)
        sys.exit(1)
    t0 = time.time()
    board_dict = create_board(data)
    root_state = BoardState(board_dict)

    print_board(root_state, compact=True)
    root_node = BoardNode(
        BoardState(board_dict), parent=None, action=None,
        pathCost=0, heuristic=heuristic(root_state)
    )
    result = AStar(root_node)
    astar_states = []
    while result:
        astar_states.append(copy.deepcopy(result.boardState))
        result = result.parent
    astar_states.reverse()
    t1 = time.time()

    if VISUALIZE_RESULT:
        visualize_test(astar_states, compact=True, spf=1)
        print(f"Solution found in {t1 - t0} seconds.")
