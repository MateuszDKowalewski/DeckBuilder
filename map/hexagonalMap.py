from gameObject import GameObject
from geometry.hexagonalPosition import HexagonalPosition
from map.tile import Tile


class HexagonalMap(GameObject):

    def draw(self, screen):
        for tile in self.tiles:
            tile.draw(screen)

    def __init__(self, position, side_length):
        super(HexagonalMap, self).__init__(position)
        self.tiles = []
        (u, v, w) = (0, 0, 0)
        self.tiles.append(Tile(HexagonalPosition(0, 0, 0), self))
        for i in range(1, side_length):
            u += 1
            for j in range(0, 6):
                for k in range(0, i):
                    position = (HexagonalPosition(u, v, w))
                    self.tiles.append(Tile(position, self))
                    new_positon = {
                        0: (u, v + 1, w),
                        1: (u - 1, v, w),
                        2: (u, v, w + 1),
                        3: (u, v - 1, w),
                        4: (u + 1, v, w),
                        5: (u, v, w - 1)
                    }
                    (u, v, w) = new_positon.get(j)

    def __str__(self):
        response = '[\n\ttiles = {\n'
        for tile in self.tiles:
            response += '\t\t' + tile.__str__() + '\n'
        response += '\t}\n]'
        return response
        