from pygame.sprite import  Sprite
import pygame
import random
from physics_stats import Physics_stats

class Trees(Sprite,Physics_stats):
    """This will be the trees on the map."""
    
    def __init__(self,rpg,x_size,y_size):
        Physics_stats.__init__(self,rpg)
        super().__init__()
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        self.image = pygame.image.load("_internal\\img\\tree1.bmp")
        self.image = pygame.transform.scale_by(self.image,3)
        self.rect = pygame.Rect(0,0,90,250)
        self.rect_image = self.image.get_rect()
        x = random.randint(0 - (x_size / 2),0 + (x_size / 2))
        y = random.randint(0 - (y_size / 2),0 + (y_size / 2))
        while (-800 <= x <= 800) and (-800 <= y <= 800):
            x = random.randint(2000,4000)
            y = random.randint(-4000,-2000)
            #print('while loop')
        self.rect_image.center = (x,y)
        self.rect.center = (x,y)
        self.rect.midbottom = self.rect_image.midbottom
        self.x = self.rect.centerx
        self.y = self.rect.centery
        #self.rect.move(500,500)
        self.rect.centerx += 5
        #self.rect.centery += 100
        self.mass = 8000

    def draw_me(self):
        """Draws a tree."""
        self.screen.blit(self.image,self.rect_image)
        #pygame.draw.rect(self.screen,(200,0,0),self.rect)