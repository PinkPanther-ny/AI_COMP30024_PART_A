from math import inf

from classes.BoardNode import BoardNode
from classes.PriorityQueue import PriorityQueue
from search.util import getAllRoutes, getSrcDstPairs
from config.config import *


def AStar(rootNode: BoardNode):
    frontier = PriorityQueue()
    frontier.put(rootNode, rootNode.pathCost + rootNode.heuristic)

    while not frontier.empty():
        current = frontier.get()
        if current.boardState.win():
            return current

        for child in current.boardState.getChildStates():
            child_node = BoardNode(child, current, None, current.pathCost + 1, heuristic(child))
            frontier.put(child_node, child_node.pathCost+child_node.heuristic)
    return None


def heuristic(board_state):
    try:
        if HEURISTIC_MODE == H_SINGLE_BFS_MAX_DISTANCE:
            return max([len(i) for i in getAllRoutes(board_state)])
        elif HEURISTIC_MODE == H_SINGLE_MAX_ABSOLUTE_DISTANCE:
            return max([i[0].coord.distance(i[1].coord) for i in getSrcDstPairs(board_state)])
    except ValueError:
        return 8
