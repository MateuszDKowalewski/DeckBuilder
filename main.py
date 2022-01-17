import sys
import pygame

from gameScreenCordinateMappers import screen_to_game_coordinates
from gemeConsts import RESOLUTION, WINDOW_NAME, BLACK
from geometry.hexagonalPosition import HexagonalPosition
from map.hexagonalMap import HexagonalMap
from player.player import Player


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(WINDOW_NAME)

        self.player = Player(HexagonalPosition(0, 0, 0))
        self.tile_map = HexagonalMap(4)

        while True:
            for event in pygame.event.get():
                self.handle_quit_event(event)
                self.handle_mouse_click_event(event)

            self.draw()

    def tick(self, dt):
        pass

    def draw(self):
        self.screen.fill(BLACK)
        for tile in self.tile_map.tiles:
            tile.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()

    def handle_mouse_click_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            for tile in self.tile_map.tiles:
                pos = screen_to_game_coordinates(event.pos[0], event.pos[1])
                if tile.contains(pos[0], pos[1]):
                    print(tile)

    def handle_quit_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    Game()
