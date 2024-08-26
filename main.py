import pygame
from constants import *
import player as pl
import asteroid 
import asteroidfield
import sys

updateable = pygame.sprite.Group()

def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock: pygame.time.Clock = pygame.time.Clock()
    dt: float = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    pl.Player.containers = (updateable, drawable)
    asteroid.Asteroid.containers = (updateable, drawable, asteroids)
    asteroidfield.AsteroidField.containers = updateable

    player: pl.Player = pl.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field: asteroidfield.AsteroidField = asteroidfield.AsteroidField()

    print(len(updateable))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        for sprite in updateable:
            sprite.update(dt)    

        for roid in asteroids:
            if roid.is_colliding(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")
        
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1_000
        
if __name__ == "__main__":
    main()