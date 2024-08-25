import pygame
from constants import *
import player as pl

updateable = pygame.sprite.Group()

def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock: pygame.time.Clock = pygame.time.Clock()
    dt: float = 0
    player: pl.Player = pl.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    updateable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for sprite in updateable:
            sprite.update(dt)
        
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1_000
        
if __name__ == "__main__":
    main()