import pygame
from pygame.sprite import Sprite

class Deck(Sprite):
    """"""

    def __init__(self,rpg,name,damage,armor,heal,limit,duration,description):
        """"""

        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        super().__init__()

        self.name = name
        self.damage = damage
        self.active = False
        self.armor = armor
        self.use_limit = limit
        self.heal = heal
        self.duration = duration
        self.description = description


