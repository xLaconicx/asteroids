import random

from circleshape import *
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        forward = pygame.Vector2(0, 1)
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        Asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        Asteroid_3 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        Asteroid_2.velocity = self.velocity.rotate(random_angle) * 1.2
        Asteroid_3.velocity = self.velocity.rotate(-random_angle) * 1.2
        for group in self.groups():
            group.add(Asteroid_2)
            group.add(Asteroid_3)
        