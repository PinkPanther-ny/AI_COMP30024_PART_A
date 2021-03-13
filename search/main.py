"""
COMP30024 Artificial Intelligence, Semester 1, 2021
Project Part A: Searching

This script contains the entry point to the program (the code in
`__main__.py` calls `main()`). Your solution starts here!
"""
import copy
import itertools
import json
import sys
from math import inf

from classes.BoardNode import BoardNode
from classes.BoardState import BoardState
from classes.Hex import *
from classes.RouteInfo import RouteInfo
from search.AStar import AStar
from search.BFS import bfs
from search.util import *


def main():
    try:
        with open(sys.argv[1]) as file:
            data = json.load(file)
    except IndexError:
        print("usage: python3 -m search path/to/input.json", file=sys.stderr)
        sys.exit(1)

    board_dict = create_board(data)
    root_state = BoardState(board_dict)
    routes = getAllRoutes(data, board_dict)
    print_board(root_state, compact=False)
    root_node = BoardNode(
        BoardState(board_dict), parent=None, action=None,
        pathCost=0, heuristic=max([len(i) for i in routes])
    )

    AStar(root_node)
    root_state.getChildStates()


def getAllRoutes(data, board_dict):
    sources = data["upper"]
    destinations = data["lower"]

    src_dst_pairs = []
    routes = []
    for src, dst in itertools.product(sources, destinations):
        src_hex = Hex(Coord(src[1], src[2]), getEnumByName(src[0], Token))
        dst_hex = Hex(Coord(dst[1], dst[2]), getEnumByName(dst[0], Token))
        if src_hex.token.battle(dst_hex.token):
            src_dst_pairs.append([src_hex, dst_hex])
            routes.append(RouteInfo(src_hex, dst_hex, bfs(src_hex, dst_hex.coord, board_dict).extractRoute()))

    # sort rule implemented in RouteInfo class
    routes.sort()
    if SINGLE_TOKEN_SHOW_ROUTE:
        for i in routes:
            print(i)

    return routes


# Test cases for animating the game
states = []
state = defaultdict(list)
state[(0, 0)].append(" s ")
state[(0, 1)].append(" p ")
state[(0, 2)].append(" r ")
state = BoardState(state)
state.update()
states.append(copy.deepcopy(state))

state.board_dict[(0, 0)].append("(r)")
state.update()
states.append(copy.deepcopy(state))

state.board_dict[(0, 0)].append("(p)")
state.board_dict[(0, 0)].append("(s)")

state.update()
states.append(copy.deepcopy(state))

# visualize_test(states, spf=0.8, messageOn=True, compact=False)
# test()
