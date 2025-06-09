import pygame
import random
from trees import Trees


class Tree_collection():
    """This holds a list of trees for the map"""
    def __init__(self,rpg,number_of_trees,x_size,y_size):
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        self.tree_list = []
        n = 0
        tree_count = number_of_trees
        m = tree_count
        while n <= m:
            hold = Trees(rpg,x_size,y_size)
            self.tree_list.append(hold)
            n += 1
    
    def draw_trees(self):
        """Displays all of trees on the screen."""
        n = 0
        m = len(self.tree_list) - 1
        while n <= m:
            self.tree_list[n].draw_me()
            n += 1