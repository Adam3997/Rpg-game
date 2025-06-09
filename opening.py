from button import Button
import pygame
from enemy_logic import Overworld_person
from trees import Trees
import json
from pathlib import Path

class Opening():
    """this will be the opening menu"""


    """rgb(73, 16, 16)
rgb(45, 73, 16)
rgb(16, 73, 73)
rgb(45, 16, 73)
a set of tetradic colors

rgb
rgb(33, 82, 31)
rgb(31, 59, 82)
rgb(80, 31, 82)
rgb(82, 54, 31)
set 2
i will start with set 2. which is green as color 1. color 4 is brown"""

    def __init__(self,rpg):
        """Initialize the menu"""
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        quarter = self.screen.get_rect().height
        quarter /= 4

        self.width_screen = self.screen.get_rect().width
        self.height_screen = self.screen.get_rect().height

        self.dark_bown = (92,64,51)
        self.cofee_brown = (111,78,55)
        self.fallow_brown = (193,154,107)
        self.mocha_brown = (150,121,105)
        self.mocha_brown_faded = (150,121,105,150)
        self.tan_brown = (210,180,140)
        self.wine_brown = (114,47,55)

        self.color_text = (112,14,8)
        self.color_text_background = (112,66,8)
        
        self.credit_spider = Overworld_person(rpg,'spider')
        self.tree_credit = Trees(rpg,10,10)
        
        self.top_margin = 50
        self.left_margin = 250
        self.space_margin = 200
        self.past_image_margin = 150 + self.left_margin
        self.text_image_offset = 50

        #self.margin_credits = 250

        self.opening_menu = False
        self.settings_menu = False
        self.top_scores_menu = False
        self.credits_screen = False
        self.title_screen = False

        self.start_stuff = True
        self.start_screen_1 = True
        self.start_screen_1_timer = 400
        self.start_screen_1_timer_old = self.start_screen_1_timer
        self.start_screen_2 = False
        self.start_screen_2_timer = 500
        self.start_screen_2_timer_old = self.start_screen_2_timer
        self.start_screen_3 = False
        self.start_screen_3_timer = 400
        self.start_screen_3_timer_old = self.start_screen_3_timer
        self.title_screen_timer = 500
        self.title_screen_timer_old = self.title_screen_timer


        pygame.mouse.set_visible(False)

        # buttons below
        self.start_campagne_button = Button(self,'New Game',3)
        self.start_campagne_button.rect.center = self.screen_rect.center
        self.start_campagne_button.rect.y -= 200
        self.start_campagne_button.prep_msg('New Game')

        self.pygame_logo = pygame.image.load('_internal\\img\\pygame_logo.png')
        self.pygame_logo_rect = self.pygame_logo.get_rect()
        self.pygame_logo_rect.center = self.screen_rect.center
        self.pygame_logo_rect.centery -= quarter

        self.sunset_logo = pygame.image.load('_internal\\img\\walkway_image_2.png')
        self.sunset_logo_rect = self.sunset_logo.get_rect()
        self.sunset_logo_rect.center = self.screen_rect.center
        self.font_sunset_logo = pygame.font.SysFont('vinerhanditc',48)
        self.text_sunset_logo = self.font_sunset_logo.render('Walkway Games',True,self.tan_brown,self.mocha_brown)
        self.text_sunset_logo_rect = self.text_sunset_logo.get_rect()
        self.text_sunset_logo_rect.center = self.screen_rect.center
        
        self.text_sunset_logo_rect.centery -= quarter

        self.font_credits = pygame.font.SysFont('bell',20)
        self.player_credits_text = self.font_credits.render('shadow/adult/shadow: - drjamgo@hotmail.com',True,self.tan_brown,self.mocha_brown)
        self.player_credits_text2 = self.font_credits.render('body/bodies/male/light: - bluecarrot16, JaidynReiman, Benjamin K. Smith (BenCreating), Evert,Eliza Wyatt (ElizaWy),',True,self.tan_brown,self.mocha_brown)
        self.player_credits_text2_2 = self.font_credits.render('TheraHedwig, MuffinElZangano, DurraniJohannes Sjölund (wulax), Stephen Challener (Redshrike)',True,self.tan_brown,self.mocha_brown)
        self.player_credits_text3 = self.font_credits.render('head/heads/human/male/light: - bluecarrot16, Benjamin K. Smith (BenCreating), Stephen Challener (Redshrike)',True,self.tan_brown,self.mocha_brown)
        self.player_credits_text4 = self.font_credits.render('beards/mustache/basic/blonde: - JaidynReiman, Carlo Enrico Victoria (Nemisys)',True,self.tan_brown,self.mocha_brown)
        self.player_credits_text5 = self.font_credits.render('hair/messy1/male/blonde: - Manuel Riecke (MrBeast)',True,self.tan_brown,self.mocha_brown)
        self.player_credits_text6 = self.font_credits.render('torso/chainmail/male/gray: - Johannes Sjölund (wulax)',True,self.tan_brown,self.mocha_brown)
        self.player_credits_text7 = self.font_credits.render('legs/pants2/male/leather: - JaidynReiman, ElizaWy, Bluecarrot16, Johannes Sjölund (wulax), Stephen Challener (Redshrike)',True,self.tan_brown,self.mocha_brown)
        self.player_credits_text8 = self.font_credits.render('feet/boots/revised/male/black: - JaidynReiman ElizaWyBluecarrot16Stephen Challener (Redshrike)Johannes Sjölund (wulax)',True,self.tan_brown,self.mocha_brown)
        self.player_credits_text9 = self.font_credits.render('weapon/polearm/spear/foreground/medium: - Pierre Vigier (pvigier), Johannes Sjölund (wulax), Inboxninja',True,self.tan_brown,self.mocha_brown)
        self.player_credits_text10 = self.font_credits.render('weapon/polearm/spear/background/medium: - Pierre Vigier (pvigier), Johannes Sjölund (wulax), Inboxninja',True,self.tan_brown,self.mocha_brown)
        
        self.player_credits_text_rect = self.player_credits_text.get_rect()
        self.player_credits_text_rect2 = self.player_credits_text2.get_rect()
        self.player_credits_text_rect2_2 = self.player_credits_text2_2.get_rect()
        self.player_credits_text_rect3 = self.player_credits_text3.get_rect()
        self.player_credits_text_rect4 = self.player_credits_text4.get_rect()
        self.player_credits_text_rect5 = self.player_credits_text5.get_rect()
        self.player_credits_text_rect6 = self.player_credits_text6.get_rect()
        self.player_credits_text_rect7 = self.player_credits_text7.get_rect()
        self.player_credits_text_rect8 = self.player_credits_text8.get_rect()
        self.player_credits_text_rect9 = self.player_credits_text9.get_rect()
        self.player_credits_text_rect10 = self.player_credits_text10.get_rect()
        
        
        self.player_credits_text_rect.topleft = self.screen_rect.topleft
        self.player_credits_text_rect.x += self.past_image_margin
        self.player_credits_text_rect.y += self.top_margin #+ self.text_image_offset 
        self.player_credits_text_rect2.topleft = self.player_credits_text_rect.bottomleft
        self.player_credits_text_rect2_2.topleft = self.player_credits_text_rect2.bottomleft
        self.player_credits_text_rect3.topleft = self.player_credits_text_rect2_2.bottomleft
        self.player_credits_text_rect4.topleft = self.player_credits_text_rect3.bottomleft
        self.player_credits_text_rect5.topleft = self.player_credits_text_rect4.bottomleft
        self.player_credits_text_rect6.topleft = self.player_credits_text_rect5.bottomleft
        self.player_credits_text_rect7.topleft = self.player_credits_text_rect6.bottomleft
        self.player_credits_text_rect8.topleft = self.player_credits_text_rect7.bottomleft
        self.player_credits_text_rect9.topleft = self.player_credits_text_rect8.bottomleft
        self.player_credits_text_rect10.topleft = self.player_credits_text_rect9.bottomleft

        self.font_credits = pygame.font.SysFont('bell',28)

        self.spider_credits_text = self.font_credits.render('Stephen "Redshrike" Challener as graphic artist and William.Thompsonj as contributor.',True,self.tan_brown,self.mocha_brown)
        self.spider_credits_text_rect = self.spider_credits_text.get_rect()
        self.spider_credits_text_rect.topleft =  self.screen_rect.topleft
        self.spider_credits_text_rect.x += (self.past_image_margin)
        self.spider_credits_text_rect.y += (self.top_margin + (2 * self.space_margin) + self.text_image_offset)

        self.a = self.left_margin
        self.b = self.top_margin + (2 * self.space_margin) 
        #self.spider_credits_text_rect.x -= 150


        self.a_player = self.left_margin # this is x and b is y
        self.b_player = self.top_margin 

        self.tree_credit.rect_image.topleft = self.screen_rect.topleft
        self.tree_credit.rect_image.centery += ((3 * self.space_margin )+ self.top_margin)
        self.tree_credit.rect_image.centerx += (self.left_margin)
        self.tree_credit.image = pygame.transform.scale_by(self.tree_credit.image,0.25)
        
        #LPC C.Nilsson (2D art)
        #Daniel Eddeland 
        #Lanea Zimmerman (AKA Sharm)
        # this is the credits for trees and in game items.
        self.tree_text_credit = self.font_credits.render('LPC C.Nilsson (2D art),Daniel Eddel, and Lanea Zimmerman (AKA Sharm)',True,self.tan_brown,self.mocha_brown)
        self.tree_text_credit_rect = self.tree_text_credit.get_rect()
        self.tree_text_credit_rect.topleft = self.screen_rect.topleft
        self.tree_text_credit_rect.y += (self.top_margin + self.text_image_offset + self.space_margin * 3)
        self.tree_text_credit_rect.x += self.past_image_margin


        self.bigger_font = pygame.font.SysFont('bell',50)
        self.art_contributions_text = self.bigger_font.render('Art Credits',True,self.tan_brown,self.mocha_brown)
        self.art_contributions_text_2 = self.bigger_font.render('Thanks!',True,self.tan_brown,self.mocha_brown)
        self.art_contributions_text_rect = self.art_contributions_text.get_rect()
        self.art_contributions_text_rect_2 = self.art_contributions_text_2.get_rect()
        self.art_contributions_text_rect.topright = self.screen_rect.topright
        self.art_contributions_text_rect.y += 400
        self.art_contributions_text_rect.x -= 20
        self.art_contributions_text_rect_2.midtop = self.art_contributions_text_rect.midbottom


        self.main_menu_load_campagne_button = Button(rpg,'Load Game',3)
        self.main_menu_load_campagne_button.rect.centerx += (2 * self.width_screen/5)
        self.main_menu_load_campagne_button.rect.centery += (2 * self.height_screen/6)
        
        self.settings_button = Button(rpg,'Settings',3)

        self.credits_button = Button(rpg,'Credits',3)

        self.quit_button = Button(rpg,'Quit Game',3)
        
        self.top_scores_button = Button(rpg,'Top Scores',3)
        
        self.rect_width = 2

        self.sunset_text_border = pygame.Surface((self.text_sunset_logo_rect.width,self.text_sunset_logo_rect.height))
        self.sunset_text_border.set_colorkey((255,255,255))
        self.sunset_text_border.fill((255,255,255))
        pygame.draw.rect(self.sunset_text_border,(self.wine_brown),self.sunset_text_border.get_rect(),self.rect_width,2)
        # testing making an outline    self.screen.get_rect().width
        
        
        self.rectangle_surface_1 = pygame.Surface((self.main_menu_load_campagne_button.rect.width,self.main_menu_load_campagne_button.rect.height))
        
        self.rectangle_surface_1.set_colorkey((255,255,255))
        self.rectangle_surface_1.fill((255,255,255))
        pygame.draw.rect(self.rectangle_surface_1,(self.wine_brown),self.rectangle_surface_1.get_rect(),self.rect_width,5)

        self.rectangle_surface_2 = pygame.Surface((self.start_campagne_button.rect.width,self.start_campagne_button.rect.height))
        self.rectangle_surface_2.set_colorkey((255,255,255))
        self.rectangle_surface_2.fill((255,255,255))
        pygame.draw.rect(self.rectangle_surface_2,self.wine_brown,self.rectangle_surface_2.get_rect(),self.rect_width,5)

        self.rectangle_surface_3 = pygame.Surface((self.settings_button.rect.width,self.settings_button.rect.height))
        self.rectangle_surface_3.set_colorkey((255,255,255))
        self.rectangle_surface_3.fill((255,255,255))
        pygame.draw.rect(self.rectangle_surface_3,self.wine_brown,self.rectangle_surface_3.get_rect(),self.rect_width,5)

        self.rectangle_surface_4 = pygame.Surface((self.quit_button.rect.width,self.quit_button.rect.height))
        self.rectangle_surface_4.set_colorkey((255,255,255))
        self.rectangle_surface_4.fill((255,255,255))
        pygame.draw.rect(self.rectangle_surface_4,self.wine_brown,self.rectangle_surface_4.get_rect(),self.rect_width,5)

        self.rectangle_surface_5 = pygame.Surface((self.credits_button.rect.width,self.credits_button.rect.height))
        self.rectangle_surface_5.set_colorkey((255,255,255))
        self.rectangle_surface_5.fill((255,255,255))
        pygame.draw.rect(self.rectangle_surface_5,self.wine_brown,self.rectangle_surface_5.get_rect(),self.rect_width,5)

        self.rectangle_surface_6 = pygame.Surface((self.top_scores_button.rect.width,self.top_scores_button.rect.height))
        self.rectangle_surface_6.set_colorkey((255,255,255))
        self.rectangle_surface_6.fill((255,255,255))
        pygame.draw.rect(self.rectangle_surface_6,self.wine_brown,self.rectangle_surface_6.get_rect(),self.rect_width,5)

        margin_buttons = 20
        self.start_campagne_button.rect.topleft = self.main_menu_load_campagne_button.rect.bottomleft
        self.start_campagne_button.rect.y += margin_buttons
        self.settings_button.rect.topleft = self.start_campagne_button.rect.bottomleft
        self.settings_button.rect.y += margin_buttons
        self.credits_button.rect.topleft = self.settings_button.rect.bottomleft
        self.credits_button.rect.y += margin_buttons
        self.top_scores_button.rect.topleft = self.credits_button.rect.bottomleft
        self.top_scores_button.rect.y += margin_buttons
        self.quit_button.rect.topleft = self.top_scores_button.rect.bottomleft
        self.quit_button.rect.y += margin_buttons

        self.main_menu_load_campagne_button.prep_msg('Load Game')
        self.start_campagne_button.prep_msg('New Game')
        self.settings_button.prep_msg('Settings')
        self.credits_button.prep_msg('Credits')
        self.top_scores_button.prep_msg('Top Scores')
        self.quit_button.prep_msg('Quit Game')


        self.return_main_menu_button = Button(rpg,'Return',3)
        self.return_main_menu_button.rect.midbottom = self.screen_rect.midbottom
        self.return_main_menu_button.rect.y -= self.top_margin
        self.return_main_menu_button.prep_msg('Return')


        self.game_name_font = pygame.font.SysFont('vinerhanditc',120)
        self.game_name = self.game_name_font.render('The Wind Whispers for War',True,self.wine_brown,self.mocha_brown)
        self.game_name_rect = self.game_name.get_rect()
        r = 0
        s = 20
        self.rect_list_for_intro_design = []
        while r <= s:
            t = self.game_name_rect.scale_by((0.1 + (r/15)),(1 + (r/15)))
            self.rect_list_for_intro_design.append(t)
            r += 1
        self.rect_list_for_intro_design.reverse()
        self.game_name_rect_bigger = self.game_name_rect.scale_by(1.5,1.5)
        self.game_name_rect.midtop = self.screen_rect.midtop
        self.game_name_rect.y += self.top_margin
        self.game_name_rect_bigger.center = self.game_name_rect.center
        self.game_name_surface = pygame.Surface((self.game_name_rect.width,self.game_name_rect.height))
        self.game_name_surface.blit(self.game_name,(0,0))
        self.game_name_surface.set_colorkey(self.mocha_brown)



    def draw_start_screen_1(self,rpg):
        """This will be pygame logo"""
        self.screen.fill(self.dark_bown)
        self.screen.blit(self.pygame_logo,self.pygame_logo_rect)

        
        

    def draw_start_screen_2(self,rpg):
        """This will be the credits for art"""
        self.screen.fill(self.cofee_brown)
        #self.screen.blit(self.sunset_logo,self.sunset_logo_rect)
        quarter = self.screen.get_rect().height
        quarter /= 4
        rpg.level_stuff.player_1.draw_for_credits((self.a_player),(self.b_player))
        self.screen.blit(self.player_credits_text,self.player_credits_text_rect)
        self.screen.blit(self.player_credits_text2,self.player_credits_text_rect2)
        self.screen.blit(self.player_credits_text2_2,self.player_credits_text_rect2_2)
        self.screen.blit(self.player_credits_text3,self.player_credits_text_rect3)
        self.screen.blit(self.player_credits_text4,self.player_credits_text_rect4)
        self.screen.blit(self.player_credits_text5,self.player_credits_text_rect5)
        self.screen.blit(self.player_credits_text6,self.player_credits_text_rect6)
        self.screen.blit(self.player_credits_text7,self.player_credits_text_rect7)
        self.screen.blit(self.player_credits_text8,self.player_credits_text_rect8)
        self.screen.blit(self.player_credits_text9,self.player_credits_text_rect9)
        self.screen.blit(self.player_credits_text10,self.player_credits_text_rect10)        

        self.credit_spider.draw_for_credits((self.a,self.b))
        self.screen.blit(self.spider_credits_text,self.spider_credits_text_rect)

        # trees
        self.tree_credit.draw_me()
        self.screen.blit(self.tree_text_credit,self.tree_text_credit_rect)

        self.screen.blit(self.art_contributions_text,self.art_contributions_text_rect)
        self.screen.blit(self.art_contributions_text_2,self.art_contributions_text_rect_2)




    def draw_start_screen_3(self,rpg):
        """This will be game logo thing or something else"""
        self.screen.fill(self.mocha_brown)
        self.screen.blit(self.sunset_logo,self.sunset_logo_rect)
        self.screen.blit(self.text_sunset_logo,self.text_sunset_logo_rect)
        self.screen.blit(self.sunset_text_border,self.text_sunset_logo_rect)
    
    def draw_opening_menu(self,rpg):
        """this draws the main menu"""

        if self.opening_menu:
            self.screen.fill(self.fallow_brown)
            self.screen.blit(self.game_name_surface,self.game_name_rect)
            self.start_campagne_button.draw_button()
            self.main_menu_load_campagne_button.draw_button()
            self.settings_button.draw_button()
            self.credits_button.draw_button()
            self.top_scores_button.draw_button()
            self.quit_button.draw_button()
            self.screen.blit(self.rectangle_surface_1,self.main_menu_load_campagne_button.rect)
            self.screen.blit(self.rectangle_surface_2,self.start_campagne_button.rect)
            self.screen.blit(self.rectangle_surface_3,self.settings_button.rect)
            self.screen.blit(self.rectangle_surface_4,self.quit_button.rect)
            self.screen.blit(self.rectangle_surface_5,self.credits_button.rect)
            self.screen.blit(self.rectangle_surface_6,self.top_scores_button.rect)
        

    def draw_top_scores_screen(self,rpg):
        """This draws on credits screen"""
        self.screen.fill(self.fallow_brown)
        self.return_main_menu_button.draw_button()

    def draw_settings_screen(self,rpg):
        """This draws on credits screen"""
        self.screen.fill(self.fallow_brown)
        rpg.settings_hold.draw_settings_screen(rpg)
        self.return_main_menu_button.draw_button()
        pygame.draw.rect(self.screen,(100,100,100),self.return_main_menu_button.msg_image_rect,5)

    def draw_credits_screen(self,rpg):
        """This draws on credits screen"""
        #self.screen.fill(self.fallow_brown)
        self.draw_start_screen_2(rpg)
        self.return_main_menu_button.draw_button()
    
    def draw_title_screen(self):
        """"""
        self.screen.fill(self.fallow_brown)
        #pygame.draw.ellipse(self.screen,self.dark_bown,self.game_name_rect_bigger)
        n = 0
        m = len(self.rect_list_for_intro_design) - 1
        while n <= m:
            self.rect_list_for_intro_design[n].center = self.game_name_rect.center
            a = (150 + (n*2) + 1)
            b = (121 + (n * 2) + 1)
            c = (105 +  (n * 2) + 1)
            if a > 255:
                a = 255
            if b > 255:
                b = 255
            if c > 255:
                c = 255
            pygame.draw.ellipse(self.screen,(a, b, c),self.rect_list_for_intro_design[n])
            n += 1
        #pygame.draw.ellipse(self.screen,self.mocha_brown,self.game_name_rect)
        self.screen.blit(self.game_name_surface,self.game_name_rect)
        
    def _check_campagne_button(self,rpg,mouse_pos):
        """This checks if you want to start a campagne"""
        button_clicked = self.start_campagne_button.msg_image_rect.collidepoint(mouse_pos)
        if button_clicked and self.opening_menu == True:
            rpg.level_stuff.load_level_1(rpg)
            rpg.campagne_mode = False
            self.opening_menu = False
            rpg.map_1 = False 
            rpg.campagne_story_1 = True
            pygame.mixer.music.play(-1)
            rpg.level_stuff.sound_logic.dialogue_1.set_volume(rpg.settings_hold.dialogue_volume * rpg.settings_hold.max_volume)

            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.dialogue_1)
            

    def _check_return_button(self,rpg,mouse_pos):
        """This checks if you want to return"""
        button_clicked = self.return_main_menu_button.msg_image_rect.collidepoint(mouse_pos)
        if button_clicked and (self.credits_screen or self.top_scores_menu or self.settings_menu):
            self.opening_menu = True
            self.credits_screen = False
            self.top_scores_menu = False
            if self.settings_menu:
                rpg.level_stuff.sound_logic.update_sound_levels(rpg)
                self.settings_menu = False
            



    def _check_load_button(self,rpg,mouse_pos):
        """This checks if you want to load an existing game"""
        button_clicked = self.main_menu_load_campagne_button.msg_image_rect.collidepoint(mouse_pos)
        if button_clicked and self.opening_menu == True:
            """Need to create logic for loading game"""
            # this will be filled in when the code is done!
            rpg.level_stuff.load_game_skip(rpg)


    def _check_settings_button(self,rpg,mouse_pos):
        """This checks if you want to load an existing game"""
        button_clicked = self.settings_button.msg_image_rect.collidepoint(mouse_pos)
        if button_clicked and self.opening_menu == True:
            """Need to create logic for settings screen"""
            # this will be filled in when the code is done!
            self.opening_menu = False
            self.settings_menu = True

    def _check_credits_button(self,rpg,mouse_pos):
        """This checks if you want to load an existing game"""
        button_clicked = self.credits_button.msg_image_rect.collidepoint(mouse_pos)
        if button_clicked and self.opening_menu == True:
            """Need to create logic for displating credits"""
            self.credits_screen = True
            self.opening_menu = False
            #self.credits_screen = True

    def _check_top_scores_button(self,rpg,mouse_pos):
        """This checks if you want to load an existing game"""
        button_clicked = self.top_scores_button.msg_image_rect.collidepoint(mouse_pos)
        if button_clicked and self.opening_menu == True:
            """Need to create logic for top scores in the game"""
            self.top_scores_menu = True
            self.opening_menu = False

    def _check_quit_game_button(self,rpg,mouse_pos):
        """This checks if you want to load an existing game"""
        button_clicked = self.quit_button.msg_image_rect.collidepoint(mouse_pos)
        if button_clicked and self.opening_menu == True:
            """Need to create logic for quit game"""
            rpg.game = False


    def intro_screen_logic(self,rpg):
        """This cycles the introduction screen"""
        
        if self.start_screen_1:
            self.draw_start_screen_1(rpg)
            self.start_screen_1_timer -= 1
            if self.start_screen_1_timer <= 0:
                self.start_screen_1_timer = self.start_screen_1_timer_old
                self.start_screen_1 = False
                self.start_screen_2 = True
        if self.start_screen_2:
            self.draw_start_screen_2(rpg)
            self.start_screen_2_timer -= 1
            #print(self.start_screen_2_timer)
            if self.start_screen_2_timer <= 0:
                self.start_screen_2_timer = self.start_screen_2_timer_old
                self.start_screen_2 = False
                self.start_screen_3 = True
        if self.start_screen_3:
            self.draw_start_screen_3(rpg)
            self.start_screen_3_timer -= 1
            #print(self.start_screen_3_timer)
            if self.start_screen_3_timer <= 0:
                self.start_screen_3_timer = self.start_screen_3_timer_old
                self.start_screen_3 = False
                self.title_screen = True
                self.game_name_rect.midbottom = self.screen_rect.center
                self.game_name_rect_bigger.center = self.game_name_rect.center
                #self.game_name_rect.y += self.top_margin      
        if self.title_screen:
            """"""
            self.draw_title_screen()
            self.title_screen_timer -= 1
            if self.title_screen_timer <= 0:
                self.game_name_rect.midtop = self.screen_rect.midtop
                self.game_name_rect.y += self.top_margin
                self.game_name_rect_bigger.center = self.game_name_rect.center
                self.title_screen = False
                self.opening_menu = True
                self.start_stuff = False
                pygame.mouse.set_visible(True)
                self.title_screen_timer = self.title_screen_timer_old

            
class Top_Scores():
    """This is the top scores hold"""

    def __init__(self,rpg):
        """Initialize the top scores."""
        self.top_score_list = []
        

        self.load_top_scores(rpg)



    def load_top_scores(self,rpg):
        """this loads the top scores"""
        path = Path('high_scores_save.json')
        
        try:
            contents = path.read_text()
            information_loaded = json.loads(contents)
        except:
            self.top_score_list.append(0)
            self.top_score_list.append(0)
            self.top_score_list.append(0)
            self.save_top_scores(rpg)
            
    def display_top_scores(self,rpg):
        """This displays the top scores on the screen."""



    def add_score(self,score_to_add):
        """This adds a score to the list."""
        self.top_score_list.append(score_to_add)
        

    def update_top_scores(self):
        """this updates the top scores"""
        self.top_score_list.sort(reverse=True)


    def save_top_scores(self,rpg):
        """"""
        path = Path('high_scores_save.json')
        contents = json.dumps(self.top_score_list)
        path.write_text(contents)

