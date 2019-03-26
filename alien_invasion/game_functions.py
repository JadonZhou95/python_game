import sys

import pygame


def check_events(ship):
    """response to the event of the keyboard and mouse"""
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            sys.exit()

        # type and key
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

            elif event.key == pygame.K_q:
                sys.exit()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """update the screen and switch to the new surface"""
    # redraw the screen for each iteration

    # fill the screen acting like clear the screen,
    # as it will cover the plane drew during last iteration
    screen.fill(ai_settings.bg_color)
    # draw the ship
    ship.blitme()

    # display the new surface
    pygame.display.flip()