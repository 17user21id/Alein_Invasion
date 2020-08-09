import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alein import Alein
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alein Invasion")
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    alien = Alein(ai_settings, screen)
    gf.create_fleet(ai_settings, screen, aliens)
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings,screen,"PLAY!")
    sb = Scoreboard(ai_settings,screen,stats)


    while True:
        gf.check_events(ship,ai_settings,screen,bullets,play_button)
        ship.update(ai_settings)
        for bullet in bullets.sprites():
            bullet.update()  
        for bullet in bullets.sprites():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
     
        gf.update_screen(screen,ship,ai_settings,bullets,aliens,play_button,sb,stats)
        if(ai_settings.gamestate):
         gf.movement(aliens,ai_settings) 

run_game()
