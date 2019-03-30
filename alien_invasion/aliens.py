import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class of alien"""

    def __init__(self, ai_settings, screen):
        """initialize the alien and set its original position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load alien image and set its rect param
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # set the starting position at the top-left corrner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the precise position of the alien
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """display the alien on the screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """update the position of the alien"""
        self.x += self.ai_settings.alien_speed_factor * \
                    self.ai_settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """return True if the alien is at the edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        else:
            return False
