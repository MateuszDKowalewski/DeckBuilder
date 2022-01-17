import pygame

from gameObject import GameObject
from gameScreenCordinateMappers import game_to_screen_coordinate
from gemeConsts import BLUE, SCALE


class Player(GameObject):

    def draw(self, screen):
        position = self.position.to_cartesian_position()
        pygame.draw.circle(screen, BLUE, game_to_screen_coordinate(position[0], position[1]), 0.4 * SCALE)

    def tick(self):
        super().tick()
