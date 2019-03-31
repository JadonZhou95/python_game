import sys
from time import sleep

import pygame

from bullet import Bullet
from aliens import Alien
from button import Button


def check_keydown_events(event, ai_settings, stats, screen, ship, aliens, bullets):
    """Check and handle the keydown events"""
    # ->
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    # <-
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    # space
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    # q: quit
    elif event.key == pygame.K_q:
        sys.exit()
    # a: restart
    elif event.key == pygame.K_a:
        if not stats.game_active:
            stats.reset_stats()
            aliens.empty()
            bullets.empty()
            create_fleet(ai_settings, screen, ship, aliens)
    # s: stop and start
    elif event.key == pygame.K_ESCAPE:
        if stats.ship_left > 0:
            stats.game_pause = not stats.game_pause


def check_keyup_events(event, ship):
    """Check and handle the keyup events"""
    # ->
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    # <-
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, stats, screen, ship, aliens, bullets, buttons):
    """response to the event of the keyboard and mouse"""
    for event in pygame.event.get():
        print(event)

        # check the event type
        # click the X close button
        if event.type == pygame.QUIT:
            sys.exit()

        # keydown events
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, stats, screen, ship, aliens, bullets)

        # keyup events
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        # mouse button down
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, buttons[0], mouse_x, mouse_y)
            check_continue_button(stats, buttons[1], mouse_x, mouse_y)
            check_quit_button(stats, buttons[3], mouse_x, mouse_y)


def check_play_button(stats, play_button, mouse_x, mouse_y):
    """start the game when the player click the play button"""
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.reset_stats()


def check_continue_button(stats, continue_button, mouse_x, mouse_y):
    if continue_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_pause = False


def check_quit_button(stats, quit_button, mouse_x, mouse_y):
    if quit_button.rect.collidepoint(mouse_x, mouse_y):
        sys.exit()

def update_screen(ai_settings, stats, screen, ship, aliens, bullets, buttons):
    """update the screen and switch to the new surface"""
    # redraw the screen for each iteration

    # fill the screen acting like clear the screen,
    # as it will cover the plane drew during last iteration
    screen.fill(ai_settings.bg_color)
    # draw the ship
    ship.blitme()
    # draw the alien
    aliens.draw(screen)

    # draw the bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    if not stats.game_active:
        buttons[0].draw_button()

    if stats.game_pause:
        for button in buttons[1:]:
            button.draw_button()

    # display the new surface
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """update the bullets"""
    bullets.update()

    # remove the dispearing bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """take actions when ship is hit by the aliens"""
    stats.ship_left -= 1

    if stats.ship_left > 0:
        # clear the aliens and bullets
        aliens.empty()
        bullets.empty()

        # create a new fleet of aliens
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        sleep(0.5)
    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """check whether any aliens reach the bottom"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """update the alien states"""

    # check whether the aliens reach the left and right edge of the screen
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # check collision between ship and aliens
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # check whether any aliens reach the screen bottom
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    """fire a bullet"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_alien_number_x(ai_settings, alien):
    """compute the number of aliens in a row"""
    alien_width = alien.rect.width
    available_width = ai_settings.screen_width - 2 * alien_width
    alien_num = int(available_width / (2 * alien_width))

    return alien_num


def get_alien_number_y(ai_settings, alien, ship):
    """compute the number of aliens in a column"""
    alien_height = alien.rect.height
    available_height = ai_settings.screen_height - 3 * alien_height - ship.rect.height
    alien_num = int(available_height / (2 * alien_height))
    return alien_num


def create_alien(ai_settings, screen, alien_num_x, alien_num_y, aliens):
    """create alien and and them in groups"""
    alien = Alien(ai_settings, screen)
    alien.x = alien.rect.x + 2 * alien.rect.width * alien_num_x
    alien.y = alien.rect.y + 2 * alien.rect.height * alien_num_y

    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a group of aliens"""
    # create a alien and compute how many aliens in one row
    # the gap between aliens was set to be alien width
    alien = Alien(ai_settings, screen)
    alien_num_x = get_alien_number_x(ai_settings, alien)
    alien_num_y = get_alien_number_y(ai_settings, alien, ship)
    print(alien_num_x, alien_num_y)

    # create and add each alien
    for row_num in range(alien_num_x):
        for column_num in range(alien_num_y):
            create_alien(ai_settings, screen, row_num, column_num, aliens)


def check_fleet_edges(ai_settings, aliens):
    """check whether the aliens reach the edge and take actions accordingly"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_setting, aliens):
    """take actions when aliens are at the edge"""
    for alien in aliens.sprites():
        alien.y += ai_setting.fleet_drop_speed
        alien.rect.y = alien.y
    ai_setting.fleet_direction *= -1


def get_button_list(ai_settings, screen):
    """create a list of buttons"""
    play_button = Button(ai_settings, screen)
    continue_button = Button(ai_settings, screen)
    restart_button = Button(ai_settings, screen)
    quit_button = Button(ai_settings, screen)

    # button 0
    play_button.prep_msg("Play")

    # button 1
    continue_button.rect.right = continue_button.rect.left - continue_button.rect.width / 2
    continue_button.prep_msg("Continue")

    # button 2
    restart_button.prep_msg("Restart")

    # button 3
    quit_button.rect.left = quit_button.rect.right + quit_button.rect.width / 2
    quit_button.prep_msg("Quit")


    return play_button, continue_button, restart_button, quit_button


