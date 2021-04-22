import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # Store a decimal value for the ship's center
        self.center = float(self.rect.centery)

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centery = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)