from math import inf

from classes.BoardNode import BoardNode
from classes.BoardState import BoardState
from classes.PriorityQueue import PriorityQueue
from config.config import *
from search.util import getAllRoutes, getSrcDstPairs


def AStar(rootNode: BoardNode):
    frontier = PriorityQueue()
    frontier.put(rootNode, rootNode.pathCost + rootNode.heuristic)

    while not frontier.empty():
        current = frontier.get()
        if current.boardState.win():
            return current

        for child in current.boardState.getChildStates():

            # if child.lose():
                # continue
            child_node = BoardNode(child, current, None,
                                   0 if BEST_FIRST_SEARCH_ON else WEIGHT_ON_COST*(current.pathCost + 1),
                                   heuristic(child))
            frontier.put(child_node, child_node.pathCost + child_node.heuristic)

    return None


def heuristic(board_state: BoardState):
    try:
        if HEURISTIC_MODE == H_SINGLE_BFS_MAX_DISTANCE:
            return max([len(i) for i in getAllRoutes(board_state)])
        elif HEURISTIC_MODE == H_SINGLE_MAX_ABSOLUTE_DISTANCE:
            return max([i[0].coord.distance(i[1].coord) for i in getSrcDstPairs(board_state)])
    except ValueError:
        return inf


def weight(board_state: BoardState):
    r = 0
    l_r = 0
    p = 0
    l_p = 0
    s = 0
    l_s = 0
    board_state.update()
    for location in board_state.board_dict:
        for piece in board_state.board_dict[location]:
            if piece[0] == UPPER_SIGN[0]:
                if piece[1].lower() == 'r':
                    r += 1
                elif piece[1].lower() == 'p':
                    p += 1
                else:
                    s += 1
            elif piece[0] == LOWER_SIGN[0]:
                if piece[1].lower() == 'r':
                    l_r += 1
                elif piece[1].lower() == 'p':
                    l_p += 1
                else:
                    l_s += 1
    if r + p + s == 0:
        return inf
    else:
        return (l_r + l_p + l_s) / (r + p + s)
