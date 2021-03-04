import copy

from classes.Hex import *

DEBUG = 0


# TODO:
# Search available points from current location
# Apply swing action when searching
# Search direction x, y, z, -x, -y, -z.
# which is clockwise direction around a given point, start from unit vector in r axis (x)
class Node:
    def __init__(self, parent, coord: Coord, token):
        self.parent = parent
        self.current = coord
        self.token = token
        self.available = []

    # Using dict with assumption: each hex only contain one token
    def getAvailableLocations(self, board_dict: dict):

        for i in Move:
            moved_coord = self.current.move(i)

            if moved_coord.isValid() and ((moved_coord.r, moved_coord.q) not in visited):

                # Do the swing check before empty hex check, since swing moves fastest
                if moved_coord.toTuple() in board_dict and board_dict[moved_coord.toTuple()][0] == UPPER_SIGN[0]:
                    # Swing from the location before movement taken
                    # Check if it's on board is done in getSwingPoints
                    # Check if swing point is empty,
                    # if not, check if their battle draw.
                    swings = self.current.getSwingPoints(moved_coord)
                    swings = [i for i in swings if (i.toTuple() not in board_dict) or
                              (board_dict[i.toTuple()][1].lower() == self.token.name)]
                    for swing in swings:
                        self.available.append(Node(self, swing, self.token))

                # Check if a hex is empty that we can move to.
                elif moved_coord.toTuple() not in board_dict:
                    self.available.append(Node(self, moved_coord, self.token))
                    continue

                # Move onto a lower token if we can beat it, or simply ignore if the battle draw
                elif board_dict[moved_coord.toTuple()][0] == LOWER_SIGN[0]:
                    # print(self.token, board_dict[moved_coord.toTuple()][1].lower())
                    battle_result = self.token.battle(
                        getEnumByName(board_dict[moved_coord.toTuple()][1].lower(), Token))
                    # print(battle_result)
                    if battle_result is None or battle_result == True:
                        self.available.append(Node(self, moved_coord, self.token))

                    continue
            else:
                continue

    def extractRoute(self):
        route = []
        node = self
        while node is not None:
            route.append(node.current.toTuple())
            node = node.parent
        route.reverse()
        return route


visited = []
a = 0


def bfs(src: Hex, dst: Coord, board_dict: dict):
    queue = []
    visited.clear()
    # Enqueue root
    root = Node(None, src.coord, src.token)
    queue.append(root)
    visited.append((root.current.r, root.current.q))

    while len(queue) != 0:

        current = queue.pop(0)
        current.getAvailableLocations(board_dict)
        if DEBUG:
            print("\n\n")
            print(f"Current search node: {current.current.toTuple()}\n"
                  f"current queue: {[i.current.toTuple() for i in queue]}"
                  f"\navailable nodes:")

        for node in current.available:
            if DEBUG: print(node.current.toTuple())
            if node.current.r == dst.r and node.current.q == dst.q:
                if DEBUG: print("Found!")
                return node
            current_coord = (node.current.r, node.current.q)
            if current_coord not in visited:
                queue.append(node)
                visited.append(current_coord)
        if DEBUG:
            print(f"visited nodes after search around node {current.current.toTuple()}:\n {visited}")
            print(f"current queue: {[i.current.toTuple() for i in queue]}")

    if DEBUG: print("Not Found!")
    return False
