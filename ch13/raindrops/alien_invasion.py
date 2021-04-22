import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Raindrop Invasion")

    # Make a ship, a group of bullets, and a group of raindrops.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    raindrops = Group()

    # Create the fleet of raindrops.
    gf.create_fleet(ai_settings, screen, ship, raindrops)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_raindrops(ai_settings, raindrops)
        gf.update_screen(ai_settings, screen, ship, raindrops, bullets)      
 
run_game()

