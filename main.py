import pygame
import sys

RESOLUTION = (900, 500)
WIN = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Deck builder!")
rect = pygame.Rect(30, 30, 60, 60)


def main():

    while True:
        for event in pygame.event.get():
            handle_quit_event(event)

        rect.x += 1

        WIN.fill((0, 0, 0))
        pygame.draw.rect(WIN, (255, 0, 0), rect)
        pygame.display.flip()


def handle_quit_event(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    main()
