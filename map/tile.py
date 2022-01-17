import math
import pygame

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

from gameObject import GameObject
from gameScreenCordinateMappers import game_to_screen_coordinates
from gemeConsts import WHITE


class Tile(GameObject):

    def draw(self, screen):
        points = self.get_vertexes_positions()
        new_points = game_to_screen_coordinates(points)
        pygame.draw.polygon(screen, WHITE, new_points)
        pygame.draw.lines(screen, (0, 0, 0), True, new_points, 3)

    def contains(self, x, y):
        point = Point(x, y)
        polygon = Polygon(self.get_vertexes_positions())
        return polygon.contains(point)

    def get_vertexes_positions(self):
        x, y = self.position.to_cartesian_position()
        a = (x + 0.25, y + math.sqrt(3) * 0.25)
        b = (x - 0.25, y + math.sqrt(3) * 0.25)
        c = (x - 0.5, y)
        d = (x - 0.25, y - math.sqrt(3) * 0.25)
        e = (x + 0.25, y - math.sqrt(3) * 0.25)
        f = (x + 0.5, y)
        return [a, b, c, d, e, f]

    def __eq__(self, other):
        if not isinstance(other, Tile):
            return NotImplemented
        return self.position == other.position

    def __str__(self):
        return '[position = {0}]'.format(self.position.__str__())
