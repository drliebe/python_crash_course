import pygame

class Daffy():

    def __init__(self, screen):
        """Initialize the Daffy and set his starting position."""
        self.screen = screen

        # Load the Daffy image and get its rect.
        self.image = pygame.image.load('images/daffy.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new Daffy at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the Daffy at its current location."""
        self.screen.blit(self.image, self.rect)