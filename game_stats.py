class GameStats():
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.score = 0
        self.high_score = 0


    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit