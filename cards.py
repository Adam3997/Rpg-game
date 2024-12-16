import pygame
from pygame.sprite import Sprite

class Card(Sprite):
    """"""

    def __init__(self,card_type1,attack,armor,health,agility,intelligence,magic,name):
        """This is a card for players decks. """
        super().__init__()

        self.card_type = card_type1
        self.attack = attack
        self.armor = armor
        self.health = health
        self.agility = agility
        self.intelligence = intelligence
        self.magic = magic
        self.name = name


    def use_card():
        """this uses the card and does the affect."""
        # i will have to make this later as i come up with the implimentation of cards



