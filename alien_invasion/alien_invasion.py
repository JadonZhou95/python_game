import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from game_states import GameStates
from button import Button

from time import sleep


def run_game():
    """Initialize the game and build a screen object"""
    pygame.init()

    # get the game settings
    ai_settings = Settings()
    stats = GameStates(ai_settings)

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.screen_caption)

    # create a list of buttons
    buttons = gf.get_button_list(ai_settings, screen)

    # build a ship instance
    ship = Ship(ai_settings, screen)
    # build a group to store bullets
    bullets = Group()

    # build a group of aliens
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    # main loop of the game
    while True:

        # react to the events of the keyboard and mouse
        gf.check_events(ai_settings, stats, screen, ship, aliens, bullets, buttons)

        if stats.game_active and not stats.game_pause:
            # update the space position
            ship.update()

            # update the bullet pos and num
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)

            # update the alien num position and game over control
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # update the new screen surface
        gf.update_screen(ai_settings, stats, screen, ship, aliens, bullets, buttons)

        # sleep(0.02)
run_game()