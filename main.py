import pygame
import sys

from geometry.hexagonalPosition import HexagonalPosition
from map.tile import Tile

RESOLUTION = (900, 500)
WIN = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Deck builder!")

X_OFFSET = 450
Y_OFFSET = 250
SCALE = 50


def main():

    tile = Tile(HexagonalPosition(0, 0, 0))

    while True:
        for event in pygame.event.get():
            handle_quit_event(event)

        WIN.fill((0, 0, 0))
        points = tile.get_vertexes_positions()
        new_points = []
        for point in points:
            (x, y) = point
            x = x * SCALE + X_OFFSET
            y = y * SCALE + Y_OFFSET
            new_points.append((x, y))

        pygame.draw.polygon(WIN, (255, 255, 255), new_points)
        pygame.display.flip()


def handle_quit_event(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    main()
