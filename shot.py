from circleshape import CircleShape
import pygame
import constants

class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0,1)
        print("A shot was created")
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    
    def update(self, dt):
        self.position += self.velocity * dt