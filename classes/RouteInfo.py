class RouteInfo:
    def __init__(self, src_hex, dst_hex, route):
        self.src_hex = src_hex
        self.dst_hex = dst_hex
        self.route = route

    def __lt__(self, other):
        return len(self.route) < len(other.route)
