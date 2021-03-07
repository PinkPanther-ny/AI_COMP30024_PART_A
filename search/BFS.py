from classes.Hex import *

from classes.Node import Node
DEBUG = 0


# Search direction x, y, z, -x, -y, -z.
# which is clockwise direction around a given point, start from unit vector in r axis (x)

def bfs(src: Hex, dst: Coord, board_dict: dict, visited):
    queue = []
    visited.clear()
    # Enqueue root

    # Don't know why this import only works inside function.

    root = Node(None, src.coord, src.token)
    queue.append(root)
    visited.append((root.current.r, root.current.q))

    while len(queue) != 0:

        current = queue.pop(0)
        current.getAvailableLocations(board_dict, visited)
        if DEBUG:
            print("\n\n")
            print(f"Current search node: {current.current.toTuple()}\n"
                  f"current queue: {[i.current.toTuple() for i in queue]}"
                  f"\navailable nodes:")

        for node in current.available:
            if DEBUG:
                print(node.current.toTuple())
            if node.current.r == dst.r and node.current.q == dst.q:
                if DEBUG:
                    print("Found!")
                return node
            current_coord = (node.current.r, node.current.q)
            if current_coord not in visited:
                queue.append(node)
                visited.append(current_coord)
        if DEBUG:
            print(f"visited nodes after search around node {current.current.toTuple()}:\n {visited}")
            print(f"current queue: {[i.current.toTuple() for i in queue]}")

    if DEBUG:
        print("Not Found!")
    # return none node, to extract an empty route
    return Node(None, None, None)
