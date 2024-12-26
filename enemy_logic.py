import pygame
from pygame.sprite import  Sprite
import random

class Overworld_person(Sprite):
    """This is the image of the enemy that shows up on the world map  when you move around the game world."""

    def __init__(self,rpg):
        """"""
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        super().__init__()
        a = [1,2,3,4]
        pick = random.choice(a)
        scale = 3
        match pick:
            case 1:
                """"""
                self.image = pygame.image.load("_internal\img\spider_1.bmp")
                self.image = pygame.transform.scale_by(self.image,scale)
            case 2:
                self.image = pygame.image.load("_internal\img\spider_2.bmp")
                self.image = pygame.transform.scale_by(self.image,scale)
            case 3:
                self.image = pygame.image.load("_internal\img\spider_3.bmp")
                self.image = pygame.transform.scale_by(self.image,scale)
            case 4:
                self.image = pygame.image.load("_internal\img\spider_4.bmp")
                self.image = pygame.transform.scale_by(self.image,scale)
        #self.image = pygame.image.load("images1\peacock.bmp")
        self.rect = self.image.get_rect()

        #self.rect.center = self.screen_rect.center
        
        x = random.randint(-2300,3500)
        y = random.randint(-2300,3500)
        self.rect.center = (x,y)

        self.surface = pygame.Surface((100,100))
        self.surface.fill((0,0,0))
        self.surface.set_colorkey((0,0,0))
        
        self.surface_rect = self.surface.blit(self.image,(-25,-20))

        self.V_x = 0
        self.V_y = 0

        self.dydt = 10
        self.dxdt = 10
        self.dVdt = random.randint(30,100)
        timer = random.randint(50,110)
        self.accelleration_timer = timer


        self.x = self.rect.x
        self.y = self.rect.y

        self.health = 30
    
    def change_accelleration(self):
        """"""
        self.dVdt = random.randint(30,100)

    def move_me(self):
        """"""
        n = random.randint
    def delete_me(self):
        x = -10000
        y = -10000
        self.rect.center = (x,y)
        self.x = self.rect.x
        self.y = self.rect.y
        del self

    def draw_me(self):
        """"""
        self.screen.blit(self.surface,(self.rect.x,self.rect.y))



    def draw_me_2(self):
        """"""
        self.screen.blit(self.surface,(self.rect.x,self.rect.y))