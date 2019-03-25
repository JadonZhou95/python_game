import sys

import pygame

from settings import Settings
from ship import Ship


def run_game():
    """Initialize the game and build a screen object"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # build a ship object
    ship = Ship(screen)

    # main loop of the game
    while True:

        # monitor the event of the keyboard and mouse
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                sys.exit()

        # fill the screen
        screen.fill(ai_settings.bg_color)
        ship.blitme()


        # update the display
        pygame.display.flip()


run_game()