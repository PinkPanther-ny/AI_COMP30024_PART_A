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
from typing import List

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
    root_state = BoardState(board_dict, action=None)

    print_board(root_state, compact=True)
    root_node = BoardNode(
        root_state, parent=None, action=None,
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
    if SHOW_SOLVE_TIME:
        print(f"Solution found in {t1 - t0} seconds.")
    show_actions(astar_states)

def show_actions(astar_states: List[BoardState]):
    turn = 0
    for state in astar_states:
        if state.action is not None:
            for singleMove in state.action:
                if singleMove[0].coord.distance(singleMove[1].coord) == 1:
                    print_slide(turn, singleMove[0].coord.r, singleMove[0].coord.q,
                                singleMove[1].coord.r, singleMove[1].coord.q)
                elif singleMove[0].coord.distance(singleMove[1].coord) == 2:
                    print_swing(turn, singleMove[0].coord.r, singleMove[0].coord.q,
                                singleMove[1].coord.r, singleMove[1].coord.q)
                else:
                    print(f"error! Turn: {turn}")
        turn += 1