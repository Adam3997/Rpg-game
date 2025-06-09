import random
import pygame
import pygame.locals


class House():
    """"""

    def __init__(self,rpg,location):
        """"""


        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()


        self.house_list = []
        self.house_rect_list = []
        a = pygame.image.load('_internal\\img\\house_1.png')
        self.house_list.append(a)
        a = a.get_rect()
        a.centerx = location[0]
        a.centery = location[1]
        self.house_rect_list.append(a)
        a = pygame.image.load('_internal\\img\\house_attempt_2.png')
        self.house_list.append(a)
        a = a.get_rect()
        a.centerx = location[0]
        a.centery = location[1]
        self.house_rect_list.append(a)
        a = pygame.image.load('_internal\\img\\building_1.png')
        self.house_list.append(a)
        a = a.get_rect()
        a.centerx = location[0]
        a.centery = location[1]
        self.house_rect_list.append(a)




        