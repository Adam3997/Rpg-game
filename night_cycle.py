import pygame
from shadow_gfx import Shadow_gfx


class Night_cycle():
    """This will hold the class that does day and night cycles"""


    def __init__(self,rpg):
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()




        self.shadow_overlay = Shadow_gfx(rpg,'shadow')
        self.day_night_timer = 5000
        self.day_night_timer_old = self.day_night_timer
        self.night_time = False

    def day_night_cycle(self,rpg):
        """This contains the day night loop logic"""
        self.day_night_time_control()
        self.check_and_display_night(rpg)

    def check_and_display_night(self,rpg):
        """This checks if its night and then displays the darkness"""
        if self.night_time == True:
            self.shadow_overlay.draw_shadowy_overlay(rpg)

    def day_night_time_control(self):
        """This will count down and reset timer"""

        self.day_night_timer -= 1
        if (self.day_night_timer < 0) and self.night_time == False:
            self.night_time = True
            self.day_night_timer = self.day_night_timer_old
            self.shadow_overlay.counter = 0
        elif (self.day_night_timer < 0) and self.night_time == True:    
            self.shadow_overlay.backwards = True
            #self.shadow_overlay.counter = 0
            self.day_night_timer = self.day_night_timer_old