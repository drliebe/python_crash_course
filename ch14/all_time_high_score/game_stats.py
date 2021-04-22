import json

filename = "highscore.json"

class GameStats():
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_setings = ai_settings
        self.reset_stats()
        self.game_active = False

        try:
            with open(filename, 'r') as f_obj:
                high_score = json.load(f_obj)
                self.high_score = high_score
        except FileNotFoundError:
            self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_setings.ship_limit
        self.score = 0
        self.level = 1
    