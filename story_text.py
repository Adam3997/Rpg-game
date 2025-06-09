
import pygame
from button import Button

class Story_text():
    """This will hold text and stuff for display during story time."""

    def __init__(self,rpg):
        """Initialize stuff"""
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        #print(pygame.font.get_fonts())
        self.font = pygame.font.SysFont('vinerhanditc',48) # chiller, showcardgothic, oldenglishtext, magneto, vinerhanditc
        self.text_color = rpg.text_color
        self.bg_color = rpg.bg_color
        self.screen_counter = 0
        # creating the story the person will read before playing.
        words1 = """Dawn rises on a smoky day while remnants of past battles linger"""
        words2 = """in the air. The sweet smell of the woods wafts onto Ragnar’s nose.'"""
        words3 = """"Where am i going?" Ragnar wonders to himself."""
        words4 = """Brown tree trunks stand like warriors around the seated Ragnarr,"""
        words5 = """their shadow casting on the grass like doubt in Ragnar’s mind."""
        self.words_1 = self.font.render(words1,True,self.text_color,self.bg_color)
        self.words_2 = self.font.render(words2,True,self.text_color,self.bg_color)
        self.words_3 = self.font.render(words3,True,self.text_color,self.bg_color)
        self.words_4 = self.font.render(words4,True,self.text_color,self.bg_color)
        self.words_5 = self.font.render(words5,True,self.text_color,self.bg_color)
        self.words_1_rect = self.words_1.get_rect()
        self.words_2_rect = self.words_2.get_rect()
        self.words_3_rect = self.words_3.get_rect()
        self.words_4_rect = self.words_4.get_rect()
        self.words_5_rect = self.words_5.get_rect()
        self.words_1_rect.midtop = self.screen_rect.midtop
        self.words_1_rect.centery += 20
        self.words_1_rect.centerx -= 50
        self.words_2_rect.topleft = self.words_1_rect.bottomleft
        self.words_3_rect.topleft = self.words_2_rect.bottomleft
        self.words_4_rect.topleft = self.words_3_rect.bottomleft
        self.words_5_rect.topleft = self.words_4_rect.bottomleft
        self.continue_button = Button(self,'Continue',1)
        self.continue_button.rect.center = self.screen_rect.center
        self.continue_button.prep_msg('Continue')

        # level 2 stuff
        words_level_2_1 = 'Start level 2'
        words_level_2_2 = 'Start level 2'
        words_level_2_3 = 'Start level 2'

        self.words_level_2_part_1 = self.font.render(words_level_2_1,True,self.text_color,self.bg_color)

        self.words_level_2_part_1_rect = self.words_level_2_part_1.get_rect()
        self.words_level_2_part_1_rect.midtop = self.screen_rect.midtop

        self.start_level_2_button = Button(self,'Start',1)
        self.start_level_2_button.rect.center = self.screen_rect.center
        self.start_level_2_button.prep_msg('start')

    def setup_second_story(self):
        """"""
        words1 = """The beast fell and burst into flames. Ragnar looked around himself"""
        words2 = """ and still in the woods, decided to venture on."""
        words3 = """"""
        words4 = """"""
        words5 = """"""
        self.words_1 = self.font.render(words1,True,self.text_color,self.bg_color)
        self.words_2 = self.font.render(words2,True,self.text_color,self.bg_color)
        self.words_3 = self.font.render(words3,True,self.text_color,self.bg_color)
        self.words_4 = self.font.render(words4,True,self.text_color,self.bg_color)
        self.words_5 = self.font.render(words5,True,self.text_color,self.bg_color)
        self.words_1_rect = self.words_1.get_rect()
        self.words_2_rect = self.words_2.get_rect()
        self.words_3_rect = self.words_3.get_rect()
        self.words_4_rect = self.words_4.get_rect()
        self.words_5_rect = self.words_5.get_rect()
        self.words_1_rect.midtop = self.screen_rect.midtop
        self.words_1_rect.centery += 20
        self.words_1_rect.centerx -= 50
        self.words_2_rect.topleft = self.words_1_rect.bottomleft
        self.words_3_rect.topleft = self.words_2_rect.bottomleft
        self.words_4_rect.topleft = self.words_3_rect.bottomleft
        self.words_5_rect.topleft = self.words_4_rect.bottomleft
    
    def setup_third_story(self):
        """"""
        words1 = """Ragnar defeated the spider. he then pulled his spear from"""
        words2 = """the side of the creature. As the blade was removed, blood"""
        words3 = """ spilled forth and darkness filled Ragnar's view."""
        words4 = """When he awoke, he realized the past battles has been a dream."""
        words5 = """"""
        self.words_1 = self.font.render(words1,True,self.text_color,self.bg_color)
        self.words_2 = self.font.render(words2,True,self.text_color,self.bg_color)
        self.words_3 = self.font.render(words3,True,self.text_color,self.bg_color)
        self.words_4 = self.font.render(words4,True,self.text_color,self.bg_color)
        self.words_5 = self.font.render(words5,True,self.text_color,self.bg_color)
        self.words_1_rect = self.words_1.get_rect()
        self.words_2_rect = self.words_2.get_rect()
        self.words_3_rect = self.words_3.get_rect()
        self.words_4_rect = self.words_4.get_rect()
        self.words_5_rect = self.words_5.get_rect()
        self.words_1_rect.midtop = self.screen_rect.midtop
        self.words_1_rect.centery += 20
        self.words_1_rect.centerx -= 50
        self.words_2_rect.topleft = self.words_1_rect.bottomleft
        self.words_3_rect.topleft = self.words_2_rect.bottomleft
        self.words_4_rect.topleft = self.words_3_rect.bottomleft
        self.words_5_rect.topleft = self.words_4_rect.bottomleft
    
    def setup_fourth_story(self):
        """"""
        words1 = """The beast lay slain. Ragnar laughed and saw the"""
        words2 = """darnkess coming. Its cold grip encircling him."""
        words3 = """Ragnar awoke from his sleep. "I must be trapped"."""
        words4 = """"""
        words5 = """"""
        self.words_1 = self.font.render(words1,True,self.text_color,self.bg_color)
        self.words_2 = self.font.render(words2,True,self.text_color,self.bg_color)
        self.words_3 = self.font.render(words3,True,self.text_color,self.bg_color)
        self.words_4 = self.font.render(words4,True,self.text_color,self.bg_color)
        self.words_5 = self.font.render(words5,True,self.text_color,self.bg_color)
        self.words_1_rect = self.words_1.get_rect()
        self.words_2_rect = self.words_2.get_rect()
        self.words_3_rect = self.words_3.get_rect()
        self.words_4_rect = self.words_4.get_rect()
        self.words_5_rect = self.words_5.get_rect()
        self.words_1_rect.midtop = self.screen_rect.midtop
        self.words_1_rect.centery += 20
        self.words_1_rect.centerx -= 50
        self.words_2_rect.topleft = self.words_1_rect.bottomleft
        self.words_3_rect.topleft = self.words_2_rect.bottomleft
        self.words_4_rect.topleft = self.words_3_rect.bottomleft
        self.words_5_rect.topleft = self.words_4_rect.bottomleft

    def setup_fifth_story(self):
        """"""
        words1 = """This time Ragnar was prepared when he defeated the beast."""
        words2 = """"I know what is coming." He yelled."""
        words3 = """"""
        words4 = """"""
        words5 = """"""
        self.words_1 = self.font.render(words1,True,self.text_color,self.bg_color)
        self.words_2 = self.font.render(words2,True,self.text_color,self.bg_color)
        self.words_3 = self.font.render(words3,True,self.text_color,self.bg_color)
        self.words_4 = self.font.render(words4,True,self.text_color,self.bg_color)
        self.words_5 = self.font.render(words5,True,self.text_color,self.bg_color)
        self.words_1_rect = self.words_1.get_rect()
        self.words_2_rect = self.words_2.get_rect()
        self.words_3_rect = self.words_3.get_rect()
        self.words_4_rect = self.words_4.get_rect()
        self.words_5_rect = self.words_5.get_rect()
        self.words_1_rect.midtop = self.screen_rect.midtop
        self.words_1_rect.centery += 20
        self.words_1_rect.centerx -= 50
        self.words_2_rect.topleft = self.words_1_rect.bottomleft
        self.words_3_rect.topleft = self.words_2_rect.bottomleft
        self.words_4_rect.topleft = self.words_3_rect.bottomleft
        self.words_5_rect.topleft = self.words_4_rect.bottomleft


    def setup_sixth_story(self):
        """"""
        words1 = """This time, everything felt different."""
        words2 = """Ragnar looked around him."""
        words3 = '''"Ready."'''
        words4 = """"""
        words5 = """"""
        self.words_1 = self.font.render(words1,True,self.text_color,self.bg_color)
        self.words_2 = self.font.render(words2,True,self.text_color,self.bg_color)
        self.words_3 = self.font.render(words3,True,self.text_color,self.bg_color)
        self.words_4 = self.font.render(words4,True,self.text_color,self.bg_color)
        self.words_5 = self.font.render(words5,True,self.text_color,self.bg_color)
        self.words_1_rect = self.words_1.get_rect()
        self.words_2_rect = self.words_2.get_rect()
        self.words_3_rect = self.words_3.get_rect()
        self.words_4_rect = self.words_4.get_rect()
        self.words_5_rect = self.words_5.get_rect()
        self.words_1_rect.midtop = self.screen_rect.midtop
        self.words_1_rect.centery += 20
        self.words_1_rect.centerx -= 50
        self.words_2_rect.topleft = self.words_1_rect.bottomleft
        self.words_3_rect.topleft = self.words_2_rect.bottomleft
        self.words_4_rect.topleft = self.words_3_rect.bottomleft
        self.words_5_rect.topleft = self.words_4_rect.bottomleft



    def display_story_1(self):
        """This displays the text on screen for the plkyaer to read"""
        self.screen.blit(self.words_1,self.words_1_rect)
        self.screen.blit(self.words_2,self.words_2_rect)
        self.screen.blit(self.words_3,self.words_3_rect)
        self.screen.blit(self.words_4,self.words_4_rect)
        self.screen.blit(self.words_5,self.words_5_rect)
        self.continue_button.draw_button()

    def display_story_2(self):
        """This displays the text on screen for the plkyaer to read"""
        self.screen.blit(self.words_1,self.words_1_rect)
        self.screen.blit(self.words_2,self.words_2_rect)
        self.screen.blit(self.words_3,self.words_3_rect)
        self.screen.blit(self.words_4,self.words_4_rect)
        self.screen.blit(self.words_5,self.words_5_rect)
        self.continue_button.draw_button()
    def display_story_3(self):
        """This displays the text on screen for the plkyaer to read"""
        self.screen.blit(self.words_1,self.words_1_rect)
        self.screen.blit(self.words_2,self.words_2_rect)
        self.screen.blit(self.words_3,self.words_3_rect)
        self.screen.blit(self.words_4,self.words_4_rect)
        self.screen.blit(self.words_5,self.words_5_rect)
        self.continue_button.draw_button()
    def display_story_4(self):
        """This displays the text on screen for the plkyaer to read"""
        self.screen.blit(self.words_1,self.words_1_rect)
        self.screen.blit(self.words_2,self.words_2_rect)
        self.screen.blit(self.words_3,self.words_3_rect)
        self.screen.blit(self.words_4,self.words_4_rect)
        self.screen.blit(self.words_5,self.words_5_rect)
        self.continue_button.draw_button()
    def display_story_5(self):
        """This displays the text on screen for the plkyaer to read"""
        self.screen.blit(self.words_1,self.words_1_rect)
        self.screen.blit(self.words_2,self.words_2_rect)
        self.screen.blit(self.words_3,self.words_3_rect)
        self.screen.blit(self.words_4,self.words_4_rect)
        self.screen.blit(self.words_5,self.words_5_rect)
        self.continue_button.draw_button()
    def display_story_6(self):
        """This displays the text on screen for the plkyaer to read"""
        self.screen.blit(self.words_1,self.words_1_rect)
        self.screen.blit(self.words_2,self.words_2_rect)
        self.screen.blit(self.words_3,self.words_3_rect)
        self.screen.blit(self.words_4,self.words_4_rect)
        self.screen.blit(self.words_5,self.words_5_rect)
        self.continue_button.draw_button()
        



    

    def _check_start_level_2_button(self,rpg, mouse_pos):
        """This checks if the person clickt the continue button"""
        button_clicked = self.start_level_2_button.rect.collidepoint(mouse_pos)
        if button_clicked and rpg.switch_first_to_second_level_screen == True:
            rpg.campagne_mode = True
            #rpg.map_1 = True 
            rpg.switch_first_to_second_level_screen = False
            pygame.mouse.set_visible(False)
    def _check_start_level_3_button(self,rpg, mouse_pos):
        """This checks if the person clickt the continue button"""
        button_clicked = self.start_level_2_button.rect.collidepoint(mouse_pos)
        if button_clicked and rpg.switch_2_to_3_level_screen == True:
            rpg.campagne_mode = True
            #rpg.map_1 = True 
            rpg.switch_2_to_3_level_screen = False
            pygame.mouse.set_visible(False)
    def _check_start_level_4_button(self,rpg, mouse_pos):
        """This checks if the person clickt the continue button"""
        button_clicked = self.start_level_2_button.rect.collidepoint(mouse_pos)
        if button_clicked and rpg.switch_3_to_4_level_screen == True:
            rpg.campagne_mode = True
            #rpg.map_1 = True 
            rpg.switch_3_to_4_level_screen= False
            pygame.mouse.set_visible(False)
    def _check_start_level_5_button(self,rpg, mouse_pos):
        """This checks if the person clickt the continue button"""
        button_clicked = self.start_level_2_button.rect.collidepoint(mouse_pos)
        if button_clicked and rpg.switch_4_to_5_level_screen == True:
            rpg.campagne_mode = True
            #rpg.map_1 = True 
            rpg.switch_first_to_second_level_screen = False
            pygame.mouse.set_visible(False)
    def _check_start_level_6_button(self,rpg, mouse_pos):
        """This checks if the person clickt the continue button"""
        button_clicked = self.start_level_2_button.rect.collidepoint(mouse_pos)
        if button_clicked and rpg.switch_5_to_6_level_screen == True:
            rpg.campagne_mode = True
            #rpg.map_1 = True 
            rpg.switch_5_to_6_level_screen = False
            pygame.mouse.set_visible(False)
    
    def _check_continue_button(self,rpg, mouse_pos):
        """This checks if the person clickt the continue button"""
        button_clicked = self.continue_button.rect.collidepoint(mouse_pos)
        if button_clicked and rpg.campagne_story_1 == True:
            rpg.campagne_mode = True
            rpg.map_1 = True 
            rpg.campagne_story_1 = False
            #pygame.mixer.music.play(-1)
            if 0.2 <= rpg.settings_hold.max_volume:

                pygame.mixer.music.set_volume(0.2)
            else:
                pygame.mixer.music.set_volume(rpg.settings_hold.max_volume)
            pygame.mixer.Sound.stop(rpg.level_stuff.sound_logic.dialogue_1)
            pygame.mouse.set_visible(False)