import sys
import pygame

from bullet import Bullet
from raindrop import Raindrop

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


def update_screen(ai_settings, screen, ship, raindrops, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    raindrops.draw(screen)

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

def get_number_raindrops_x(ai_settings, raindrop_width):
    """Determine the number of raindrops that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * raindrop_width
    number_raindrops_x = int(available_space_x / (2 * raindrop_width))
    return number_raindrops_x

def get_number_rows(ai_settings, ship_height, raindrop_height):
    """Determine the nmber of ros of raindrops that fit on the screen."""
    available_space_y = (ai_settings.screen_height 
                         - (3 * raindrop_height) - ship_height)
    number_rows = int(available_space_y / (2 * raindrop_height))
    return number_rows

def create_raindrop(ai_settings, screen, raindrops, raindrop_number, row_number):
    """Create an raindrop and place it in the row."""
    raindrop = Raindrop(ai_settings, screen)
    raindrop_width = raindrop.rect.width
    raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
    raindrop.rect.x = raindrop.x
    raindrop.y = raindrop.rect.height + 2 * raindrop.rect.height * row_number
    raindrop.rect.y = raindrop.y
    raindrops.add(raindrop)

def create_row(ai_settings, screen, raindrops, row_number):
    """Create a single row of raindrops."""
    raindrop = Raindrop(ai_settings, screen)
    number_raindrops_x = get_number_raindrops_x(ai_settings, raindrop.rect.width)
    for raindrop_number in range(number_raindrops_x):
        create_raindrop(ai_settings, screen, raindrops, raindrop_number, 
                        row_number)

def create_fleet(ai_settings, screen, ship, raindrops):
    raindrop = Raindrop(ai_settings, screen)
    number_rows = get_number_rows(ai_settings, ship.rect.height, 
                                  raindrop.rect.height)

    # Create the fleet of raindrops.
    for row_number in range(number_rows):
        create_row(ai_settings, screen, raindrops, row_number)

def check_fleet_edges(ai_settings, screen, raindrops):
    """Respond appropriately if any alies have reached an edge."""
    for raindrop in raindrops.sprites():
        if raindrop.check_edges():
            break

def change_fleet_direction(ai_settings, raindrops):
    """Drop the entire fleet and change the fleet's direction."""
    for raindrop in raindrops.sprites():
        raindrop.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_raindrops(ai_settings, screen, raindrops):
    """
    Check if the fleet is at an edge,
      and then update the positions of all raindrops in the fleet.
    """
    check_fleet_edges(ai_settings, screen, raindrops)
    raindrops.update()

    # Get rid of raindrops that have disappeared.
    removed_raindrops = False
    for raindrop in raindrops.copy():
        if raindrop.rect.top >= ai_settings.screen_height:
            raindrops.remove(raindrop)
            removed_raindrops = True
    if removed_raindrops:
        create_row(ai_settings, screen, raindrops, 0)
