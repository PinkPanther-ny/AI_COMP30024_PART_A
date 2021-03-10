from classes import Hex
from classes.enums import Move


class Action:
    def __init__(self, currentHex: Hex, action: Move):
        self.hex = currentHex
        self.action = action
