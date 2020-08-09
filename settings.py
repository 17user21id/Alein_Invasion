class Settings():
    def __init__(self):
        self.screen_width = 1080+60+120
        self.screen_height = 700 + 80 
        self.bg_color = (230, 230 ,230)
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 4
        self.alien_speed_factor = 1
        self.direction = 1
        self.vertical_speed_factor = 15
        self.ship_limit = 3
        self.speedup_scale = 1.1
        self.gamestate = False
        self.alien_points = 50
        self.initialize_dynamic_settings()
        

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        
    def increase_speed(self):
        self.ship_speed_factor *= 1.5
        self.bullet_speed_factor *= 3
        self.alien_speed_factor *= 1