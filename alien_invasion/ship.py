import pygame


class Ship():
    """Handle the ship action"""

    def __init__(self, screen):
        """initialize the spaceship and set its original position"""
        self.screen = screen

        # load the spaceship image and get its bbox
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        print(self.rect)
        self.screen_rect = screen.get_rect()
        print(self.screen_rect)

        # put the spaceship at the screen bottom middle
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)