import pygame
import random

class Town():
    """"""
    def __init__(self,rpg,location):
        """"""

        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()

        self.house_list = []

        a = 0
        b = 5
        while a <= b:
            d = random.randint(-1000,1000)
            e = random.randint(-1000,1000)
            c = Building((location[0] + d,location[1] + e))
            self.house_list.append(c)
            a += 1

    def draw_town(self):
        """"""
        n = 0
        m = len(self.house_list) - 1

        while n <= m:
            self.screen.blit(self.house_list[n].image,self.house_list[n].rect)
            n += 1


class Building():
    """This holds the individual buildings"""

    def __init__(self,location):
        """initialize the buildings"""

        self.image = pygame.image.load("_internal\\img\\house_2.png")
        self.image = pygame.transform.scale_by(self.image,2)
        self.rect = self.image.get_rect()
        self.rect.center = (location[0],location[1])