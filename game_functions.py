import sys
import pygame
from bullet import Bullet
from alein import Alein
from time import sleep


def check_events(ship,ai_settings,screen,bullets,play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x , mouse_y = pygame.mouse.get_pos()
            check_play_buttons(play_button,ai_settings,mouse_x, mouse_y)
        
        if event.type == pygame.KEYDOWN and ai_settings.gamestate:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
            if event.key == pygame.K_SPACE:
                if len(bullets) < ai_settings.bullets_allowed:
                  new_bullet = Bullet(ai_settings,screen,ship)
                  bullets.add(new_bullet)
       
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
        




def update_screen(screen,ship,ai_settings,bullets,aleins,play_button,sb,stats):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for alein in aleins:
        alein.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    if(ai_settings.gamestate==False):
        play_button.draw_button()
    sb.prep_score()
    sb.show_score()
    pygame.display.flip()
    collisions = pygame.sprite.groupcollide(bullets, aleins, True, True)
    if collisions:
        for aliens in collisions.values(): 
            stats.score += ai_settings.alien_points * len(aliens)
        sb.prep_score()
        if(stats.score >= stats.high_score):
            stats.high_score = stats.score
        else:
            pass
    if pygame.sprite.spritecollideany(ship, aleins) or check_alein_bottom(aleins,screen):
        ai_settings.ship_limit -= 1
        if(ai_settings.ship_limit >= 1):
            ship_hit(ai_settings,screen,ship,aleins,bullets,stats,sb)
        else:
            ship_hit(ai_settings,screen,ship,aleins,bullets,stats,sb)
            ai_settings.gamestate = False
            ai_settings.ship_limit = 3
            stats.score = 0    
            
    if len(aleins) == 0:
        bullets.empty()
        create_fleet(ai_settings,screen,aleins)

def create_fleet(ai_settings,screen,aleins):
    
    for alein_column_number in range(5):
        for alien_number in range(9):
            alien = Alein(ai_settings, screen)
            alien.x = 60 + (2*alien_number + 1)*alien.rect.width
            alien.y =60 + 30*(alein_column_number+1) + alein_column_number*alien.rect.height
            alien.rect.x = alien.x
            alien.rect.y = alien.y
            aleins.add(alien)

def movement(aleins,ai_settings):
    for alein in aleins:
       if(alein.check_edges() == 1):
            ai_settings.direction = -1*ai_settings.direction
            for alein in aleins:
             alein.rect.x = alein.rect.x - 1 
            for alein in aleins:
             alein.rect.y = alein.rect.y + ai_settings.vertical_speed_factor
       if(alein.check_edges() == 2):
            ai_settings.direction = -1*ai_settings.direction
            for alein in aleins:
             alein.rect.x = alein.rect.x + 1      
            for alein in aleins:
             alein.rect.y = alein.rect.y + ai_settings.vertical_speed_factor
       alein.rect.x = alein.rect.x + ai_settings.direction*ai_settings.alien_speed_factor 
         

def ship_hit(ai_settings,screen,ship,aleins,bullets,stats,sb):
    aleins.empty()
    bullets.empty()
    create_fleet(ai_settings,screen,aleins)
    ship.center_ship()
    sleep(0.5)

def check_alein_bottom(aleins,screen):
    for alein in aleins:
        if alein.rect.bottom >= screen.get_rect().bottom:
           return True
           break 
    return False

def check_play_buttons(play_button,ai_settings,mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        ai_settings.gamestate = True
        