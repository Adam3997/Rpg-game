from pygame.sprite import  Sprite
import pygame
import random
from physics_stats import Physics_stats

class Trees(Sprite,Physics_stats):
    """This will be the trees on the map."""





    def __init__(self,rpg):
        """"""
        
        Physics_stats.__init__(self)
        
        super().__init__()
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()

        self.image = pygame.image.load("images1\\used\\tree_2.bmp")
        self.image = pygame.transform.scale_by(self.image,3)
        self.rect = pygame.Rect(0,0,90,350)
        #self.rect_hitbox
        #pygame.Rect.move(self,50,50)
        
        self.rect_image = self.image.get_rect()
        

        x = random.randint(-4000,4000)
        y = random.randint(-4000,4000)
        if -800 <= x <= 800:
            x += random.randint(2000,3000)
        if -800 <= y <= 800:
            y += random.randint(2000,3000)
        self.rect_image.center = (x,y)
        self.rect.center = (x,y)
        #self.rect.centerx += 1500
        #self.rect.centery += 1500

        self.x = self.rect.centerx
        self.y = self.rect.centery
        #self.rect.move(500,500)
        self.rect.centerx += 5
        #self.rect.centery += 100

        self.mass = 8000


    def draw_me(self):
        """"""



        #self.screen.blit(self.flowers[i],self.rect_list[i])
        #pygame.draw.rect(self.screen,'black',rect=self.rect)
        self.screen.blit(self.image,self.rect_image)