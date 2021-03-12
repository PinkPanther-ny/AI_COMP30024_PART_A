from classes import BoardState, Action


class BoardNode:
    def __init__(self, boardState: BoardState, parent, action: Action, pathCost, heuristic):
        self.boardState = boardState
        self.parent = parent
        self.action = action
        self.pathCost = pathCost
        self.heuristic = heuristic
