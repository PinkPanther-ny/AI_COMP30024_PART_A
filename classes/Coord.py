from classes.enums import *

# Global variables

# Maximum distance from the centre hex
BOARD_SIZE = 4
UPPER_SIGN = "()"
LOWER_SIGN = "  "
BLOCK_SIGN = "#####"


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

            if i.toTuple() not in board_dict:
                x.append(i)
            elif board_dict[i.toTuple()][1].lower() == src_node.token.name:
                x.append(i)
            elif getEnumByName(board_dict[i.toTuple()][1].lower(), Token) is not None:
                if src_node.token.battle(getEnumByName(board_dict[i.toTuple()][1].lower(), Token)):
                    x.append(i)

        # swings = [i for i in swings if (i.toTuple() not in board_dict) or
        #          (board_dict[i.toTuple()][1].lower() == src_node.token.name) or
        #          (src_node.token.battle(getEnumByName(board_dict[target.toTuple()][1].lower(), Token)))]

        return x


def signCheck(a, b):
    return a * b >= 0
