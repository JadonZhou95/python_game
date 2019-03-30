class GameStates():
    """hold the game info"""

    def __init__(self, ai_settings):
        """initialize system parameters"""
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """initialize changeable system parameters"""
        self.ship_left = self.ai_settings.ship_limit
        self.game_active = True