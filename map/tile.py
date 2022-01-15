import math

from geometry.hexagonalPosition import HexagonalPosition


class Tile:

    def get_vertexes_positions(self):
        x, y = self.position.to_cartesian_position()
        a = (x + 0.5, y + math.sqrt(3) * 0.5)
        b = (x - 0.5, y + math.sqrt(3) * 0.5)
        c = (x - 1, y)
        d = (x - 0.5, y - math.sqrt(3) * 0.5)
        e = (x + 0.5, y - math.sqrt(3) * 0.5)
        f = (x + 1, y)
        return [a, b, c, d, e, f]

    def __init__(self, position):
        if not isinstance(position, HexagonalPosition):
            raise TypeError("Only HexagonalPosition are allowed")
        self.position = position

    def __eq__(self, other):
        if not isinstance(other, Tile):
            return NotImplemented
        return self.position == other.position

    def __str__(self):
        return '[position = {0}]'.format(self.position.__str__())
