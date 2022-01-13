class HexagonalPosition:

    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __eq__(self, other):
        if not isinstance(HexagonalPosition):
            return NotImplemented
        return self.u - other.u == self.v - other.v == self.w - other.w
