import pygame
from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS, 
    LINE_WIDTH, 
    PLAYER_SHOOT_SPEED, 
    PLAYER_TURN_SPEED, 
    PLAYER_SPEED, 
    PLAYER_SHOOT_COOLDOWN  # Make sure to add this constant in constants.py!
)
from shot import Shot # Note: Ensure your class in shot.py is named appropriately (usually 'Shot')

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0  # 1. Initialize the shoot timer

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt: float) -> None:
        # 2. Decrease the timer every frame
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

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

    def shoot(self):
        # 3. Prevent shooting if the cooldown hasn't finished
        if self.shoot_timer > 0:
            return
        
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN  # Reset the cooldown timer
        
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_position = self.position + forward * (self.radius + 5)
        new_shot = Shot(shot_position.x, shot_position.y)
        new_shot.velocity = forward * PLAYER_SHOOT_SPEED
        return new_shot