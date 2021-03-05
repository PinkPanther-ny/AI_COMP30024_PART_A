from classes.Node import *


class RouteInfo:
    def __init__(self, src_hex, dst_hex, route):
        self.src_hex = src_hex
        self.dst_hex = dst_hex
        self.route = route

    def extractRoute(self: Node):
        if self.current is None:
            return None
        route = []
        node = self
        while node is not None:
            route.append(node.current.toTuple())
            node = node.parent
        route.reverse()
        return route
