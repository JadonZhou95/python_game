import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """a class handles spaceship bullet"""

    def __init__(self, ai_settings, screen, ship):
        """initialize a bullet at the ship position"""
        super().__init__()
        self.screen = screen

        # create a bullet and set its position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # setting float of bullet position
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """move the bullet upwards"""
        # update the float of bullet position
        self.y -= self.speed_factor
        # update the bullet position
        self.rect.y = self.y

    def draw_bullet(self):
        # drew bullect onto the screen
        pygame.draw.rect(self.screen, self.color, self.rect)