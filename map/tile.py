from geometry.hexagonalPosition import HexagonalPosition


class Tile:

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
