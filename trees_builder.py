import pygame
import random
from trees import Trees


class Tree_collection():
    """"""


    def __init__(self,rpg):

        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()


        self.tree_list = []

        n = 0
        tree_count = 100
        m = tree_count

        while n <= m:
            hold = Trees(rpg)
            self.tree_list.append(hold)
            
            n += 1

    def draw_trees(self):

        """"""
        n = 0
        m = len(self.tree_list) - 1

        while n <= m:
            """"""
            self.tree_list[n].draw_me()
            n += 1