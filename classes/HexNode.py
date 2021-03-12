from typing import List

from classes.Hex import *
from classes.Coord import *
from classes.enums import *


class HexNode:
    def __init__(self, parent, cur_hex: Hex):
        self.parent = parent
        self.cur_hex = cur_hex
        self.available: List[HexNode] = []

    # Using dict with assumption: each hex only contain one token
    def getAvailableLocations(self, board_dict: dict, visited):

        for i in Move:
            moved_coord = self.cur_hex.coord.move(i)

            if moved_coord.isValid() and (moved_coord.toTuple() not in visited):

                # Do the swing check before empty hex check, since swing moves fastest
                if len(board_dict[moved_coord.toTuple()]) > 0 and \
                        any(piece[0] == UPPER_SIGN[0] for piece in board_dict[moved_coord.toTuple()]):
                    # Swing from the location before movement taken
                    # Check if it's on board is done in getSwingPoints
                    # Check if swing point is empty,
                    # if not, check if their battle draw.
                    swings = self.cur_hex.coord.getSwingPoints(self, moved_coord, board_dict)
                    # check if the point we gonna swing is empty,
                    # if not, the only two cases that we can continue is
                    # 1: the same color from either side
                    # 2: different color from other side that we can beat it

                    for swing in swings:
                        self.available.append(HexNode(self, Hex(swing, self.cur_hex.token)))

                # Check if a hex is empty that we can move to.
                elif len(board_dict[moved_coord.toTuple()]) == 0:
                    self.available.append(HexNode(self, Hex(moved_coord, self.cur_hex.token)))
                    continue

                # Move onto a lower token if we can beat it, or simply ignore if the battle draw
                # Could improve, if more self side token than opponent, that would cause a lost!!!!!
                elif any(piece[0] == LOWER_SIGN[0] for piece in board_dict[moved_coord.toTuple()]):
                    battle_result = self.cur_hex.token.battle(
                        getEnumByName(board_dict[moved_coord.toTuple()][0][1], Token))

                    if battle_result or (battle_result is None):
                        self.available.append(HexNode(self, Hex(moved_coord, self.cur_hex.token)))

                    continue
            else:
                continue

    def extractRoute(self):
        if self.cur_hex is None:
            return []
        route = []
        node = self
        while node is not None:
            route.append(node.cur_hex.coord.toTuple())
            node = node.parent
        route.reverse()
        return route
