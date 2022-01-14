from geometry.hexagonalPosition import HexagonalPosition
from map.tile import Tile


class HexagonalMap:
    
    def __init__(self, side_length):
        self.tiles = []
        (u, v, w) = (0, 0, 0)
        step = 0
        self.tiles.append(Tile(HexagonalPosition(0, 0, 0)))
        for i in range(0, side_length):
            for j in range(0, 6):
                for k in range(0, step):
                    position = (HexagonalPosition(u, v, w))
                    self.tiles.append(Tile(position))
                    new_positon = {
                        0: (u, v + 1, w),
                        1: (u - 1, v, w),
                        2: (u, v, w + 1),
                        3: (u, v - 1, w),
                        4: (u + 1, v, w),
                        5: (u, v, w - 1)
                    }
                    (u, v, w) = new_positon.get(j)
            step += 1

    def __str__(self):
        response = '[\n\ttiles = {\n'
        for tile in self.tiles:
            response += '\t\t' + tile.__str__() + '\n'
        response += '\t}\n]'
        return response
        