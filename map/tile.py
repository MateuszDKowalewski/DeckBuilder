import math
import pygame

from gameScreenCordinateMappers import game_to_screen_coordinates
from geometry.hexagonalPosition import HexagonalPosition


class Tile:

    def draw(self, screen):
        points = self.get_vertexes_positions()
        new_points = game_to_screen_coordinates(points)
        pygame.draw.polygon(screen, (255, 255, 255), new_points)
        pygame.draw.lines(screen, (0, 0, 0), True, new_points, 3)

    def get_vertexes_positions(self):
        x, y = self.position.to_cartesian_position()
        a = (x + 0.25, y + math.sqrt(3) * 0.25)
        b = (x - 0.25, y + math.sqrt(3) * 0.25)
        c = (x - 0.5, y)
        d = (x - 0.25, y - math.sqrt(3) * 0.25)
        e = (x + 0.25, y - math.sqrt(3) * 0.25)
        f = (x + 0.5, y)
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
