import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def update(self, dt: float) -> None:
        # must override
        pass

    def collides_with(self, other: "CircleShape | pygame.Rect") -> bool:
        if isinstance(other, pygame.Rect):
            other_position = pygame.Vector2(other.center)
            other_radius = 0
        else:
            other_position = other.position
            other_radius = getattr(other, "radius", 0)

        distance = self.position.distance_to(other_position)
        return distance < (self.radius + other_radius)