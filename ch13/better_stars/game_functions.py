import sys
import pygame
from random import randint

from bullet import Bullet
from star import Star

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to key presses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True  
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, stars, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    stars.draw(screen)

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    bullets.update()

        # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if the lmit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)    

def get_number_stars_x(ai_settings, star_width):
    """Determine the number of stars that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * star_width
    number_stars_x = int(available_space_x / (2 * star_width))
    return number_stars_x

def get_number_rows(ai_settings, ship_height, star_height):
    """Determine the nmber of ros of stars that fit on the screen."""
    available_space_y = (ai_settings.screen_height 
                         - (3 * star_height) - ship_height)
    number_rows = int(available_space_y / (2 * star_height))
    return number_rows

def create_star(ai_settings, screen, stars, star_number, row_number):
    """Create a star and place it in the row."""
    star = Star(ai_settings, screen)
    star_width = star.rect.width
    star.x = (star_width + 2 * star_width * star_number 
              + randint(-50, 50))
    star.rect.x = star.x
    star.rect.y = (star.rect.height + 2 * star.rect.height * row_number 
                   + randint(-50, 50))
    stars.add(star)


def create_fleet(ai_settings, screen, ship, stars):
    """Create a full fleet of stars."""
    # Create a star and find the number of stars in a row.
    star = Star(ai_settings, screen)
    number_stars_x = get_number_stars_x(ai_settings, star.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, 
                                  star.rect.height)

    # Create the fleet of stars.
    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            create_star(ai_settings, screen, stars, star_number, 
                         row_number)    