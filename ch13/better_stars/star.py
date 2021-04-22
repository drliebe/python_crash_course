import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single star in the sky."""

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the star image and set its rect attribute.
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        # Start each new star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the star's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the star at its current location."""
        self.screen.blit(self.image, self.rect)