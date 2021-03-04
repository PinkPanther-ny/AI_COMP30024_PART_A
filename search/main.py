"""
COMP30024 Artificial Intelligence, Semester 1, 2021
Project Part A: Searching

This script contains the entry point to the program (the code in
`__main__.py` calls `main()`). Your solution starts here!
"""

import sys
import json
import itertools

# If you want to separate your code into separate files, put them
# inside the `search` directory (like this one and `util.py`) and
# then import from them like this:
# from search.util import print_board, print_slide, print_swing
from random import Random

from classes.Coord import *
from classes.Hex import test, Hex
from search.BFS import *
from search.util import *

import os
from time import sleep


def main():
    try:
        with open(sys.argv[1]) as file:
            data = json.load(file)
    except IndexError:
        print("usage: python3 -m search path/to/input.json", file=sys.stderr)
        sys.exit(1)

    board_dict = create_board(data)
    print_board(board_dict, compact=False)
    # print(data)

    sources = data["upper"]
    destinations = data["lower"]
    # print(sources, "\n", destinations)

    src_dst_pairs = []
    routes = []
    for src, dst in itertools.product(sources, destinations):
        src_hex = Hex(Coord(src[1], src[2]), getEnumByName(src[0], Token))
        dst_hex = Hex(Coord(dst[1], dst[2]), getEnumByName(dst[0], Token))
        if src_hex.token.battle(dst_hex.token):
            print(src, dst)
            src_dst_pairs.append([src_hex, dst_hex])
            routes.append(RouteInfo(src_hex, dst_hex, bfs(src_hex, dst_hex.coord, board_dict)))

    x = Random().randint(a=0, b=len(src_dst_pairs)-1)
    s = src_dst_pairs[x][0]
    d = src_dst_pairs[x][1].coord

    route = bfs(s, d, board_dict).extractRoute()
    # print(f"\nFrom {s.coord.toTuple()} to {d.toTuple()}\nRoute is: {route}\n")
    # sleep(2)

    board_states = []
    current_state = dict(board_dict)
    for i in route:
        current_state = dict(current_state)
        current_state[i] = UPPER_SIGN[0] + s.token.name.upper() + UPPER_SIGN[1]
        board_states.append(dict(current_state))
        current_state[i] = ""

    visualize_test(board_states)
    return board_dict
    # TODO:
    # Find and print a solution to the board configuration described
    # by `data`.
    # Why not start by trying to print this configuration out using the
    # `print_board` helper function? (See the `util.py` source code for
    # usage information).


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

# visualize_test(states, 0.4)
# test()