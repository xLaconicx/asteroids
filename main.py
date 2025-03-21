import pygame
import sys
print(sys.path)

from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField

print(AsteroidField)

def main():
    pygame.init()

    dt = 0
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #print("Exiting Asteroids!")
                #pygame.quit()
                return
            
        dt = clock.get_time() / 1000
        updatable.update(dt)

        screen.fill((0, 0, 0))

        for entity in drawable:
            if hasattr(entity, "draw"):
                entity.draw(screen)

        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
    