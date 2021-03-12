class RouteInfo:
    def __init__(self, src_hex, dst_hex, route):
        self.src_hex = src_hex
        self.dst_hex = dst_hex
        self.route = route

    def __len__(self):
        return len(self.route)

    def __lt__(self, other):
        return len(self) < len(other)

    def __str__(self):
        return f"From {str(self.src_hex):13} to {str(self.dst_hex):13}, length {len(self)}:\n" \
               f" {self.route}\n"
