import math


class HexagonalPosition:

    def to_cartesian_position(self):
        x = math.sqrt(3) / 2 * (self.w - self.v)
        y = self.u - (self.v + self.w) / 2
        return x, y

    def __init__(self, u, v, w):
        (self.u, self.v, self.w) = (u, v, w)

    def __eq__(self, other):
        if not isinstance(other, HexagonalPosition):
            return NotImplemented
        return self.u - other.u == self.v - other.v == self.w - other.w

    def __str__(self):
        return '(u, v, w) = ({0}, {1}, {2})'.format(self.u, self.v, self.w)
