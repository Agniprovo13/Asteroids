from logger import log_event
import pygame, random
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  

    def draw(self, surface):
        # Pygame accepts self.position (Vector2) directly as the center argument
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        # Update vector position directly using velocity vector
        self.position += self.velocity * dt

        # Screen wrap-around using self.position.x and self.position.y
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0

        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
    def split(self):
        self.kill()  # Remove the current asteroid from all groups
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle1 = random.uniform(20, 50)
        self.velocity.rotate(random_angle1)
        self.velocity.rotate(-random_angle1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = 1.2 * self.velocity.rotate(random_angle1)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = 1.2 * self.velocity.rotate(-random_angle1)
