from geometry.hexagonalPosition import HexagonalPosition


class GameObject:

    position = HexagonalPosition(0, 0, 0)

    def draw(self, screen):
        pass

    def tick(self, dt):
        pass

    def __init__(self, position):
        if not isinstance(position, HexagonalPosition):
            raise TypeError("Only HexagonalPosition are allowed")
        self.position = position
