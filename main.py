import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from logger import log_state, log_event
from asteroids import Asteroid
from Asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    game_clock = pygame.time.Clock()
    dt = 0.0

    # Assign class containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # Instantiate using lowercase variable names
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # 1. Update position/state first
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("Collision detected between player and asteroid.")
                log_event("player_hit")
                print("Game Over")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("Collision detected between shot and asteroid.")
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
        # 2. Render frame
        screen.fill("black")
        for drawable_sprite in drawable:
            drawable_sprite.draw(screen)

        pygame.display.flip()
        
        # 3. Control frame rate and calculate delta time
        delta = game_clock.tick(60)
        dt = delta / 1000.0

if __name__ == "__main__":
    main()