import pygame
from pygame.sprite import Sprite


class Decoration(Sprite):
    """This is for stuff in the games graphics. this means things like trees or houses.
    This can also include other things that are depicted graphicly as stuff to look at.
    nothing in here can be fought. there may be limited interactions, like not being
    able to move past an object. These will be drawn on top of the player character 
    to look more immersive."""