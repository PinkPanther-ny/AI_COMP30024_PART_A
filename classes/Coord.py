from classes.enums import *
from config.config import *


class Coord:

    def __init__(self, r, q):
        self.r = r
        self.q = q

    def __eq__(self, other):
        return (self.r == other.r) and (self.q == other.q)

    def distance(self, x: "Coord") -> int:
        # normalized to (0,0), then apply the pattern that I manually found.
        normalize = Coord(self.r - x.r, self.q - x.q)
        if signCheck(normalize.r, normalize.q):
            return abs(normalize.r + normalize.q)
        else:
            return max(abs(normalize.r), abs(normalize.q))

    def isValid(self) -> bool:
        if self.distance(Coord(0, 0)) <= BOARD_SIZE:
            return True
        else:
            return False

    def toTuple(self):
        return self.r, self.q

    def move(self, move: Move) -> "Coord":
        return Coord(self.r + move.value[0], self.q + move.value[1])

    def getSwingPoints(self, src_node, target: "Coord", board_dict) -> list:
        # Get relative swing location, only check if it is on the board
        # Tricky way, since self is not adjacent to any swing points.
        swings = []
        for i in Move:
            if target.move(i).distance(self) > 1 and target.move(i).isValid():
                swings.append(target.move(i))

        x = []

        for i in swings:
            # If the swing point is empty, safely add it
            if len(board_dict[i.toTuple()]) == 0:
                # if i.toTuple() not in board_dict:
                x.append(i)

            # else if the swing point contains a token from either side, as long as they are the same, add it
            elif any(piece[1].lower() == src_node.cur_hex.token.name for piece in board_dict[i.toTuple()]):
                # elif board_dict[i.toTuple()][1].lower() == src_node.cur_hex.token.name:
                x.append(i)

            # if swing point contains token that can be defeat, no matter from which side, smash it!
            elif CAN_SWING_ONTO_FRIENDLY_TOKEN and \
                    (getEnumByName(board_dict[i.toTuple()][0][1].lower(), Token) is not None):
                if src_node.cur_hex.token.battle(getEnumByName(board_dict[i.toTuple()][0][1].lower(), Token)):
                    x.append(i)

        return x


def signCheck(a, b):
    return a * b >= 0


def tupleToCoord(location):
    assert type(location) == tuple
    return Coord(location[0], location[1])
