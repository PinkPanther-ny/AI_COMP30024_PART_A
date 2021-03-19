import copy
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
                            if token[1] == pieces[1]:
                                self.board_dict[i].remove(token)
                    else:
                        for token in self.board_dict[i].copy():
                            if token[1] == pieces[0]:
                                self.board_dict[i].remove(token)

    def getChildStates(self):
        origin = copy.deepcopy(self.board_dict)
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

        self.update()
        if CHILD_STATES_SHOW_COMBINATIONS:
            print("The combination of their movements are:")
            for i in combination:
                print("\t\t", [str(h) for h in i])

        for location in self.board_dict.copy():
            # Remove all upper tokens
            self.board_dict[location] = [token for token in self.board_dict[location] if token[0] != UPPER_SIGN[0]]
        self.update()

        new_board_states: List[BoardState] = []
        for new_upper_hexes in combination:
            new_board_state = copy.deepcopy(self.board_dict)
            for new_hex in new_upper_hexes:
                new_board_state[new_hex.coord.toTuple()].append(
                    UPPER_SIGN[0] + new_hex.token.name.upper() + UPPER_SIGN[1])
            new_board_states.append(BoardState(copy.deepcopy(new_board_state)))

        self.board_dict = origin
        return new_board_states

    def win(self):

        self.update()
        for location in self.board_dict:
            for token in self.board_dict[location]:
                if token[0] == LOWER_SIGN[0]:
                    return False
        return True

    def lose(self):
        upper_tokens = set()
        lower_tokens = set()
        self.update()
        for location in self.board_dict:
            for token in self.board_dict[location]:
                if token[0] == UPPER_SIGN[0]:
                    upper_tokens.add(getEnumByName(token[1], Token))
                elif token[0] == LOWER_SIGN[0]:
                    lower_tokens.add(getEnumByName(token[1], Token))
        upper_tokens = list(upper_tokens)
        lower_tokens = list(lower_tokens)
        if len(upper_tokens) < len(lower_tokens):
            return True
        elif len(upper_tokens) == 1 and len(lower_tokens) == 1:
            return lower_tokens[0].battle(upper_tokens[0])
        else:
            return False

    def toKey(self):
        self.update()
        list_items = []
        for i in self.board_dict.copy():
            list_items.append((i, sorted(self.board_dict[i])))
        list_items.sort()

        return str(list_items)
