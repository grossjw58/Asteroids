import pygame
from constants import *
import player as pl

def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock: pygame.time.Clock = pygame.time.Clock()
    dt: float = 0
    player: pl.Player = pl.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        player.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1_000
        
if __name__ == "__main__":
    main()