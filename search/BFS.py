from classes.Hex import *

from classes.HexNode import HexNode


# Search direction x, y, z, -x, -y, -z.
# which is clockwise direction around a given point, start from unit vector in r axis (x)

def bfs(src: Hex, dst: Coord, board_dict: dict):
    # List of HexNode
    queue = []
    # List of tuple
    visited = []
    # Enqueue root

    # Don't know why this import only works inside function.

    root = HexNode(None, Hex(src.coord, src.token))
    queue.append(root)
    visited.append(root.cur_hex.coord.toTuple())

    while len(queue) != 0:

        current_node = queue.pop(0)
        current_node.getAvailableLocations(board_dict, visited)
        if BFS_DEBUG:
            print("\n\n")
            print(f"Current search node: {current_node.cur_hex.coord.toTuple()}\n"
                  f"current queue: {[i.cur_hex.coord.toTuple() for i in queue]}"
                  f"\navailable nodes:")

        for node in current_node.available:
            if BFS_DEBUG:
                print(node.cur_hex.coord.toTuple())
            if node.cur_hex.coord == dst:
                if BFS_DEBUG:
                    print("Found!")
                return node
            current_coord = node.cur_hex.coord.toTuple()
            if current_coord not in visited:
                queue.append(node)
                visited.append(current_coord)
        if BFS_DEBUG:
            print(f"visited nodes after search around node {current_node.cur_hex.coord.toTuple()}:\n {visited}")
            print(f"current queue: {[i.cur_hex.coord.toTuple() for i in queue]}")

    if BFS_DEBUG:
        print("Not Found!")
    # return none node, to extract an empty route
    return HexNode(None, None)
