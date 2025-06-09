import pygame
from button import Button
import random

class Pause_menu():
    """This will be the pause menu and system"""
    
    
    def __init__(self,rpg):
        
        
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.pause_active = False
        self.pause_screen_color = (149,69,53)
        self.pause_screen_font = pygame.font.SysFont('vinerhanditc',20)
        self.text_color = (234,221,202)
        self.hint_font_color = (234,221,202)

        words = 'Game Paused'
        self.pause_words = self.pause_screen_font.render(words,True,self.text_color,self.pause_screen_color)
        self.pause_words_rect = self.pause_words.get_rect()
        self.pause_words_rect.midtop = self.screen_rect.midtop
        self.pause_words_rect.centery += self.screen_height/5

        self.unpause_button = Button(self,'Return to game.',1)
        self.unpause_button.rect.midtop = self.screen_rect.midtop
        self.unpause_button.rect.centery += (2*  self.screen_height/5)
        self.unpause_button.prep_msg('Return to game.')

        self.save_game_button = Button(self,'Save your game.',1)
        self.save_game_button.rect.midtop = self.unpause_button.rect.midbottom
        self.save_game_button.prep_msg('Save your game.')

        self.hint_button = Button(self,'Hint about game.',1)
        self.hint_button.rect.midtop = self.save_game_button.rect.midbottom
        self.hint_button.prep_msg('Hint about game.')

        self.hint_font = pygame.font.SysFont('frenchscript',60)

        self.hint_timer = 10000
        self.hint_timer_old = self.hint_timer

        self.hint_active = False

        self.save_reset = True

        self.hint_list = []
        a = 'Evoke Glory Cross Bowl Pond Plant'
        self.hint_list.append(a)
        a = 'Invoke Glory Cross Pond Pillar Plant'
        self.hint_list.append(a)
        a = 'Evoke War Stone Bowl Pillar Plant'
        self.hint_list.append(a)
        a = 'Invoke War Pillar Pond Stone Plant'
        self.hint_list.append(a)
        a = 'Evoke Life Plant Bowl Pond Stone'
        self.hint_list.append(a)
        a = 'Invoke Life Plant Pond Bowl Stone'
        self.hint_list.append(a)
        a = 'Evoke Knowledge Pond Bowl Stone Plant'
        self.hint_list.append(a)
        a = 'Invoke Knowledge Pond Bowl Plant Stone'
        self.hint_list.append(a)
        a = 'Interact with objects to perform rituals'
        self.hint_list.append(a)
        a = 'Rituals will change the game'
        self.hint_list.append(a)
        a = 'rituals must be performed in the correct order'
        self.hint_list.append(a)
        a = 'A circle of fire defeats any foe'
        self.hint_list.append(a)
        a = 'the boss makes a noise before attacking with fire'
        self.hint_list.append(a)
        a = 'If your low on health, try to evoke life, it gives health'
        self.hint_list.append(a)
        a = 'invoke War to make boss fights more difficult'
        self.hint_list.append(a)


    def prep_hint(self):
        """This preps a hint for display"""
        a = random.choice(self.hint_list)
        self.hint_to_display = self.hint_font.render(a,True,self.hint_font_color,self.pause_screen_color)
        self.hint_to_display_rect = self.hint_to_display.get_rect()
        #self.hint_to_display_rect.center = self.screen_rect.center
        self.hint_to_display_rect.midbottom = self.screen_rect.midbottom

        

    def display_hint(self):
        """This displays a hint on the screen."""
        self.screen.blit(self.hint_to_display,self.hint_to_display_rect)

    def draw_pause_screen(self):
        """This draws the pause screen"""


        self.screen.fill(self.pause_screen_color)
        self.screen.blit(self.pause_words,self.pause_words_rect)
        self.save_game_button.draw_button()
        self.unpause_button.draw_button()
        self.hint_button.draw_button()
        if self.hint_active:
            self.display_hint()
            self.hint_timer -= 1
            if self.hint_timer <= 0:
                self.hint_timer = self.hint_timer_old
                self.hint_active = False
            
            

       

    def check_to_unpause(self,mouse_pos):
        """Checks to return to game and end pause."""
        button_clicked = self.unpause_button.rect.collidepoint(mouse_pos) #
        if button_clicked and (self.pause_active):
            """"""
            self.pause_active = False
            self.reset_save_trigger()
            #print('reached here')
            pygame.mixer.unpause()
            pygame.mouse.set_visible(False)

    def check_to_save(self,rpg,mouse_pos):
        """"""
        button_clicked = self.save_game_button.rect.collidepoint(mouse_pos) #
        if button_clicked and (self.pause_active) and (self.save_reset):
            """"""
            rpg.save_file_1.save_game(rpg)
            self.save_reset = False
            #self.pause_active = False

            # this must save.
    def check_hint_button(self,mouse_pos):
        """"""
        button_clicked = self.hint_button.rect.collidepoint(mouse_pos) #
        if button_clicked and (self.pause_active) and not self.hint_active:
            """"""
            self.hint_active = True
            self.prep_hint()


    def reset_save_trigger(self):
        """Resets the save trigger"""
        self.save_reset = True
