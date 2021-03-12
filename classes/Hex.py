from classes.Coord import *


class Hex:
    def __init__(self, coord: Coord, token: Token):
        self.token = token
        self.coord = coord

    def move(self, move: Move):
        self.coord.r += move.value[0]
        self.coord.q += move.value[1]

    def __str__(self):
        return f"({self.token.name.upper()}, {self.coord.toTuple()})"
