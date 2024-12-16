import pygame
from pygame.sprite import  Sprite
import random

class Overworld_person(Sprite):
    """"""

    def __init__(self,rpg):
        """"""
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        super().__init__()
        a = [1,2,3,4]
        pick = random.choice(a)
        match pick:
            case 1:
                """"""
                self.image = pygame.image.load("images1\peacock_good.bmp")
            case 2:
                self.image = pygame.image.load("images1\chess_good.bmp")
            case 3:
                self.image = pygame.image.load("images1\cat_1_good.bmp")
            case 4:
                self.image = pygame.image.load("images1\dog_1_good.bmp")
        #self.image = pygame.image.load("images1\peacock.bmp")
        self.rect = self.image.get_rect()

        #self.rect.center = self.screen_rect.center
        
        x = random.randint(-2300,3500)
        y = random.randint(-2300,3500)
        self.rect.center = (x,y)
        


        self.x = self.rect.x
        self.y = self.rect.y
        
    def delete_me(self):
        x = -10000
        y = -10000
        self.rect.center = (x,y)
        self.x = self.rect.x
        self.y = self.rect.y
        del self

    def draw_me(self):
        """"""
        self.screen.blit(self.image,self.rect)