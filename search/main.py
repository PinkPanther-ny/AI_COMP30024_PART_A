"""
COMP30024 Artificial Intelligence, Semester 1, 2021
Project Part A: Searching

This script contains the entry point to the program (the code in
`__main__.py` calls `main()`). Your solution starts here!
"""

import itertools
import json
import os
import sys
from time import sleep

from classes.RouteInfo import RouteInfo
from search.BFS import *
from search.util import *

visited = []


def main():
    try:
        with open(sys.argv[1]) as file:
            data = json.load(file)
    except IndexError:
        print("usage: python3 -m search path/to/input.json", file=sys.stderr)
        sys.exit(1)

    board_dict = create_board(data)
    print_board(board_dict, compact=False)

    routes = getAllRoutes(data, board_dict)


def create_board(data: dict) -> dict:
    board_dict = {}
    for i in data["upper"]:
        board_dict[(i[1], i[2])] = UPPER_SIGN[0] + i[0].upper() + UPPER_SIGN[1]
    for i in data["lower"]:
        board_dict[(i[1], i[2])] = LOWER_SIGN[0] + i[0].upper() + LOWER_SIGN[1]
    for i in data["block"]:
        board_dict[(i[1], i[2])] = BLOCK_SIGN

    return board_dict


def visualize_test(board_states: list, spf=0.8):
    os.system("cls")
    count = 0
    for state in board_states:
        count += 1
        print_board(state)
        sleep(spf)
        if count < len(board_states):
            os.system("cls")


def getAllRoutes(data, board_dict, show_routes=True):
    sources = data["upper"]
    destinations = data["lower"]

    src_dst_pairs = []
    routes = []
    for src, dst in itertools.product(sources, destinations):
        src_hex = Hex(Coord(src[1], src[2]), getEnumByName(src[0], Token))
        dst_hex = Hex(Coord(dst[1], dst[2]), getEnumByName(dst[0], Token))
        if src_hex.token.battle(dst_hex.token):
            src_dst_pairs.append([src_hex, dst_hex])
            routes.append(RouteInfo(src_hex, dst_hex, bfs(src_hex, dst_hex.coord, board_dict, visited).extractRoute()))

    # sort rule implemented in RouteInfo class
    routes.sort()
    if show_routes:
        for i in routes:
            print(f"{i.src_hex.coord.toTuple()} to {i.dst_hex.coord.toTuple()}\nRoute: {i.route} length {len(i.route)}")

    return routes
# visualize_test(states, 0.4)
# test()
