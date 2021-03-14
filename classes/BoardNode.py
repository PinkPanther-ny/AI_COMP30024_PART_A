from classes import BoardState, Action


class BoardNode:
    def __init__(self, boardState: BoardState, parent, action: Action, pathCost, heuristic):
        self.boardState = boardState
        self.parent = parent
        self.action = action
        self.pathCost = pathCost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.pathCost + self.heuristic) < (other.pathCost + other.heuristic)

    def __le__(self, other):
        return (self.pathCost + self.heuristic) <= (other.pathCost + other.heuristic)
