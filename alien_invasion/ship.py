import pygame


class Ship():
    """Handle the ship action"""

    def __init__(self, ai_settings, screen):
        """initialize the spaceship and set its original position"""
        self.screen = screen
        self.ai_setting = ai_settings

        # load the spaceship image and get its bbox
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        # print(self.rect)
        self.screen_rect = screen.get_rect()
        # print(self.screen_rect)

        # put the spaceship at the screen bottom middle
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # float of the centerx
        self.centerx = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """update the position of the ship"""
        if self.moving_right:
            # move the ship to right
            if self.rect.left >= self.screen_rect.right:
                self.rect.right = self.screen_rect.left + 1
                self.centerx = float(self.rect.centerx)
            else:
                self.centerx += self.ai_setting.ship_speed_factor
                self.rect.centerx = int(self.centerx)

        if self.moving_left:
            # moving ship to left
            if self.rect.right <= self.screen_rect.left:
                self.rect.left = self.screen_rect.right - 1
                self.centerx = float(self.rect.centerx)
            else:
                self.centerx -= self.ai_setting.ship_speed_factor
                self.rect.centerx = int(self.centerx)