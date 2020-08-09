import pygame
from pygame.sprite import Sprite

class Alein(Sprite):
  #a class representing a single alein in fleet

  def __init__(self,ai_settings,screen):
    super(Alein,self).__init__()
    self.screen = screen
    self.ai_settings = ai_settings

    #load the alein image 
    self.image = pygame.image.load('images/alien.bmp')
    self.rect = self.image.get_rect()
    self.screen_rect = self.screen.get_rect()
    self.rect.x = self.rect.width
    self.rect.y = 20

    self.x = float(self.rect.x)

  def blitme(self):
    self.screen.blit(self.image,self.rect)
  
  def check_edges(self):
    if(self.rect.right == self.screen_rect.right ):
      return 1
    elif (self.rect.left == 0):
      return 2
    else:
      return 3
