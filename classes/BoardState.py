from typing import List

from classes.Coord import UPPER_SIGN
from classes.Hex import Hex, tupleToCoord
from classes.HexNode import HexNode
from classes.enums import getEnumByName, Token


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

        for i in range(len(upper_hexes)):
            print(str(upper_hexes[i]))
            x = HexNode(None, Hex(upper_hexes[i].coord, upper_hexes[i].token))
            x.getAvailableLocations(self.board_dict, [])
            print([str(i.cur_hex.coord.toTuple()) for i in x.available])
