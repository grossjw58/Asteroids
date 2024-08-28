import circleshape
import pygame
import constants
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius > constants.ASTEROID_MIN_RADIUS:
            rand_angle = random.uniform(20,50)
            left_rotated_velocity = self.velocity.rotate(-rand_angle) * 1.2
            right_roated_velocity = self.velocity.rotate(rand_angle) * 1.2
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            first_asteroid = Asteroid(self.position.x,self.position.y,new_radius)
            first_asteroid.velocity = left_rotated_velocity
            second_asteroid = Asteroid(self.position.x,self.position.y,new_radius)
            second_asteroid.velocity = right_roated_velocity
            






