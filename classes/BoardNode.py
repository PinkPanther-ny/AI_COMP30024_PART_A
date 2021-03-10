from classes import BoardState, Action


class BoardNode:
    def __init__(self, boardState: BoardState, parent: "BoardNode", action: Action, pathCost):
        self.boardState = boardState
        self.parent = parent
        self.action = action
        self.pathCost = pathCost
