from classes.Coord import *
from classes.enums import *


class HexNode:
    def __init__(self, parent, coord, token):
        self.parent = parent
        self.current = coord
        self.token = token
        self.available = []

    # Using dict with assumption: each hex only contain one token
    def getAvailableLocations(self, board_dict: dict, visited):

        for i in Move:
            moved_coord = self.current.move(i)

            if moved_coord.isValid() and ((moved_coord.r, moved_coord.q) not in visited):

                # Do the swing check before empty hex check, since swing moves fastest
                if len(board_dict[moved_coord.toTuple()]) > 0 and \
                        any(piece[0] == UPPER_SIGN[0] for piece in board_dict[moved_coord.toTuple()]):
                    # Swing from the location before movement taken
                    # Check if it's on board is done in getSwingPoints
                    # Check if swing point is empty,
                    # if not, check if their battle draw.
                    swings = self.current.getSwingPoints(self, moved_coord, board_dict)
                    # check if the point we gonna swing is empty,
                    # if not, the only two cases that we can continue is
                    # 1: the same color from either side
                    # 2: different color from other side that we can beat it

                    for swing in swings:
                        self.available.append(HexNode(self, swing, self.token))

                # Check if a hex is empty that we can move to.
                elif len(board_dict[moved_coord.toTuple()]) == 0:
                    self.available.append(HexNode(self, moved_coord, self.token))
                    continue

                # Move onto a lower token if we can beat it, or simply ignore if the battle draw
                # Could improve, if more self side token than opponent, that would cause a lost!!!!!
                elif any(piece[0] == LOWER_SIGN[0] for piece in board_dict[moved_coord.toTuple()]):
                    battle_result = self.token.battle(
                        getEnumByName(board_dict[moved_coord.toTuple()][0][1], Token))

                    if battle_result or (battle_result is None):
                        self.available.append(HexNode(self, moved_coord, self.token))

                    continue
            else:
                continue

    def extractRoute(self):
        if self.current is None:
            return []
        route = []
        node = self
        while node is not None:
            route.append(node.current.toTuple())
            node = node.parent
        route.reverse()
        return route
