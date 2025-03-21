from circleshape import *
from constants import *

class Player(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.velocity = pygame.Vector2(0, 1)
        self.timer = 0

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        forward = pygame.Vector2(0, 1)
        self.position += self.velocity * dt
        

        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        if self.timer > 0:
            self.timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer <= 0:
            self.timer = PLAYER_SHOOT_COOLDOWN
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            Shot(self.position.x, self.position.y, SHOT_RADIUS, forward * PLAYER_SHOOT_SPEED)

class Shot(CircleShape, pygame.sprite.Sprite):
    containers = None

    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity
        print(f"Creating shot at {self.position} with velocity {self.velocity}")
        if self.containers:
            for container in self.containers:
                container.add(self)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    