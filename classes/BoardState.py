import itertools
from typing import List

from classes.Hex import Hex, tupleToCoord
from classes.HexNode import HexNode
from classes.enums import getEnumByName, Token
from config.config import *


class BoardState:
    def __init__(self, board_dict):
        self.board_dict = board_dict

    def update(self):

        # First remove empty
        for i in self.board_dict.copy():
            # use copy to avoid "dictionary changed size during iteration"
            if len(self.board_dict[i]) == 0:
                del self.board_dict[i]

        # Check each hex, if they battle
        for i in self.board_dict.copy():

            if len(self.board_dict[i]) > 1:
                # Start battle
                pieces = set()
                for piece in self.board_dict[i]:
                    pieces.add(piece[1])

                if len(pieces) == 3:
                    del self.board_dict[i]
                elif len(pieces) == 2:
                    pieces = list(pieces)
                    if getEnumByName(pieces[0], Token).battle(getEnumByName(pieces[1], Token)):
                        for token in self.board_dict[i].copy():
                            if token == pieces[1]:
                                self.board_dict[i].remove(token)
                    else:
                        for token in self.board_dict[i].copy():
                            if token == pieces[0]:
                                self.board_dict[i].remove(token)

    def getChildStates(self):
        upper_hexes: List[Hex] = []
        for location in self.board_dict:
            for piece in self.board_dict[location]:
                if piece[0] == UPPER_SIGN[0]:
                    upper_hexes.append(Hex(tupleToCoord(location), getEnumByName(piece[1], Token)))

        next_steps = []
        for i in range(len(upper_hexes)):
            this_hex = HexNode(None, Hex(upper_hexes[i].coord, upper_hexes[i].token))
            this_hex.getAvailableLocations(self.board_dict, [])
            next_steps.append([i.cur_hex for i in this_hex.available])
            if GET_CHILD_STATES_DEBUG:
                print(f"Hex: {str(upper_hexes[i])} with its next available movements:\n"
                      f"{[str(i.cur_hex) for i in this_hex.available]}\n")
        # A list of list of child state hexes
        combination = [[n for n in i] for i in itertools.product(*next_steps)]

        if CHILD_STATES_SHOW_HEX:
            print("The combination of their movements are:")
            for i in combination:
                print("\t\t", [str(h) for h in i])
