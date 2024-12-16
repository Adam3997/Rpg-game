#import pygame
#from pygame.sprite import _Group, Sprite

import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    """"""
    def __init__(self,rpg):
        """"""
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        super().__init__()

        self.image = pygame.image.load("images1\ch_1.bmp")
        #self.image_resized = pygame.transform.scale(self.image,(150,250))
        self.image_resized = pygame.transform.scale2x(self.image)
        self.rect = self.image_resized.get_rect()

        self.rect.center = self.screen_rect.center

        self.x = self.rect.x
        self.y = self.rect.y

    def animation(self):
        """This performs the animation of the player."""

    def draw_me(self):
        """"""
        self.screen.blit(self.image_resized,self.rect)

