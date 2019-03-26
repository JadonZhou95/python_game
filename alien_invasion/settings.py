"""Handle the game settings"""


class Settings():
    """Store all the settings and parameters of the game"""

    def __init__(self):
        # initialize the game settings

        # screen caption
        self.screen_caption = "Alien Invasion"

        # screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed_factor = 1.5