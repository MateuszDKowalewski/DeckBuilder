import sys
import pygame

from map.hexagonalMap import HexagonalMap

RESOLUTION = (900, 500)
WIN = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Deck builder!")

X_OFFSET = 450
Y_OFFSET = 250
SCALE = 70


def main():

    tile_map = HexagonalMap(4)

    while True:
        for event in pygame.event.get():
            handle_quit_event(event)

        WIN.fill((0, 0, 0))
        for tile in tile_map.tiles:
            draw_tile(tile)
        for tile in tile_map.tiles:
            draw_tile_outline(tile)
        pygame.display.flip()


def draw_tile(tile):
    points = tile.get_vertexes_positions()
    new_points = []
    for point in points:
        (x, y) = point
        x = x * SCALE + X_OFFSET
        y = y * SCALE + Y_OFFSET
        new_points.append((x, y))
    pygame.draw.polygon(WIN, (255, 255, 255), new_points)

def draw_tile_outline(tile):
    points = tile.get_vertexes_positions()
    new_points = []
    for point in points:
        (x, y) = point
        x = x * SCALE + X_OFFSET
        y = y * SCALE + Y_OFFSET
        new_points.append((x, y))
    pygame.draw.lines(WIN, (0, 0, 0), True, new_points, 3)


def handle_quit_event(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    main()
