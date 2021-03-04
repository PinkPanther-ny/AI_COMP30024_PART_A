from enum import Enum
from typing import Optional


class Token(Enum):
    r = 1
    p = 2
    s = 3

    def __eq__(self, other: "Token"):
        return self.value == other.value

    def battle(self, opponent):
        df = self.value - opponent.value
        if df == 1 or df == -2:
            # Win
            return True
        elif df == 0:
            # Draw
            return None
        else:
            # Lose
            return False


def getEnumByName(name, enum):
    for i in enum:
        if name == i.name:
            return i
    return None


class Move(Enum):
    x = [1, 0]
    y = [0, 1]
    z = [-1, 1]
    nx = [-1, 0]
    ny = [0, -1]
    nz = [1, -1]
