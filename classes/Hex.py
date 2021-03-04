from classes.Coord import *


class Hex:
    def __init__(self, coord: Coord, token: Token):
        self.token = token
        self.coord = coord

    def move(self, move: Move):
        self.coord.r += move.value[0]
        self.coord.q += move.value[1]


def test():
    # Test cases
    print("\n\n")
    print(Coord(0, 0).__eq__(Coord(0, 0)))
    print(Coord(0, 0).distance(Coord(2, -1)))
    print(Coord(0, 0).distance(Coord(2, -2)))
    print(Coord(0, 0).distance(Coord(1, -2)))
    print(Coord(0, 0).distance(Coord(0, -2)))
    print(Coord(0, 0).distance(Coord(-1, -1)))
    print(Coord(0, 0).distance(Coord(-2, 0)))
    print(Coord(0, 0).distance(Coord(-2, 1)))
    print(Coord(0, 0).distance(Coord(-2, 2)))
    print(Coord(0, 0).distance(Coord(-1, 2)))
    print(Coord(0, 0).distance(Coord(0, 2)))
    print(Coord(0, 0).distance(Coord(1, 1)))
    print(Coord(0, 0).distance(Coord(1, 1)))

    print("\n\n")
    print(Hex(Coord(0, 0), Token.r).battle(Hex(Coord(0, 0), Token.r)))
    print(Hex(Coord(0, 0), Token.r).battle(Hex(Coord(0, 0), Token.p)))
    print(Hex(Coord(0, 0), Token.r).battle(Hex(Coord(0, 0), Token.s)))
    print(Hex(Coord(0, 0), Token.s).battle(Hex(Coord(0, 0), Token.r)))
    print(Hex(Coord(0, 0), Token.s).battle(Hex(Coord(0, 0), Token.p)))
    print(Hex(Coord(0, 0), Token.s).battle(Hex(Coord(0, 0), Token.s)))
    print(Hex(Coord(0, 0), Token.p).battle(Hex(Coord(0, 0), Token.r)))
    print(Hex(Coord(0, 0), Token.p).battle(Hex(Coord(0, 0), Token.p)))
    print(Hex(Coord(0, 0), Token.p).battle(Hex(Coord(0, 0), Token.s)))

    print("\n\n")
    h = Hex(Coord(0, 0), Token.r)
    h.move(Move.x)
    print(h.coord.r, h.coord.q)

    h = Hex(Coord(0, 0), Token.r)
    h.move(Move.y)
    print(h.coord.r, h.coord.q)

    h = Hex(Coord(0, 0), Token.r)
    h.move(Move.z)
    print(h.coord.r, h.coord.q)

    h = Hex(Coord(0, 0), Token.r)
    h.move(Move.nx)
    print(h.coord.r, h.coord.q)

    h = Hex(Coord(0, 0), Token.r)
    h.move(Move.ny)
    print(h.coord.r, h.coord.q)

    h = Hex(Coord(0, 0), Token.r)
    h.move(Move.nz)
    print(h.coord.r, h.coord.q)


    print("\n\n")
    for i in Move:
        coord = Coord(0,0).move(i)
        print(coord.r, coord.q)