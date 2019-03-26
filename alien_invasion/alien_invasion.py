import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """Initialize the game and build a screen object"""
    pygame.init()

    # get the game settings
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.screen_caption)

    # build a ship instance
    ship = Ship(ai_settings, screen)

    # main loop of the game
    while True:

        # react to the events of the keyboard and mouse
        gf.check_events(ship)

        # update the space position
        ship.update()

        # update the new screen surface
        gf.update_screen(ai_settings, screen, ship)


run_game()