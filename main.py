import sys
import pygame

from gemeConsts import RESOLUTION, SCALE, X_OFFSET, Y_OFFSET, WINDOW_NAME
from map.hexagonalMap import HexagonalMap

WINDOW = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption(WINDOW_NAME)


def main():
    tile_map = HexagonalMap(4)

    while True:
        for event in pygame.event.get():
            handle_quit_event(event)

        draw(tile_map)


def draw(tile_map):
    WINDOW.fill((0, 0, 0))
    for tile in tile_map.tiles:
        draw_tile(tile)
    pygame.display.flip()


def draw_tile(tile):
    points = tile.get_vertexes_positions()
    new_points = game_to_screen_coordinates(points)
    pygame.draw.polygon(WINDOW, (255, 255, 255), new_points)
    pygame.draw.lines(WINDOW, (0, 0, 0), True, new_points, 3)


def game_to_screen_coordinates(points):
    new_points = []
    for point in points:
        (x, y) = point
        x = x * SCALE + X_OFFSET
        y = - y * SCALE + Y_OFFSET
        new_points.append((x, y))
    return new_points


def handle_quit_event(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    main()
