import pygame
import sys

# hex_map = HexagonalMap(3)
# print(hex_map)

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")
color = (255, 0, 0)
rect = pygame.Rect(30, 30, 60, 60)


def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        rect.x += 1
        print(rect)

        WIN.fill((0, 0, 0))
        pygame.draw.rect(WIN, color, rect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
